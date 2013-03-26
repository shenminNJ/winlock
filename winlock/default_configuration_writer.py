import ConfigParser

config = ConfigParser.RawConfigParser()

config.add_section('Server')
config.set('Server', 'certificate', '../cert/certificate.pem')
config.set('Server', 'private_key', '../cert/key.pem')
config.set('Server', 'bind_address', 'localhost')
config.set('Server', 'port', '4443')
config.add_section('Client')
config.set('Client', 'certificate', '../cert/client.crt')
config.set('Client', 'private_key', '../cert/client.key')

# Writing our configuration file to 'example.cfg'
with open('winlock_config.ini', 'wb') as configfile:
  config.write(configfile)
