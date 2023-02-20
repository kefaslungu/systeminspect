import wmi, wx, subprocess

class Frame(wx.Frame):
    def __init__(self):
        super().__init__(None, wx.ID_ANY, title = "bios info By Kefas J Lungu")

        self.pnl = wx.Panel(self)

        self.bios(self.pnl)
        self.Show(True)

    def bios(self, parent):
        bios_mode = subprocess.getoutput(["powershell","$env:firmware_type"])
        c = wmi.WMI()
        for bios in c.Win32_BIOS():
            bios_info = (f"Bios information:\n"
                f"Manufacturer: {bios.Manufacturer}\n"
                f"Bios Mode: {bios_mode}\n"
                f"SMBIOS Version: {bios.SMBIOSBIOSVersion}\n"
                f"Version: {bios.Version}\n"
                f"Embedded Controller Major Version: {bios.EmbeddedControllerMajorVersion}\n"
                f"Embedded Controller Minor Version: {bios.EmbeddedControllerMinorVersion}\n"
                f"Current language: {bios.CurrentLanguage}\n"
                f"Installable Languages: {bios.InstallableLanguages}\n"
                f"List of Languages: {bios.ListOfLanguages}\n"
                f"Serial Number: {bios.SerialNumber}\n"
                f"Status: Bios is {bios.Status}\n")

        wx.TextCtrl(self.pnl, -1, bios_info, size = (1500, 1500), style = (wx.TE_MULTILINE | wx.TE_READONLY))

if(__name__ == '__main__'):
    app = wx.App()    #have to instantiates the App class
    frame = Frame()    #instantiate the Frame subclass above
    app.MainLoop()    #call the App's MainLoop method to handle waiting events