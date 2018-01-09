import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="GridSizer Example")
        self.SetSize(300,170)
        self.mainPanel= wx.Panel(self)

        self.gridSizer= wx.GridSizer(rows=4, cols=3,hgap=5,vgap=5)

        self.buttons = (
            wx.Button(self.mainPanel, label="1"),
            wx.Button(self.mainPanel, label="2"),
            wx.Button(self.mainPanel, label="3"),
            wx.Button(self.mainPanel, label="4"),
            wx.Button(self.mainPanel, label="5"),
            wx.Button(self.mainPanel, label="6"),
            wx.Button(self.mainPanel, label="7"),
            wx.Button(self.mainPanel, label="8"),
            wx.Button(self.mainPanel, label="9"),
            wx.Button(self.mainPanel, label="*"),
            wx.Button(self.mainPanel, label="0"),
            wx.Button(self.mainPanel, label="#"),
            )

        for button in self.buttons:
            self.gridSizer.Add(button,0, wx.EXPAND)

        self.vtBoxSizer = wx.BoxSizer(wx.VERTICAL)
        self.vtBoxSizer.Add(self.gridSizer, 1, wx.EXPAND, 5)
        self.mainPanel.SetSizer(self.vtBoxSizer)


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    frame.Show()

    app.MainLoop()