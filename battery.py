import subprocess
import wmi
import psutil
import wx
class Frame(wx.Frame):
    def __init__(self):
        super().__init__(None, wx.ID_ANY, title = "")

        self.pnl = wx.Panel(self)

        self.battery_info(self.pnl)
        self.Show(True)

    def battery_info(self, parent):
        battery = psutil.sensors_battery()
        batteryInfo = {
        "has_battery": str(subprocess.getoutput(["powershell", "@(Get-CimInstance -ClassName Win32_Battery).Count -gt 0 "])),
        "battery_percentage": battery.percent,
        "on_power": battery.power_plugged,
        "secs": battery.secsleft,
        "number_of_battery": str(subprocess.getoutput(["powershell", "@(Get-CimInstance -ClassName Win32_Battery).Count"]))}
        c = wmi.WMI()
        for battery in c.query("SELECT * FROM Win32_Battery"):
            battery_info = (f"PC has battery: {batteryInfo['has_battery']}\n"
            f"Number of installed batteries: {batteryInfo['number_of_battery']}\n"
            f"Battery type: {battery.Caption}\n"
            f"Battery percentage: {batteryInfo['battery_percentage']}%\n"
            f"Power plugged: {batteryInfo['on_power']}\n"
        f"Remaining time until full charge: {batteryInfo['secs']}\n"
            f"Design voltage: {battery.DesignVoltage}\n"
            f"Battery id: {battery.DeviceID}\n"
            f"Battery name: {battery.Name}\n"
            f"Battery status: {battery.Status}\n")


        wx.TextCtrl(parent, -1, battery_info, size=(1500, 1500), style=(wx.TE_MULTILINE | wx.TE_READONLY))
if __name__ == '__main__':
    app = wx.App()    #have to instantiates the App class
    frame = Frame()    #instantiate the Frame subclass above
    app.MainLoop()    #call the App's MainLoop method to handle waiting events