# startup.py
# A part of System inspect
# This file is covered by the GNU General Public License.
# Copyright (C) 2023 kefaslungu

import wmi

def startup():
    """Gets information on all items that start with windows."""
    c = wmi.WMI()
    startupItem = ''
    for startup_item in c.Win32_StartupCommand():
        startupItem += (f"Name: {startup_item.Name}.\n"
        f"Command: {startup_item.Command}.\n"
        f"Location: {startup_item.Location}.\n")
    return startupItem
