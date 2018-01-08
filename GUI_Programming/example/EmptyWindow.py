import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,parent=None,title='Empty Window')


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    frame.Show()

    app.MainLoop()