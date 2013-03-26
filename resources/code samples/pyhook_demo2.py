import pyHook
import pythoncom
import datetime
from datetime import datetime, date, time

hookManager = pyHook.HookManager()

def onKeyboardEvent(event):
     if event.KeyID == 113: # F2
	print "F2 pushed!\n"
	print datetime.now()
	
     return True

hookManager.KeyDown = onKeyboardEvent
hookManager.HookKeyboard()
pythoncom.PumpMessages()

