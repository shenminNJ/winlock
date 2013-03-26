import traceback
import socket
import ssl
import BaseHTTPServer
import SimpleHTTPServer
import threading
import httplib
import json
import windows_locker
import configurator

class command_for_locking_server:
  command_type = "lock"
  def __init__(self, command_string):
    self.from_string(command_string)
  def command_string(self):
    return "{ \"command\" : \"" + self.command_type + "\" }"
  def from_string(self, command_string):
    print "command_string: " + command_string
    self.command_type = json.loads(command_string)['command']

class lock_command(command_for_locking_server):
  def __init__(self):
    self.command_type = "lock"

class unlock_command(command_for_locking_server):
  def __init__(self):
    self.command_type = "unlock"

class command_response:
  def __init__(self, response_text):
    response = json.loads(response_text)
    self.success = response['success']
