import wx
from pc_info import *
class Frame(wx.Frame):
    def __init__(self):
        super().__init__(None, wx.ID_ANY, title="SystemInspect")
        self.pnl = wx.Panel(self)
        self.pchealth(self.pnl)
        self.Show(True)
        
    def pchealth(self, parent):
        notebook = wx.Notebook(parent)
        functions = ((bios.bios(), 'Bios information'), (cpu.cpu_stats(), 'Cpu information'), (disks.disk_info(), 'Disk information'), (motherboard.motherboard(), 'Motherboard information'), (ram.ram_info(), 'Ram information'),) 
        for handler, label in functions:
            page = wx.Panel(notebook)
            sizer = wx.BoxSizer(wx.VERTICAL)
            text_ctrl = wx.TextCtrl(page, -1, value=handler, style=wx.TE_MULTILINE | wx.TE_READONLY)
            sizer.Add(text_ctrl, 1, wx.EXPAND)
            page.SetSizer(sizer)
            notebook.AddPage(page, label)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(notebook, 1, wx.EXPAND)
        parent.SetSizer(sizer)
        
if __name__ == '__main__':
    app = wx.App()
    frame = Frame()
    app.MainLoop()
