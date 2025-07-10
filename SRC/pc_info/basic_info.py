# basic_info.py
# A part of System inspect
# This file is covered by the GNU General Public License.
# Copyright (C) 2023 kefaslungu

import wmi

def basicInfo():
    """Provides all the necessary basic information about your operating system, and your hardware."""
    c = wmi.WMI()

    os_info = ["OS name: {}\n"
               "OS Manufacturer: {}\n"
               "Version: {}\n"
               "Build number: {}\n"
               "Windows Serial number: {}\n".format(win.Caption, win.Manufacturer, win.Version, win.BuildNumber, win.SerialNumber) for win in c.Win32_OperatingSystem()]

    pc_info = ["Computer name: {}\n"
               "PC manufacturer: {}\n"
               "System model: {}\n"
               "System type: {}\n"
               "System family: {}\n"
               "System SKU: {}\n"
               "Owner: {}\n"
               "DNSHostName: {}\n"
               "A Hypervisor is present: {}\n".format(computer.Name, computer.Manufacturer, computer.Model, computer.SystemType, computer.SystemFamily, computer.SystemSKUNumber, computer.PrimaryOwnerName, computer.DNSHostName, computer.HypervisorPresent) for computer in c.Win32_ComputerSystem()]

    about_windows = "\n".join(os_info) + "\n" + "\n".join(pc_info)

    return about_windows
