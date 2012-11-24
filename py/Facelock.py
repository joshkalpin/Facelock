import wx
import time
import UserLoader as loader
import PasswordHasher as hasher

class StartScreen(wx.Frame):
  
    def __init__(self, parent, title):
        super(StartScreen, self).__init__(parent, title=title, size=(390, 180),
                style=wx.CAPTION|wx.CLOSE_BOX)
        self.controller = loader.UserController()
        self.pw_hasher = hasher.PasswordHasher()
        self.button_text = "Lock!"

        self.InitBasicUI()
        if self.controller.is_empty():
            self.InitEntryUI()

        self.InitUI()
        self.Centre()
        self.Show()
        self.closes = 0
        
    def InitBasicUI(self):
        self.root = wx.Panel(self)
        self.font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        self.font.SetPointSize(9)
        self.root_layout = wx.BoxSizer(wx.VERTICAL)


    def InitEntryUI(self):
        info_row = wx.BoxSizer(wx.HORIZONTAL)

        info_text = wx.StaticText(self.root, style=wx.ALIGN_CENTRE, label="It appears there are no users created, please enter your information to create a user")
        info_text.SetFont(self.font)
        info_text.Wrap(400)
        info_row.Add(info_text, flag=wx.CENTRE, border=8)
        
        self.root_layout.Add(info_row, border=9)
        self.root_layout.Add((-1, 10))
        self.button_text = "Create!"

    def InitUI(self):
        username_row = wx.BoxSizer(wx.HORIZONTAL)

        usr_name_text = wx.StaticText(self.root, label='Username')
        usr_name_text.SetFont(self.font)
        username_row.Add(usr_name_text, flag=wx.RIGHT, border=8)

        self.usr_name_ctrl = wx.TextCtrl(self.root)
        username_row.Add(self.usr_name_ctrl, proportion=1)
        self.root_layout.Add(username_row, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        self.root_layout.Add((-1, 10))

        pw_row = wx.BoxSizer(wx.HORIZONTAL)

        pwd_text = wx.StaticText(self.root, label='Password')
        pwd_text.SetFont(self.font)
        pw_row.Add(pwd_text, flag=wx.RIGHT, border=8)

        self.pwd_ctrl = wx.TextCtrl(self.root, style=wx.TE_PASSWORD)
        pw_row.Add(self.pwd_ctrl, proportion=1)

        self.root_layout.Add(pw_row, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        self.root_layout.Add((-1, 10))

        self.sub_button = wx.Button(self.root, label=self.button_text)
        self.sub_button.Bind(wx.EVT_BUTTON, self.button_submit)

        self.root_layout.Add(self.sub_button, proportion=1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP,border=10)
        self.root_layout.Add((-1,10))

        self.root.SetSizer(self.root_layout)

        self.Bind(wx.EVT_CLOSE, self.close)


    def button_submit(self, e):
        usr = self.usr_name_ctrl.GetValue()
        pwd = self.pwd_ctrl.GetValue()

        if self.controller.is_empty():
            pw_hash = self.pw_hasher.encode(pwd)
            new_user = loader.User(0, usr, str(time.time()), pw_hash)
            self.controller.addUser(new_user)
            self.controller.load_users()
        else:
            pw_hash = self.pw_hasher.encode(pwd)
            for u in self.controller.users:
                if u.password == pw_hash and u.name == usr:
                    print "huzzah!"

    def close(self, e):
        self.Destroy()



if __name__ == '__main__':
  
    app = wx.App()
    StartScreen(None, title='Go To Class')
    app.MainLoop()
