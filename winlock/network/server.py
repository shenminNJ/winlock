import logging
import traceback
import socket
import ssl
import BaseHTTPServer
import SimpleHTTPServer
import threading
import httplib
import json
import configurator
from windows_locker import desktop_locker
import tempfile
import os
import sys
from commands.lock_commands import command_for_locking_server

class https_command_server(threading.Thread):

  def createLogger(self):
    self.logger = logging.getLogger('https_command_server')
    self.logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    self.logger.addHandler(ch)

  def __init__(self, host, port, socket=socket.socket(), server_key='', server_certificate='', client_certificate='', locker=desktop_locker(), number_of_connections = -1 ):
    threading.Thread.__init__(self)
    self.keep_going = True
    self.ignore_errors = False
    self.port = port
    self.listen_on = host
    self.bindsocket = socket
    self.key = server_key
    self.cert = server_certificate
    self.client_certificate = client_certificate
    self.locker = locker
    self.number_of_connections = number_of_connections
    self.createLogger()

  def interpret_command(self, command):
    if command.command_type == 'lock':
      self.locker.lock()
    if command.command_type == 'unlock':
      self.locker.unlock()

  def stop_server(self):
    self.keep_going = False
    self.ignore_errors = True
    self.locker.turnoff()

  def do_request(self, connstream, from_addr):
    x = object()
    LockingHTTPRequestHandler(connstream, from_addr, x, self)

  def notify_request_handler_of_shutdown(self):
    return True

  def run(self):
    self.serve()

  def serve(self):
    print("PRINT serving on port " + str(self.port) + "\n")
    self.logger.debug("serving on port " + str(self.port))
    self.bindsocket.bind((self.listen_on, self.port))
    self.bindsocket.listen(5)
    accepted_connections = 0

    while self.keep_going and accepted_connections != self.number_of_connections:
      accepted_connections = accepted_connections + 1
      self.logger.debug("Accepting command number " + str(accepted_connections))
      (newsocket, from_addr) = self.bindsocket.accept()
      self.logger.debug("got a request " + str(accepted_connections) + " on socket\n")
      try:
        connstream = ssl.wrap_socket(newsocket,
              server_side=True,
              certfile=self.cert,
              keyfile=self.key,
              ca_certs=self.client_certificate,
              cert_reqs=ssl.CERT_REQUIRED)
        self.do_request(connstream, from_addr)
      except Exception as e :
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print "Exception: ", e
        self.logger.debug("Exception on connection: " + str(exc_type) )

    self.logger.debug("Reached last socket connection\n")
    self.locker.turnoff()
    self.bindsocket.close()

class LockingHTTPRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
  objectvar = "sometext"
  def __init__(self, request, client_address, server, interpreter):
    self.interpreter = interpreter
    BaseHTTPServer.BaseHTTPRequestHandler.__init__(self, request, client_address, server)

  def flush(self):
    message = "\r\n{ \"success\": true }\r\n"
    self.send_response(200)
    self.end_headers()
    self.wfile.write(message)
    self.wfile.flush()
    self.connection.shutdown(1)
    return

  def do_POST(self):
    content_len = int(self.headers.getheader('content-length'))
    post_body = self.rfile.read(content_len)
    locking_command = command_for_locking_server(post_body)
    self.interpreter.interpret_command(locking_command)
    self.flush()
    return

class https_command_client:

  def __init__(self, server_address, config):
    self.server_address = server_address
    self.server_port = config.port
    self.certfile = config.client_certificate
    self.keyfile = config.client_key

  def send_command(self, command):
    conn = httplib.HTTPSConnection(
        self.server_address,
        self.server_port,
        key_file = self.keyfile,
        cert_file = self.certfile,
      )
    conn.request('POST', '/', command.command_string())
    response = conn.getresponse()
    response_text = response.read()
    return command_response(response_text)

class certificate:
  def __init__(self, string_representation):
    self.certificate = string_representation

  def as_file(self):
    temp = tempfile.NamedTemporaryFile()
    temp.write(self.certificate)
    temp.flush()
    return temp

  def file(self):
    return self.as_file().name
