import unittest
import os
from network.server import certificate 

class test_certs(unittest.TestCase):
  def test_cert_creates_file(self):
    cert = certificate('foo')
    print(cert.file())
    self.assertTrue(os.path.exists(cert.file()))

if __name__ == '__main__':
    unittest.main()

