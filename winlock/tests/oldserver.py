import threading
import logging
import unittest
import commands.lock_commands
import network.server
import network.client
import tests.helper
import time
import configurator
import mox
import socket
import httplib

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

  def test_server_can_receive_lock_command(self):
    port = 4450
    host = 'localhost'
    s = network.server.https_command_server(host, port,
          socket.socket(), server_key=self.server_key(),
          server_certificate=self.server_certificate(),
          client_certificate=self.client_certificate())
    t = threading.Thread( target=s.serve, args=(1,) )
    t.start()
    time.sleep(2)
    c = network.client.https_command_client(host, port, self.client_certificate(), self.client_key())
    c.send_command('lock')
    t.join()

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

