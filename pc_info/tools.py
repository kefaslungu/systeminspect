from subprocess import run
from threading import Thread as t

def driverVerifier():
    t1 = t(target=run, args=("verifier",))
    t1.start()

def taskManager():
    t1 = t(target=run, args=("taskmgr",))
    t1.start()

def resourceMonitor():
    t1 = t(target=run, args=("resmon",))
    t1.start()

def eventViewer():
    t1 = t(target=run, args=("eventvwr.msc",))
    t1.start()

def systemConfiguration():
    t1 = t(target=run, args=("msconfig",))
    t1.start()

def diskCleanup():
    t1 = t(target=run, args=("cleanmgr",))
    t1.start()

def diskDefragmenter():
    t1 = t(target=run, args=("v",))
    t1.start()

def windowsMemoryDiagnostic():
    t1 = t(target=run, args=("mdsched",))
    t1.start()

def system_scan():
    t1 = t(target=run, args=("sfc /scannow",))
    t1.start()

def directXDiagnosticTool():
    t1 = t(target=run, args=("dxdiag",))
    t1.start()

def uninstaller():
    t1 = t(target=run, args=("arpwiz.cpl"))
    t1.start()

    t1 = t(target=run, args=("verifier",))
    t1.start()

