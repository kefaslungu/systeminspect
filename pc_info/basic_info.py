# basic_info.py
# A part of System inspect
# This file is covered by the GNU General Public License.
# Copyright (C) 2023 kefaslungu

import wmi

def basicInfo():
    """Provides all the necessary basic information about your operating system, and your hard ware."""
    c = wmi.WMI()
    for win in c.Win32_OperatingSystem():
        os_info = (f"OS name: {win.Caption}.\n"
               f"OS Manufacturer: {win.Manufacturer}.\n"
               f"Version: {win.Version}.\n"
               f"Build number: {win.BuildNumber}.\n"
               f"Windows Serial number: {win.SerialNumber}.\n")

    for computer in c.Win32_ComputerSystem():
        pc_info = (f"Computer name: {computer.Name}.\n"
               f"PC manufacturer: {computer.Manufacturer}.\n"
               f"System model: {computer.Model}.\n"
               f"System type: {computer.SystemType}.\n"
               f"System family: {computer.SystemFamily}.\n"
               f"System SKU: {computer.SystemSKUNumber}.\n"
               f"Owner: {computer.PrimaryOwnerName}.\n"
               f"DNSHostName: {computer.DNSHostName}.\n"
               f"A Hypervisor is present: {computer.HypervisorPresent}.\n")
    about_windows =f"{os_info}{pc_info}"
    return about_windows  

