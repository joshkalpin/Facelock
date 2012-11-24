import wx

class ScreenSaver(wx.Frame):

	def __init__(self, parent, title):
		super(ScreenSaver, self).__init(parent, title=title, size = wx.DisplaySize())
  51    