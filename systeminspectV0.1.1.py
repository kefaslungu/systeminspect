"""
System inspect
This file is covered by the GNU General Public License.
Copyright (C) 2023 kefaslungu
this is the main file for the System inspect utility. Please see the readme file for what it does."""

from subprocess import run
from os import system
from threading import Thread as t
import winreg
import wx
from pyperclip import copy
from pc_info import (
    basic_info,
    battery,
    bios,
    cpu,
    disks,
    motherboard,
    network_info,
    ram,
    sound,
    startup)

class Frame(wx.Frame):
    """This is the class that inherit the wx frame, and all other functions are written in this class, or is used to call other functions else where."""
    def __init__(self):
        super().__init__(None, wx.ID_ANY, title="System InspectV0.1.1 by Kefas Lungu")
        self.pnl = wx.Panel(self)

        self.system_inspect(self.pnl)
        self.Show()

    def new_user(self, event):
        dlg = wx.Dialog(self, title="Create New User", size=(400, 300))
        pnl = wx.Panel(dlg)
        label1 = wx.StaticText(pnl, wx.ID_ANY, "Input the new user name:")
        text1 = wx.TextCtrl(pnl, wx.ID_ANY, value="")
        label2 = wx.StaticText(pnl, wx.ID_ANY, "Input the new password:")
        text2 = wx.TextCtrl(pnl, wx.ID_ANY, value="", style=wx.TE_PASSWORD)
        label3 = wx.StaticText(pnl, wx.ID_ANY, "Confirm the new password:")
        text3 = wx.TextCtrl(pnl, wx.ID_ANY, value="", style=wx.TE_PASSWORD)
        ok_btn = wx.Button(pnl, wx.ID_OK, label="OK")
        cancel_btn = wx.Button(pnl, wx.ID_CANCEL, label="Cancel")
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        button_sizer.AddStretchSpacer()
        button_sizer.Add(ok_btn, 0, wx.ALIGN_BOTTOM | wx.ALL, 5)
        button_sizer.Add(cancel_btn, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(label1, 0, wx.ALIGN_LEFT | wx.ALL, 5)
        sizer.Add(text1, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(label2, 0, wx.ALIGN_LEFT | wx.ALL, 5)
        sizer.Add(text2, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(label3, 0, wx.ALIGN_LEFT | wx.ALL, 5)
        sizer.Add(text3, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(button_sizer, 0, wx.EXPAND | wx.ALL, 5)
        pnl.SetSizer(sizer)
        dlg.ShowModal()
        if dlg.GetReturnCode() == wx.ID_OK and text2.GetValue() == text3.GetValue():
            cmd = ["net", "user", text1.GetValue(), text2.GetValue(), "/add"]
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode == 0:
                wx.MessageBox("User created successfully!", "Success", wx.OK | wx.ICON_INFORMATION)
            else:
                wx.MessageBox(f"Error creating user: {result.stderr}", "Error", wx.OK | wx.ICON_ERROR)
        elif dlg.GetReturnCode() == wx.ID_OK:
            wx.MessageBox("Passwords do not match!", "Error", wx.OK | wx.ICON_ERROR)
        dlg.Destroy()

    def password_change(self, event):
        dlg = wx.Dialog(self, title="Change password for current user", size=(400, 300))
        username = os.environ['USERNAME']
        pnl = wx.Panel(dlg)
        label1 = wx.StaticText(pnl, wx.ID_ANY, "user name:")
        CurrentUserName = wx.TextCtrl(pnl, wx.ID_ANY, value=username, style = wx.TE_READONLY)
        label2 = wx.StaticText(pnl, wx.ID_ANY, f"Input the new password for {username}:")
        text2 = wx.TextCtrl(pnl, wx.ID_ANY, value="", style=wx.TE_PASSWORD)
        label3 = wx.StaticText(pnl, wx.ID_ANY, "Confirm the new password:")
        text3 = wx.TextCtrl(pnl, wx.ID_ANY, value="", style=wx.TE_PASSWORD)
        ok_btn = wx.Button(pnl, wx.ID_OK, label="OK")
        cancel_btn = wx.Button(pnl, wx.ID_CANCEL, label="Cancel")
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        button_sizer.AddStretchSpacer()
        button_sizer.Add(ok_btn, 0, wx.ALIGN_BOTTOM | wx.ALL, 5)
        button_sizer.Add(cancel_btn, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(label1, 0, wx.ALIGN_LEFT | wx.ALL, 5)
        sizer.Add(CurrentUserName, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(label2, 0, wx.ALIGN_LEFT | wx.ALL, 5)
        sizer.Add(text2, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(label3, 0, wx.ALIGN_LEFT | wx.ALL, 5)
        sizer.Add(text3, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(button_sizer, 0, wx.EXPAND | wx.ALL, 5)
        pnl.SetSizer(sizer)
        dlg.ShowModal()
        if dlg.GetReturnCode() == wx.ID_OK and text2.GetValue() == text3.GetValue():
            cmd = ["net", "user", username, text2.GetValue()]
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode == 0:
                wx.MessageBox(f"{username}'s password was changed successfully!", "Success", wx.OK | wx.ICON_INFORMATION)
            else:
                wx.MessageBox(f"Error changing {username}'s password: {result.stderr}", "Error", wx.OK | wx.ICON_ERROR)
        elif dlg.GetReturnCode() == wx.ID_OK:
            wx.MessageBox("Passwords do not match!", "Error", wx.OK | wx.ICON_ERROR)
        dlg.Destroy()

    def password_management(self, event):
        """the main purpose of this function is to collect information from the user on what password settings the user wants to change"""
        dlg = wx.Dialog(None, title="Password Management")
        pnl = wx.Panel(dlg)    
        label1 = wx.StaticText(pnl, wx.ID_ANY, "Input the maximum password age (in days):")
        text1 = wx.TextCtrl(pnl, wx.ID_ANY, value="")
        label2 = wx.StaticText(pnl, wx.ID_ANY, "Input the minimum length of a password 0-14:")
        text2 = wx.TextCtrl(pnl, wx.ID_ANY, value="")
        label3 = wx.StaticText(pnl, wx.ID_ANY, "Input the minimum password age (in days):")
        text3 = wx.TextCtrl(pnl, wx.ID_ANY, value="")
        label4 = wx.StaticText(pnl, wx.ID_ANY, "Input the number of unique new passwords:")
        text4 = wx.TextCtrl(pnl, wx.ID_ANY, value="")
        ok_button = wx.Button(pnl, wx.ID_OK)
        cancel_button = wx.Button(pnl, wx.ID_CANCEL)
    
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(label1, 0, wx.ALIGN_LEFT | wx.ALL, 5)
        sizer.Add(text1, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(label2, 0, wx.ALIGN_LEFT | wx.ALL, 5)
        sizer.Add(text2, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(label3, 0, wx.ALIGN_LEFT | wx.ALL, 5)
        sizer.Add(text3, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(label4, 0, wx.ALIGN_LEFT | wx.ALL, 5)
        sizer.Add(text4, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(ok_button, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        sizer.Add(cancel_button, 0, wx.ALIGN_CENTER | wx.ALL, 5)
    
        pnl.SetSizer(sizer)
        sizer.Fit(dlg)
    
        result = dlg.ShowModal()
        if result == wx.ID_OK:
            try:
                max_password_age = int(text1.GetValue())
                min_password_length = int(text2.GetValue())
                min_password_age = int(text3.GetValue())
                num_unique_passwords = int(text4.GetValue())
            except ValueError:
                wx.MessageBox("All input values must be integers!", "Error", wx.OK | wx.ICON_ERROR)
                return
    
            # Construct the net accounts command with the specified options
            cmd = f"net accounts /maxpwage:{max_password_age} /minpwlen:{min_password_length} " \
                  f"/minpwage:{min_password_age} /uniquepw:{num_unique_passwords}"
    
            # Execute the command using subprocess.run()
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode == 0:
                wx.MessageBox("Password rules updated successfully!", "Success", wx.OK | wx.ICON_INFORMATION)
            else:
                wx.MessageBox(f"Error updating password rules: {result.stderr}", "Error", wx.OK | wx.ICON_ERROR)
        dlg.Destroy()

    def password_complexity(self, event):
        dlg = wx.Dialog(None, wx.ID_ANY, "Password Complexity")
        button1 = wx.Button(dlg, wx.ID_ANY, label="Enable Password Complexity Requirements")
        button2 = wx.Button(dlg, wx.ID_ANY, label="Disable Password Complexity Requirements")
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(button1, 0, wx.ALL, 5)
        sizer.Add(button2, 0, wx.ALL, 5)
        dlg.SetSizer(sizer)
        def enable_password_complexity(event):
            """the function that implements the enabling of password complexity"""
            try:
                key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, 
                   r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Passwords")
                winreg.SetValueEx(key, "PasswordComplexity", 0, winreg.REG_DWORD, 1)
                winreg.CloseKey(key)
                wx.MessageBox("Password complexity has been enabled successfully.", "Success", wx.OK | wx.ICON_INFORMATION)
                dlg.Destroy()
            except Exception as e:
                wx.MessageBox("An error occurred while enabling password complexity:\n\n{}".format(str(e)), "Error", wx.OK | wx.ICON_ERROR)
                dlg.Destroy()
    
        def disable_password_complexity(event):
            """the function that implements the disabling of password complexity"""
            try:
                key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                                     "SYSTEM\\CurrentControlSet\\Services\\Netlogon\\Parameters", 
                                     0, 
                                     winreg.KEY_WRITE)
                winreg.SetValueEx(key, "RequireStrongKey", 0, winreg.REG_DWORD, 0)
                winreg.CloseKey(key)
                wx.MessageBox("Password complexity has been disabled successfully.", "Success", wx.OK | wx.ICON_INFORMATION)
                dlg.Destroy()
            except Exception as e:
                wx.MessageBox("An error occurred while disabling password complexity:\n\n{}".format(str(e)), "Error", wx.OK | wx.ICON_ERROR)
                dlg.Destroy()
    
        button1.Bind(wx.EVT_BUTTON, enable_password_complexity)
        button2.Bind(wx.EVT_BUTTON, disable_password_complexity)
    
        dlg.ShowModal()
        dlg.Destroy()

    def create_button(self, parent, label, handler):
        btn = wx.Button(parent, label=label)
        btn.Bind(wx.EVT_BUTTON, handler)
        return btn

    def admin(self, parent):
        admin_rights = (
        (self.new_user, 'create a new user'),
        (self.password_management, 'manage multiple password settings'),
        (self.password_complexity, 'create Password complexity'),
        (self.enable_admin_account, 'enable your builtin administrative account'),
        (self.disable_admin_account, 'Disable your builting administrative account'),
        (self.password_change, 'Change the password for the current user'))
        buttons = []
        for handler, label in admin_rights:
            buttons.append(self.create_button(parent, label, handler))
        return buttons
    
    def pc_inspect(self, parent):
        """This function collects all functions from the pc_info module, and creates a wx.Button instance for all the functions it can get"""
        functions = (
            (basic_info.basicInfo, 'basic windows information'),
            (battery.battery_information, 'Battery information'),
            (bios.bios, 'Bios information'),
            (cpu.cpu_stats, 'Cpu information'),
            (disks.disk_info, 'Disk information'),
            (motherboard.motherboard, 'Motherboard information'),
            (network_info.networkCards, 'networkCards'),
            (ram.ram_info, 'Ram information'),
            (sound.sound, 'sound information'),
            (startup.startup, 'Startup items'),
            (self.msinfo, 'View windows system information'))
        buttons = []
        for handler, label in functions:
            btn = wx.Button(parent, label=label)
            if handler == self.msinfo:  # check if the handler is msinfo because it doesn't return a dialog box like other functions.
                btn.Bind(wx.EVT_BUTTON, lambda event, handler=handler, label=label: handler())  # execute the handler directly to avoid calling the `show_info` function that generates the dialog box, because we don't need it.
            else:
                btn.Bind(wx.EVT_BUTTON, lambda event, handler=handler, label=label: self.show_info(handler, label))
            buttons.append(btn)
        return buttons

    def show_info(self, handler, label):
        """This function shows the information generated by the function in a dialog box"""
        info = handler()
        dlg = wx.Dialog(self, wx.ID_ANY, label, size=(500, 500))
        text_ctrl = wx.TextCtrl(dlg, wx.ID_ANY, value=info, style=wx.TE_MULTILINE | wx.TE_READONLY)

        # Add a 'Copy to Clipboard' button
        copy_button = wx.Button(dlg, wx.ID_ANY, "Copy to Clipboard")
        copy_button.Bind(wx.EVT_BUTTON, lambda event, info=info: copy(info))
                
        # Add an 'Okay' button to close the dialog box.
        ok_button = wx.Button(dlg, wx.ID_OK)
        ok_button.SetDefault()
        # Create a horizontal sizer to hold the buttons
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        button_sizer.Add(copy_button, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        button_sizer.Add(ok_button, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        # Create a vertical sizer to hold the text control and the button sizer
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(text_ctrl, 1, wx.ALL | wx.EXPAND, 5)
        sizer.Add(button_sizer, 0, wx.ALIGN_RIGHT)
        dlg.SetSizer(sizer)
        
        dlg.ShowModal()
        dlg.Destroy()
    def system_inspect(self, parent):
        notebook = wx.Notebook(parent)
        functions = ((self.pc_inspect, 'system information'), (self.admin, 'user settings'))
        for handler, label in functions:
            page = wx.Panel(notebook)
            sizer = wx.BoxSizer(wx.VERTICAL)
            page.SetSizer(sizer)
            notebook.AddPage(page, label)
            buttons = handler(page)
            button_sizer = wx.BoxSizer(wx.HORIZONTAL)
            for button in buttons:
                button_sizer.Add(button, 1, wx.EXPAND)
            sizer.Add(button_sizer, 1, wx.EXPAND)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(notebook, 1, wx.EXPAND)
        parent.SetSizer(sizer)

    # find little functions below, those that need little     or no much gui.
    # starting with enabling and disabling administrative account respectively.
    def enable_admin_account(self, parent):
        cmd = ['net', 'user', 'administrator', '/active:yes']
        result = subprocess.run(cmd, shell=True)
        if result.returncode == 0:
            wx.MessageBox("Your built-in Administrator account has been enabled successfully!\nHowever, It is recommended to disable it when not needed.", "Success", wx.OK | wx.ICON_INFORMATION)
        else:
            wx.MessageBox(f"Error enabling built-in Administrator account: {result.stderr}", "Error", wx.OK | wx.ICON_ERROR)

    def disable_admin_account(self, parent):
        cmd = ['net', 'user', 'administrator', '/active:no']
        result = subprocess.run(cmd, shell=True)
        if result.returncode == 0:
            wx.MessageBox("Your administrative account has been disabled successfully!", "Success", wx.OK | wx.ICON_INFORMATION)
        else:
            wx.MessageBox(f"Error disabling administrative account: {result.stderr}", "Error", wx.OK | wx.ICON_ERROR)

    def msinfo(self):
        t1 = t(target=run, args=("msinfo32",))
        t1.start()

# a function that exit the application
    def exit(self, parent):
        self.Close()

if __name__ == '__main__':
    app = wx.App()
    frame = Frame()
    app.MainLoop()