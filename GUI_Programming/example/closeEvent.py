import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,parent=None,title="Close Event")
        self.Bind(wx.EVT_CLOSE, self.OnClose)

    def OnClose(self,event):
        if wx.MessageBox("윈도우를 닫을까요?","확인", wx.YES_NO) != wx.YES:
            event.Skip(False)
        else:
            self.Destroy()

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    frame.Show()

    app.MainLoop()