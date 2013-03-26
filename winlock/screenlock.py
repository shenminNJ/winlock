import wx

class OverlayFrame( wx.Frame )  :

    def __init__( self )  :

        wx.Frame.__init__( self, None, title="Transparent Window",
                           style=wx.DEFAULT_FRAME_STYLE | wx.STAY_ON_TOP )

        self.ShowFullScreen( True )
        self.alphaValue = 200
        self.SetTransparent( self.alphaValue )

    def OnCloseWindow( self, evt ) :
        self.Destroy()

#end OverlayFrame class

#=======================================================

if __name__ == '__main__' :

    app = wx.App( False )
    frm = OverlayFrame()
    frm.Show()
    app.MainLoop()
