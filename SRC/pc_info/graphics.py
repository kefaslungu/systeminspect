# graphics.py
# A part of System inspect
# This file is covered by the GNU General Public License.
# Copyright (C) 2023 kefaslungu
import wmi

def graphicsInfo():
    properties_list = []
    for controller in wmi.WMI().Win32_VideoController():
        properties = (
            "Caption: {}".format(controller.Caption),
            "Driver version: {}".format(controller.DriverVersion),
            "Driver date: {}".format(controller.DriverDate),
            "AdapterCompatibility: {}".format(controller.AdapterCompatibility),
            "AdapterDACType: {}".format(controller.AdapterDACType),
            "AdapterRAM: {}".format(controller.AdapterRAM),
            "Availability: {}".format(controller.Availability),
            "CurrentBitsPerPixel: {}".format(controller.CurrentBitsPerPixel),
            "CurrentHorizontalResolution: {}".format(controller.CurrentHorizontalResolution),
            "CurrentNumberOfColors: {}".format(controller.CurrentNumberOfColors),
            "CurrentNumberOfColumns: {}".format(controller.CurrentNumberOfColumns),
            "CurrentNumberOfRows: {}".format(controller.CurrentNumberOfRows),
            "CurrentRefreshRate: {}".format(controller.CurrentRefreshRate),
            "CurrentScanMode: {}".format(controller.CurrentScanMode),
            "CurrentVerticalResolution: {}".format(controller.CurrentVerticalResolution),
            "DitherType: {}".format(controller.DitherType),
            "MaxRefreshRate: {}".format(controller.MaxRefreshRate),
            "MinRefreshRate: {}".format(controller.MinRefreshRate),
            "Monochrome: {}".format(controller.Monochrome),
            "Name: {}".format(controller.Name),
            "PNPDeviceID: {}".format(controller.PNPDeviceID),
            "SystemName: {}".format(controller.SystemName),
            "VideoArchitecture: {}".format(controller.VideoArchitecture),
            "VideoMemoryType: {}".format(controller.VideoMemoryType),
            "VideoModeDescription: {}".format(controller.VideoModeDescription),
            "VideoProcessor: {}".format(controller.VideoProcessor),
            "Status: {}".format(controller.Status),
        )
        properties_list.extend(properties)
    return '\n'.join(properties_list)

#graphicsInfo()