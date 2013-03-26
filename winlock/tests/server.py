import threading
import logging
import unittest
from commands.lock_commands import lock_command
from commands.lock_commands import unlock_command
import network.server
import network.client
import tests.helper
import time
import configurator
import socket
import httplib
from windows_locker import desktop_locker

class TestServer(unittest.TestCase):
  """Test the server class
      Testing strategy in general is to start a server in one thread,
      then in the main thread to make requests to it and see if it
      is doing what it should.
  """
  def createLogger(self):
    self.logger = logging.getLogger('TestServer')
    self.logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    self.logger.addHandler(ch)

  def setUp(self):
    self.createLogger()

  def test_server_starts_locked(self):
    print "No Test Here"
    #create mock object for locker
    #start server
    #check that mock object got lock call
    #stop server

  def test_server_can_receive_lock_command(self):
    print "Interpret Lock Command"
    port = 4450
    host = 'localhost'
    s = network.server.https_command_server(host, port,
          socket.socket(), server_key=self.server_key(),
          server_certificate=self.server_certificate(),
          client_certificate=self.client_certificate(),
          number_of_connections = 2)
    s.start()
    time.sleep(2)
    c = network.client.https_command_client(host, port, self.client_certificate(), self.client_key())
    c.send_command(lock_command().command_string())
    time.sleep(2)
    c.send_command(unlock_command().command_string())
    s.join()

  def server_certificate(self):
    return '../cert/certificate.pem'

  def server_key(self):
    return '../cert/key.pem'

  def client_certificate(self):
    return '../cert/client.crt'

  def client_key(self):
    return '../cert/client.key'

if __name__ == '__main__':
  unittest.main()

