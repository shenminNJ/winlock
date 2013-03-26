
import traceback
import socket
import ssl
import SimpleHTTPServer

SSL = True
PORT = 4443 if SSL else 80

def do_request(connstream, from_addr):
    x = object()
    SimpleHTTPServer.SimpleHTTPRequestHandler(connstream, from_addr, x)

def serve():
    bindsocket = socket.socket()
    bindsocket.bind(('localhost', PORT))
    bindsocket.listen(5)
    
    print("serving on port", PORT)
    
    while True:
        try:
            newsocket, from_addr = bindsocket.accept()
            if SSL:
                connstream = ssl.wrap_socket(newsocket,
                                            server_side=True,
                                            certfile='cert/certificate.pem',
                                            keyfile='cert/key.pem',
                                            ca_certs='cert/client.crt',
                                            #ssl_version=ssl.PROTOCOL_TLSv1,
                                            cert_reqs=ssl.CERT_REQUIRED)
            else:
                connstream = newsocket
            
            do_request(connstream, from_addr)
            
        except Exception:
            traceback.print_exc()

serve()
