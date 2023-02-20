import wx, wmi

class Frame(wx.Frame):
    def __init__(self):
        super().__init__(None, wx.ID_ANY)

        self.pnl = wx.Panel(self)
        self.motherboard(self.pnl)
        self.Show(True)

    def motherboard(self, parent):
        c = wmi.WMI()
        for board in c.Win32_BaseBoard():
            motherboard_info = (f"Motherboard information:\n"
            f"Motherboard Manufacturer: {board.Manufacturer}.\n"
            f"Product: {board.Product}.\n"
            f"Name: {board.Name}.\n"
            f"HostingBoard: {board.HostingBoard}.\n"
            f"HotSwappable: {board.HotSwappable}.\n"
            f"SerialNumber: {board.SerialNumber}.\n"
            f"Version: {board.Version}.\n"
            f"Motherboard is replaceable: {board.Replaceable}.\n"
            f"Motherboardd is Removable: {board.Removable}.\n"
            f"Requires Daughterboard/Daughtercard: {board.RequiresDaughterBoard}.\n"
            f"Motherboard status: {board.Status}.\n")
        
        wx.TextCtrl(self.pnl, -1, motherboard_info, size = (1500, 1500), style = (wx.TE_MULTILINE | wx.TE_READONLY))

        
if(__name__ == '__main__'):
    app = wx.App()    #have to instantiates the App class
    frame = Frame()    #instantiate the Frame subclass above
    app.MainLoop()    #call the App's MainLoop method to handle waiting events