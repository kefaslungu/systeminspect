#more work is comming to this module soon, not yet completed.

import subprocess
import wmi
import wx

def cpu_stats():
    cpu = subprocess.getoutput('wmic cpu get name, caption, deviceid, numberofcores, status, maxclockspeed /format:list').replace('\n\n\n', '')
    return cpu
