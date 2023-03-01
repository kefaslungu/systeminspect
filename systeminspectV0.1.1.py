#System inspect
# This file is covered by the GNU General Public License.
# Copyright (C) 2023 kefaslungu

import wx
"""this is the main file for the System inspect utility. Please see the readme file for what it does."""
from pc_info import (
basic_info,
battery,
bios,
cpu,
disks,
motherboard,
ram,
sound,
startup
)

class Frame(wx.Frame):
    """This is the class that inherit the wx frame, and all other functions are written in this class, or is used to call other functions else wheree."""
    def __init__(self):
        super().__init__(None, wx.ID_ANY, title="System InspectV0.1.1 by Kefas Lungu")
        self.pnl = wx.Panel(self)
        self.pc_inspect(self.pnl)
        self.Show(True)
        
    def pc_inspect(self, parent):
        """This function collects all functions from the pc_info module, and creates a wx.Notebook instance for all the functions it can get"""
        notebook = wx.Notebook(parent)
        functions = ((basic_info.basicInfo(), 'basic windows information'), (battery.battery_information(), 'Battery information'), (bios.bios(), 'Bios information'), (cpu.cpu_stats(), 'Cpu information'), (disks.disk_info(), 'Disk information'), (motherboard.motherboard(), 'Motherboard information'), (ram.ram_info(), 'Ram information'), (sound.sound(), 'sound information'), (startup.startup(), 'Startup items'))
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
