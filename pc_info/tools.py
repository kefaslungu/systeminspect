from subprocess import run
from threading import Thread as t

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
    t1 = t(target=run, args=("eventvwr.msc",))
    t1.start()

def systemConfiguration(event):
    t1 = t(target=run, args=("msconfig",))
    t1.start()

def diskCleanup(event):
    t1 = t(target=run, args=("cleanmgr",))
    t1.start()

def diskDefragmenter(event):
    t1 = t(target=run, args=("v",))
    t1.start()

def windowsMemoryDiagnostic(event):
    t1 = t(target=run, args=("mdsched",))
    t1.start()

def system_scan(event):
    t1 = t(target=run, args=("sfc /scannow",))
    t1.start()

def directXDiagnosticTool(event):
    t1 = t(target=run, args=("dxdiag",))
    t1.start()

def uninstaller(event):
    t1 = t(target=run, args=("arpwiz.cpl"))
    t1.start()

def maliciousRemoval(event):
    t1 = t(target=run, args=("mrt",))#Microsoft Windows Malicious Software Removal Tool
    t1.start()

def advanceFireWall(event):
    t1 = t(target=run, args=("wf.msc",))
    t1.start()

def sysReset(event):
    t1 = t(target=run, args=("systemreset",))
    t1.start()

def fireWall(event):
    t1 = t(target=run, args=("firewall.cpl",))
    t1.start()

def msinfo(self, event):
    t1 = t(target=run, args=("msinfo32",))
    t1.start()
