from threading import Thread as t
from subprocess import run, Popen
# builtin windows tools, found on the third tab in the program
def driverVerifier(event):
    t1 = t(target=run, args=("verifier",))
    t1.start()

def taskManager(event):
    t1 = t(target=run, args=("taskmgr",))
    t1.start()

def resourceMonitor(event):
    t1 = t(target=run, args=("resmon",))
    t1.start()

def eventViewer(event):
    t1 = t(target=Popen, args=(['mmc.exe', 'eventvwr.msc'],))
    t1.start()

def systemConfiguration(event):
    t1 = t(target=run, args=("msconfig",))
    t1.start()

def diskCleanup(event):
    t1 = t(target=run, args=("cleanmgr",))
    t1.start()

def diskDefragmenter(event):
    t1 = t(target=run, args=("dfrgui",))
    t1.start()

def windowsMemoryDiagnostic(event):
    t1 = t(target=run, args=("mdsched",))
    t1.start()

def system_scan(event):
    cmd = 'cmd /k start sfc /scannow'
    t1 = t(target=Popen, args=(cmd, shell:=True,))
    t1.start()

def directX(event):
    t1 = t(target=run, args=("dxdiag",))
    t1.start()

def uninstaller(event):
    t1 = t(target=Popen, args=(['rundll32.exe', 'shell32.dll,Control_RunDLL', 'appwiz.cpl'],))
    t1.start()

def maliciousRemoval(event):
    t1 = t(target=run, args=("mrt",))#Microsoft Windows Malicious Software Removal Tool
    t1.start()

def advanceFireWall(event):
    t1 = t(target=Popen, args=(['mmc.exe', 'wf.msc'],))
    t1.start()

def sysReset(event):
    t1 = t(target=run, args=("systemreset",))
    t1.start()

def fireWall(event):
    t1 = t(target=Popen, args=(['rundll32.exe', 'shell32.dll,Control_RunDLL', 'firewall.cpl'],))
    t1.start()

def msinfo(event):
    t1 = t(target=run, args=("msinfo32",))
    t1.start()
