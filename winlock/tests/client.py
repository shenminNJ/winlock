import threading
import logging
import unittest
import commands.lock_commands
import network.server
import network.client
import time
import configurator
import mox
import socket
import ssl

class TestClient(unittest.TestCase):
  def createLogger(self):
    self.logger = logging.getLogger('TestClient')
    self.logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    self.logger.addHandler(ch)

  def setUp(self):
    self.createLogger()

  def test_client_connects_to_socket(self):
    try:
      port = 4448
      host = 'localhost'
      command = ''
      c = network.client.https_command_client(host, port, '', '' )
      s = socket.socket()
      s.bind((host, port))
      s.listen(5)
      s.settimeout(2)
      serverthread = threading.Thread( target=s.accept ).start()
      c.send_command(command)
      serverthread.join()
    except ssl.SSLError:
      self.logger.debug('SSL Error expected')
      pass
      return
    except Exception as e:
      self.logger.debug("Error({0}): {1}".format(e.errno, e.strerror))
      self.fail('unexpected exception')


if __name__ == '__main__':
  unittest.main()

