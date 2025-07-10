# bios.py
# A part of System inspect
# This file is covered by the GNU General Public License.
# Copyright (C) 2023 kefaslungu

import io
import subprocess
import wmi

def bios():
    """Provides information about your BIOS."""
    bios_mode = subprocess.getoutput(["powershell", "$env:firmware_type"])
    bios_info_list = [
        "Bios information:",
        "Manufacturer: {}",
        "Bios Mode: {}".format(bios_mode),
        "SMBIOS Version: {}",
        "Version: {}",
        "Embedded Controller Major Version: {}",
        "Embedded Controller Minor Version: {}",
        "Current language: {}",
        "Installable Languages: {}",
        "List of Languages: {}",
        "Serial Number: {}",
        "Status: Bios is {}"
    ]
    bios_info_str_io = io.StringIO()
    c = wmi.WMI()
    for bios in c.Win32_BIOS():
        bios_info_str_io.write('\n'.join(bios_info_list).format(
            bios.Manufacturer,
            bios.SMBIOSBIOSVersion,
            bios.Version,
            bios.EmbeddedControllerMajorVersion,
            bios.EmbeddedControllerMinorVersion,
            bios.CurrentLanguage,
            bios.InstallableLanguages,
            bios.ListOfLanguages,
            bios.SerialNumber,
            bios.Status
        ))
        bios_info_str_io.write('\n')
    bios_info_str = bios_info_str_io.getvalue()
    bios_info_str_io.close()
    return bios_info_str 
