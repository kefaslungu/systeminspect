import subprocess
import psutil
import wmi
import wx
import memory_converter

class Frame(wx.Frame):
    def __init__(self):
        super().__init__(None, wx.ID_ANY, title = "System Health Check By Kefas J Lungu")

        self.pnl = wx.Panel(self)

        self.disk_info(self.pnl)
        self.Show(True)

    def disk_info(self, parent):
        """ this function helps to gather all theneeded information for the hard drives connected to this pc."""
        c = wmi.WMI()
        disk_stats = ''
        partitions = psutil.disk_partitions()
        count = len(partitions)
        for disk in c.Win32_DiskDrive():
            ...
        for partition in partitions:
            try:
                usage = psutil.disk_usage(partition.mountpoint)
            except:
                continue
            disk_stats += (f"Drive volume: {partition.device}\n"
            f"Drive letter: {partition.device[:2]}\n"
            f"Total memory: {memory_converter.get_size(usage.total)}.\n"
            f"Space used: {memory_converter.get_size(usage.used)}.\n"
            f"Free space: {memory_converter.get_size(usage.free)}.\n"
            f"Manufacturer: {disk.Manufacturer}\n"
            f"Model: {disk.Model}\n"
            f"Serial number: {disk.SerialNumber}\n"
            f"Media type: {disk.MediaType}\n"
            f"Interface type: {disk.InterfaceType}\n"
            f"DeviceID: {disk.DeviceID}\n"
            f"Disk status: {disk.Status}\n"
            f"__________\n")

            DiskUsage = (f"Disk partitions and Usage.\n"
            f"List of partitions on This PC: {count}.\n"
            f"{disk_stats}")
        wx.TextCtrl(self.pnl, -1, DiskUsage, size = (1500, 1500), style = (wx.TE_MULTILINE | wx.TE_READONLY))

if(__name__ == '__main__'):
    app = wx.App()    #have to instantiates the App class
    frame = Frame()    #instantiate the Frame subclass above
    app.MainLoop()    #call the App's MainLoop method to handle waiting events
