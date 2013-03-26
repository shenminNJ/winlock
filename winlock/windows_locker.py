import wx
import screenlock
import threading
import time

class desktop_locker:
  def __init__(self):
    self.screen = screen_locker()
    self.keyboard = keyboard_locker()
    self.screen.start()

  def is_locked(self):
    return self.screen.is_locked() and self.keyboard.is_locked()

  def lock(self):
    print "Lock Called\n"
    self.keyboard.lock()
    self.screen.lock_screen()

  def unlock(self):
    print "Unlock Called\n"
    self.keyboard.unlock()
    self.screen.unlock_screen()

  def turnoff(self):
    self.screen.turnoff()

class screen_locker(threading.Thread):

  def __init__(self):
    threading.Thread.__init__(self)
    self.ready = False

  def stall_until_ready(self):
    while self.ready == False:
      print "Stalling until setup is finished"
      time.sleep(1)

  def lock_screen(self):
    print "Screenlocker lock Called\n"
    self.stall_until_ready()
    wx.CallAfter( self.frm.Show )
    self.screen_locked = True
    print "Screenlocker lock returned\n"

  def unlock_screen(self):
    print "Screenlocker unlock Called\n"
    self.stall_until_ready()
    wx.CallAfter( self.frm.Hide )
    self.screen_locked = False

  def is_locked(self):
    return self.screen_locked()

  def run(self):
    print "Screenlocker thread started\n"
    self.overlayApp = wx.App(False)
    self.frm = screenlock.OverlayFrame()
    self.ready = True
    print "Screenlocker overlay mainloop\n"
    self.overlayApp.MainLoop()

  def turnoff(self):
    wx.CallAfter(self.frm.Close)

class keyboard_locker:
  def lock(self):
    self.locked = True
    return True
  def unlock(self):
    self.locked = False
    return True
  def is_locked(self):
    return self.locked

if __name__ == '__main__':
  s = screen_locker()
  s.start()
  s.lock_screen()
  time.sleep(5)
  s.unlock_screen()
  time.sleep(5)
  
  print "Calling shutdown on locker"
  s.turnoff()
