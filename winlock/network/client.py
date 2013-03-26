import httplib
import logging
from commands.lock_commands import command_response

class https_command_client:

  def createLogger(self):
    self.logger = logging.getLogger('https_command_client')
    self.logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    self.logger.addHandler(ch)

  def __init__(self, server_address, port, certfile, keyfile):
    self.logger = logging.getLogger('https_command_client')
    self.server_address = server_address
    self.server_port = port
    self.certfile = certfile
    self.keyfile = keyfile
    self.createLogger()

  def send_command(self, command):
    conn = httplib.HTTPSConnection(
        self.server_address,
        self.server_port,
        key_file = self.keyfile,
        cert_file = self.certfile,
      )
    conn.request('POST', '/', command)
    response = conn.getresponse()
    response_text = response.read()
    return command_response(response_text)

