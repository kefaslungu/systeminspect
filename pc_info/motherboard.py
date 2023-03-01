# motherboard.py
# A part of System inspect
# This file is covered by the GNU General Public License.
# Copyright (C) 2023 kefaslungu

import wmi

def motherboard():
    """Gathers all information about your motherboard."""
    c = wmi.WMI()
    for board in c.Win32_BaseBoard():
        motherboard_info = (f"Motherboard information:\n"
        f"Motherboard Manufacturer: {board.Manufacturer}.\n"
        f"Product: {board.Product}.\n"
        f"Name: {board.Name}.\n"
        f"HostingBoard: {board.HostingBoard}.\n"
        f"HotSwappable: {board.HotSwappable}.\n"
        f"SerialNumber: {board.SerialNumber}.\n"
        f"Version: {board.Version}.\n"
        f"Motherboard is replaceable: {board.Replaceable}.\n"
        f"Motherboardd is Removable: {board.Removable}.\n"
        f"Requires Daughterboard/Daughtercard: {board.RequiresDaughterBoard}.\n"
        f"Motherboard status: {board.Status}.\n")
        return motherboard_info
