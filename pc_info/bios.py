import wmi
import wx
import subprocess

def bios():
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
