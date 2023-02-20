import subprocess
import wx
import psutil
import wmi
import memory_converter
class Frame(wx.Frame):
    def __init__(self):
        super().__init__(None, wx.ID_ANY, title = "System Health Check By Kefas J Lungu")

        self.pnl = wx.Panel(self)

        self.ram_info(self.pnl)
        self.Show(True)

    def ram_info(self, parent):
        memory_usage = psutil.virtual_memory()
        technical_ram_info = ''
        c = wmi.WMI()
        for ram in c.Win32_PhysicalMemory():
            technical_ram_info += (f"Device location: {ram.DeviceLocator}\n"
            f"Manufacturer: {ram.Manufacturer}\n"
            f"Part number: {ram.PartNumber}\n"
            f"Speed: {ram.Speed}\n"
            f"SMBIOS memory type: {ram.SMBIOSMemoryType}\n"
            f"Serial number: {ram.SerialNumber}\n\n")

        basic_ram_info = (f"Total ram installed: {memory_converter.get_size(memory_usage.total)}\n"
        f"Available: {memory_converter.get_size(memory_usage.available)} ram available\n"
        f"Used: {memory_converter.get_size(memory_usage.used)}\n"
        f"Percentage: {memory_converter.get_size(memory_usage.percent)}% used")
        ram_info = f"{technical_ram_info}Ram usage statistics:\n{basic_ram_info}\n"


        wx.TextCtrl(self.pnl, -1, ram_info, size = (1500, 1500), style = (wx.TE_MULTILINE | wx.TE_READONLY))

if(__name__ == '__main__'):
    app = wx.App()    #have to instantiates the App class
    frame = Frame()    #instantiate the Frame subclass above
    app.MainLoop()    #call the App's MainLoop method to handle waiting events
