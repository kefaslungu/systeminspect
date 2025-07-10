# cpu.py
# A part of System inspect
# This file is covered by the GNU General Public License.
# Copyright (C) 2023 kefaslungu

import wmi

def cpu_stats():
    """Provides basic information about your cpu."""
    c = wmi.WMI()
    cpu_info = ''
    for cpu in c.Win32_Processor():
        cpu_info+=(f"CPU name: {cpu.Name}.\n"
        f"Manufacturer: {cpu.Manufacturer}.\n"
        f"Current clock speed: {cpu.CurrentClockSpeed}.\n"
        f"Maximum clock speed: {cpu.MaxClockSpeed}.\n"
        f" Number of cores: {cpu.NumberOfCores}.\n"
        f"Number of enabled cores: {cpu.NumberOfEnabledCore}.\n"
        f"Logical processors: {cpu.NumberOfLogicalProcessors}.\n"
        f"Serial number: {cpu.ProcessorId}.\n"
        f"Number of threads: {cpu.ThreadCount}.\n"
        f"Architecture: {cpu.Architecture}.\n")
    return cpu_info
