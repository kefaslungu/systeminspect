import subprocess
import psutil
import wmi
import wx
#import memory_converter
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
        
def disk_info():
    """ this function helps to gather all theneeded information for the hard drives connected to this pc."""
    c = wmi.WMI()
    disk_stats = ''
    partitions = psutil.disk_partitions()
    count = len(partitions)
    for disk in c.Win32_DiskDrive():
        ...
    for partition in partitions:
        try:
            usage = psutil.disk_usage(partition.mountpoint)
        except:
            continue
        disk_stats += (f"Drive volume: {partition.device}\n"
        f"Drive letter: {partition.device[:2]}\n"
        f"Total memory: {get_size(usage.total)}.\n"
        f"Space used: {get_size(usage.used)}.\n"
        f"Free space: {get_size(usage.free)}.\n"
        f"Manufacturer: {disk.Manufacturer}\n"
        f"Model: {disk.Model}\n"
        f"Serial number: {disk.SerialNumber}\n"
        f"Media type: {disk.MediaType}\n"
        f"Interface type: {disk.InterfaceType}\n"
        f"DeviceID: {disk.DeviceID}\n"
        f"Disk status: {disk.Status}\n"
        f"__________\n")

        DiskUsage = (f"Disk partitions and Usage.\n"
        f"List of partitions on This PC: {count}.\n"
        f"{disk_stats}")
    return DiskUsage
