# sound.py
# A part of System inspect
# This file is covered by the GNU General Public License.
# Copyright (C) 2023 kefaslungu

import wmi

def sound():
    """Gathers information about the sound devices connected to this PC."""
    sound_device = ''
    for device in wmi.WMI().win32_SoundDevice():
        sound_device += (f"Sound device: {device.Caption}.\n"
        f"Device description: {device.Description}.\n"
        f"Manufacturer: {device.Manufacturer}.\n"
        f"Device ID: {device.DeviceID}.\n")
    return sound_device
