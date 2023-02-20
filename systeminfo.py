import wx

class Frame(wx.Frame):
    def __init__(self):
        super().__init__(None, wx.ID_ANY, "Advance System information By Kefas J Lungu")


        pnl = wx.Panel(self)

        self.Show()   



if(__name__ == '__main__'):
    app = wx.App()    #have to instantiates the App class
    frame = Frame()    #instantiate the Frame subclass above
    app.MainLoop()    #call the App's MainLoop method to handle waiting events
