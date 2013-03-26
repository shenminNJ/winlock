#we want to have a thread running some service that responds to external commands
#we want a separate thread that runs a wxWidgets application and responds to messages from first thread
import time
import screenlock
import wx
import threading

class CommandDispatcher:
	def main_loop(self):
		gui = wxGuiExample()
		gui.begin()

		while(True):
			time.sleep(2)
			print "CommandDispatcher: sending show message"
			gui.show()

			time.sleep(2)
			print "CommandDispatcher: sending hide message"
			gui.hide()


class wxGuiExample:
	def __init__(self):
		self.overlayApp = wx.App(False)
		self.frm = screenlock.OverlayFrame()
		
	def main_loop(self):
		print "wxGuiExample: main_loop"
		self.overlayApp.MainLoop()

	def begin(self):
		self.ongoing_thread = threading.Thread(target=self.main_loop, args=(self, ))

	def show(self):
		wx.CallAfter( self.frm.Show )

	def hide(self):
		wx.CallAfter( self.frm.Hide )


cd = CommandDispatcher()
cd.main_loop()