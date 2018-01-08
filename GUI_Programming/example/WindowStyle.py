import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent = None,title="Window Style")
        self.Bind(wx.EVT_LEFT_DOWN,self.OnMouseLButtonDown)
        self.Bind(wx.EVT_RIGHT_DOWN,self.OnMouseRButtonDown)

    def OnMouseLButtonDown(self, event):
        self.SetWindowStyle(wx.RESIZE_BORDER | wx.CAPTION)

    def OnMouseRButtonDown(self, event):
        self.SetWindowStyle(wx.DEFAULT_FRAME_STYLE)

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    frame.Show()

    app.MainLoop()
