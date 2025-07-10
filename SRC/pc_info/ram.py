# ram.py
# A part of System inspect
# This file is covered by the GNU General Public License.
# Copyright (C) 2023 kefaslungu

import subprocess
import psutil
import wmi

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
            
def ram_info():
    """Returns all information about your ram, from usage to hard ware information."""
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

    basic_ram_info = (f"Total ram installed: {get_size(memory_usage.total)}\n"
    f"Available: {get_size(memory_usage.available)} ram available\n"
    f"Used: {get_size(memory_usage.used)}\n"
    f"Percentage: {get_size(memory_usage.percent)}% used")
    ram_info = f"{technical_ram_info}Ram usage statistics:\n{basic_ram_info}\n"
    return ram_info
