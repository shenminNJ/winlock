import unittest
import commands.lock_commands
import time
import configurator

class TestSSLFuntions(unittest.TestCase):

  def test_passes_requests_to_interpreter(self):
    time.sleep(5)
    config = configurator.configurator('winlock_config.ini')
    s = commands.lock_commands.https_command_server_thread('localhost', config)
    c = commands.lock_commands.https_command_client('localhost', config)
    command = commands.lock_commands.lock_command()
    unlock = commands.lock_commands.unlock_command()
    s.start()
    print "Listen thread started\n"
    time.sleep(5)
    print "Sending lock command\n"
    command_result = c.send_command(command)
    time.sleep(10)
    print "Sending unlock command\n"
    command_result = c.send_command(unlock)
    time.sleep(5)
    s.stop_server()
    print "Listen thread stop called\n"
    s.join()
    print "End\n"
    self.assertTrue(command_result.success)

if __name__ == '__main__':
  unittest.main()

