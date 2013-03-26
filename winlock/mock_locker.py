class desktop_locker:
  def __init__(self):
    self.screen = screen_locker()
    self.keyboard = keyboard_locker()

  def is_locked(self):
    return self.screen.is_locked() and self.keyboard.is_locked()

  def lock(self):
    self.keyboard.lock()
    self.screen.lock()

  def unlock(self):
    self.keyboard.unlock()
    self.screen.unlock()

class screen_locker:
  def lock(self):
    self.locked = True
    return true
  def unlock(self):
    self.locked = False
    return true
  def is_locked(self):
    return self.locked

class keyboard_locker:
  def lock(self):
    self.locked = True
    return true
  def unlock(self):
    self.locked = False
    return true
  def is_locked(self):
    return self.locked
