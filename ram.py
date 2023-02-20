import subprocess
import psutil, wx
import memory_converter
class Frame(wx.Frame):
    def __init__(self):
        super().__init__(None, wx.ID_ANY, title = "System Health Check By Kefas J Lungu")

        self.pnl = wx.Panel(self)

        self.ram_info(self.pnl)
        self.Show(True)

        def ram_info(self, parent):
        memory_usage = psutil.virtual_memory()
        basic_ram_info = subprocess.getoutput('wmic memorychip list full').replace('\n\n', '\n')
        technical_ram_info =f"Total: {memory_converter.get_size(memory_usage.total)}\nAvailable: {memory_converter.get_size(memory_usage.available)}\nUsed: {memory_converter.get_size(memory_usage.used)}\nPercentage: {memory_converter.get_size(memory_usage.percent)}%"
