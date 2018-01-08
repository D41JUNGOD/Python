import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="Simple Button")

        btnClick= wx.Button(self,label = "Click Me!")
        btnClick.Bind(wx.EVT_BUTTON,self.OnBtnClickMe)

    def OnBtnClickMe(self, event):
        wx.MessageBox("Clicked!","Simple Button", wx.OK)


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    frame.Show()

    app.MainLoop()