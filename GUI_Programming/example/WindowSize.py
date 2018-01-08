import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="Window Size")

        self.Bind(wx.EVT_LEFT_DOWN, self.OnMouseLButtonDown)
        self.Bind(wx.EVT_RIGHT_DOWN, self.OnMouseRButtonDown)
    
    def OnMouseLButtonDown(self,event):
        frame.SetSize(wx.Size(400,200))

    def OnMouseRButtonDown(self,event):
        frame.SetSize(wx.Size(200,400))

if __name__ == '__main__':
        app = wx.App()
        frame = MyFrame()
        frame.Show()

        app.MainLoop()    