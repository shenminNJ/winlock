import ConfigParser
import os

class configurator:
  def __init__(self, configfile):
    config = ConfigParser.RawConfigParser()
    config.read(configfile)
    self.certificate = config.get('Server', 'certificate')
    self.private_key = config.get('Server', 'private_key')
    self.bind_address = config.get('Server', 'bind_address')
    self.port = config.getint('Server', 'port')
    self.client_certificate = config.get('Client', 'certificate')
    self.client_key = config.get('Client', 'private_key')
    self.validate()

  def validate(self):
    if not os.path.exists(self.certificate):
      print "Certificate does not exist: " + self.certificate
    if not os.path.exists(self.private_key):
      print "Private key file does not exist: " + self.private_key

if __name__ == "__main__":
  conf = configurator('winlock_config.ini')
  print "configuration:\n"
  print conf.certificate + "\n"
  print conf.private_key + "\n"
  print conf.bind_address + "\n"
  print conf.port + "\n"
