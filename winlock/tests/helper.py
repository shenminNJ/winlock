import socket

class port:
  def is_port_open(self, host, port):
    try:
      socket.socket().connect((host, port))
      return True
    except socket.error as a:
      return False
    except Exception:
      print "Unexpected exception"
      return False

if __name__ == '__main__':
  s = socket_helper()
  print "is 4545 open? " + str(s.is_port_open('localhost', 4545))
