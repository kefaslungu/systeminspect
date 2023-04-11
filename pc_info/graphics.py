# graphics.py
# A part of System inspect
# This file is covered by the GNU General Public License.
# Copyright (C) 2023 kefaslungu
import wmi

def graphics():
    for cards in wmi.WMI().Win32_VideoController():
        