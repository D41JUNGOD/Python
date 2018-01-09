import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="BoxSizer Example")

        self.mainPanel = wx.Panel(self)
        self.upperPanel = wx.Panel(self.mainPanel)
        self.leftButton = wx.Button(self.upperPanel, label="Left")
        self.rightButton = wx.Button(self.upperPanel, label="Right")

        self.hzBoxSizer = wx.StaticBoxSizer(wx.HORIZONTAL,self.upperPanel, "Upper")
        self.hzBoxSizer.Add(self.leftButton)
        self.hzBoxSizer.Add(self.rightButton)
        self.upperPanel.SetSizer(self.hzBoxSizer)

        self.middleButton = wx.Button(self.mainPanel, label="Middle")
        self.lowerButton = wx.Button(self.mainPanel, label="Lower")

        self.vtBoxSizer = wx.BoxSizer(wx.VERTICAL)
        self.vtBoxSizer.Add(self.upperPanel, 0, wx.ALIGN_LEFT|wx.TOP|wx.LEFT,5)
        self.vtBoxSizer.Add(self.middleButton, 1, wx.EXPAND|wx.ALL,5)
        self.vtBoxSizer.Add(self.lowerButton, 0, wx.ALIGN_RIGHT|wx.RIGHT|wx.BOTTOM,5)

        self.mainPanel.SetSizer(self.vtBoxSizer)

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    frame.Show()

    app.MainLoop()