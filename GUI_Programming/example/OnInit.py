import wx

class MyApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(parent=None, title='Hello!')
        frame.Show(True)
        return True

if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()