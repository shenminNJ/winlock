
  def _test_server_opens_and_closes_port(self):
    s = network.server.https_command_server(host='localhost', port=4443)
    s.start()
    s.stop_server()

  def _test_end_to_end(self):
    config = configurator.configurator('winlock_config.ini')
    s = network.server.https_command_server_thread('localhost', config)
    c = network.client.https_command_client('localhost', config)
    command = commands.lock_commands.lock_command()
    unlock = commands.lock_commands.unlock_command()
    s.start()
    print "Listen thread started\n"
    time.sleep(2)
    print "Sending lock command\n"
    command_result = c.send_command(command)
    time.sleep(3)
    print "Sending unlock command\n"
    command_result = c.send_command(unlock)
    time.sleep(2)
    s.stop_server()
    print "Listen thread stop called\n"
    s.join()
    print "End\n"
    self.assertTrue(command_result.success)

