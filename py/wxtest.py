import wx

class Example(wx.Frame):
  
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(390, 180),
                style=wx.CAPTION)
            
        self.InitUI()
        self.Centre()
        self.Show()
        self.closes = 0
        
    def InitUI(self):
    
        panel = wx.Panel(self)

        font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(9)

        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)

        usr_name_text = wx.StaticText(panel, label='Username')
        usr_name_text.SetFont(font)
        hbox1.Add(usr_name_text, flag=wx.RIGHT, border=8)

        self.usr_name_ctrl = wx.TextCtrl(panel)
        hbox1.Add(self.usr_name_ctrl, proportion=1)
        vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        vbox.Add((-1, 10))

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)

        pwd_text = wx.StaticText(panel, label='Password')
        pwd_text.SetFont(font)
        hbox2.Add(pwd_text, flag=wx.RIGHT, border=8)

        self.pwd_ctrl = wx.TextCtrl(panel, style=wx.TE_PASSWORD)
        hbox2.Add(self.pwd_ctrl, proportion=1)

        vbox.Add(hbox2, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        vbox.Add((-1, 10))

        self.sub_button = wx.Button(panel, label='submit')
        self.sub_button.Bind(wx.EVT_BUTTON,self.button_submit)

        vbox.Add(self.sub_button, proportion=1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP,border=10)
        vbox.Add((-1,10))

        panel.SetSizer(vbox)

        self.Bind(wx.EVT_CLOSE, self.attempted_close)


    def button_submit(self,e):
        usr = self.usr_name_ctrl.GetValue()
        pwd = self.pwd_ctrl.GetValue()
        if usr == pwd:
            self.close()

    def attempted_close(self,e):
        e.Veto()

    def veto_event(self,e):
        print 'click'
        e.Veto()


    def close(self):
        self.Destroy()



if __name__ == '__main__':
  
    app = wx.App()
    Example(None, title='Go To Class')
    app.MainLoop()