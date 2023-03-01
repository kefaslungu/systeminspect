# bios.py
# A part of System inspect
# This file is covered by the GNU General Public License.
# Copyright (C) 2023 kefaslungu

import subprocess
import wmi

def bios():
    """Provides information about your bios."""
    bios_mode = subprocess.getoutput(["powershell","$env:firmware_type"])
    c = wmi.WMI()
    for bios in c.Win32_BIOS():
        bios_info = (f"Bios information:\n"
        f"Manufacturer: {bios.Manufacturer}\n"
        f"Bios Mode: {bios_mode}\n"
        f"SMBIOS Version: {bios.SMBIOSBIOSVersion}\n"
        f"Version: {bios.Version}\n"
        f"Embedded Controller Major Version: {bios.EmbeddedControllerMajorVersion}\n"
        f"Embedded Controller Minor Version: {bios.EmbeddedControllerMinorVersion}\n"
        f"Current language: {bios.CurrentLanguage}\n"
        f"Installable Languages: {bios.InstallableLanguages}\n"
        f"List of Languages: {bios.ListOfLanguages}\n"
        f"Serial Number: {bios.SerialNumber}\n"
        f"Status: Bios is {bios.Status}\n")
    return bios_info
