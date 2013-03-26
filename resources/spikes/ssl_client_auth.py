## {{{ http://code.activestate.com/recipes/117004/ (r1)
#!/usr/bin/env python

import httplib

CERTFILE = 'cert/client.crt'
KEYFILE = 'cert/client.key'
HOSTNAME = 'localhost'
PORT = 4443

conn = httplib.HTTPSConnection(
	HOSTNAME,
	PORT,
	key_file = KEYFILE,
	cert_file = CERTFILE
)
conn.putrequest('GET', '/')
conn.endheaders()
response = conn.getresponse()
print response.read()
## end of http://code.activestate.com/recipes/117004/ }}}

