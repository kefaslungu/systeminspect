import subprocess, wmi
import wx

def get_size(bytes):
    """
    Scale bytes to its proper format
    e.g:
    1253656 => '1.20MB'
    1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "KB", "MB", "GB", "TB", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}"
        bytes /= factor

class Frame(wx.Frame):
    def __init__(self):
        super().__init__(None, wx.ID_ANY, title = "CPU and mutherboard info By Kefas J Lungu")

        self.pnl = wx.Panel(self)

        self.cpu_stats(self.pnl)
        self.Show(True)

    def cpu_stats(self, parent):
        cpu = subprocess.getoutput('wmic cpu get name, caption, deviceid, numberofcores, status, maxclockspeed /format:list').replace('\n\n\n', '')
        #results = f" CPU and motherboard information:\nCPU:\n{cpu}\nMotherbotard information:\n{motherboard_info  }"



        wx.TextCtrl(self.pnl, -1, cpu, size = (1500, 1500), style = (wx.TE_MULTILINE | wx.TE_READONLY))

if(__name__ == '__main__'):
    app = wx.App()    #have to instantiates the App class
    frame = Frame()    #instantiate the Frame subclass above
    app.MainLoop()    #call the App's MainLoop method to handle waiting events