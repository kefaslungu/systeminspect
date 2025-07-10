
#menubar for the application
import wx
from tools import win_tools
#subclass the wx.MenuBar
class Menubar(wx.MenuBar):

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.__createMenuItem()


    #methods defined

    #get information about each menu item
    def __menuInfo(self):
        return (
        ('&File',    #for the file menu item
            (('&Open File...\tctrl+o', self.on_openFile),
            ('&Save File...\tctrl+s', self.on_saveFile),
            ('&Print File...\tctrl+p', self.on_printFile),
            ('&Exit Program...\talt+f4', self.on_exit),)),

        ('&Builtin windows diagnostic tools',
            (('&Driver verefy\tshift+v', win_tools.driverVerifier),
            ('& Task Manager\tshift+t', win_tools.taskManager),
            ('&Resource Monitor\tshift+r', win_tools.resourceMonitor),
            ('&Event Viewer\tshift+e', win_tools.eventViewer),
            ('&System Configuration\tshift+c', win_tools.systemConfiguration),
            ('&Disk Cleanup\tshift+d', win_tools.diskCleanup),
            ('&Disk Defragmenter\tshift+f', win_tools.diskDefragmenter),
            ('&Windows Memory Diagnostic\tshift+i', win_tools.windowsMemoryDiagnostic),
            ('&Basic system scan: [SFC]\tshift+b', win_tools.system_scan),
            ('&Direct X Diagnostic Tool\tshift+x', win_tools.directX),
            ('&Programs and features\tshift+u', win_tools.uninstaller),
            ('&Windows malicious removal tool\tshift+m', win_tools.maliciousRemoval),
            ('&fireWall\tshift+w', win_tools.fireWall),
            ('&Advance FireWall\tshift+a', win_tools.advanceFireWall),
            ('& PC system information\tshift+p', win_tools.msinfo),
        ('&sysReset\tshift+esc', win_tools.sysReset),)),

        ('&View/Page',    #for the view/page menu item
            (('&Zoom In \talt+i', self.on_zoomIn),
            ('&Zoom Out\talt+o', self.on_zoomOut),
            ('&Go To Page...\tctrl+g', self.on_goToPage),
            ('&Adjust Fonts...\talt+f', self.on_adjustFont),)),

        ('&Advance',    #for the advance menu item
            (('&Check Word Meaning...\tctrl+w', self.on_checkWord),
            ('&Access Rich Knowledge Enhancement (RKE)\tctrl+r', self.on_rke),
            ('&Download More Books From Here\tctrl+d', self.on_downloadBook),
            ('&Get More Voices From Here\tctrl+g', self.on_getVoices),)),

        ('&Help',    #for the help menu item
            (('&About EBAR...\tctrl+a', self.on_about),
            ('&User\'s Guide\tctrl+h', self.on_userGuide),
            ('&View License\tctrl+l', self.on_license),
            ('&Visit Website\talt+w', self.on_website),)),
        )

    #create each menu item and add it to the menubar
    def __createMenuItem(self):
        for menuItem,  menuItemInfo in self.__menuInfo():
            menu= wx.Menu()
            for item in menuItemInfo:
                menuChild = menu.Append(wx.ID_ANY, item[0])
                self.parent.Bind(wx.EVT_MENU, item[1], menuChild)
            menu.AppendSeparator()
            self.Append(menu, menuItem)


    #events associated to this class
    #file menu item
    def on_openFile(self, event):
        pass

    def on_saveFile(self, event):
        pass

    def on_printFile(self, event):
        pass

    def on_exit(self, event):
        self.parent.Close()

    #for the edit menu item
    def on_copy(self, event):
        pass

    def on_cut(self, event):
        pass

    def on_paste(self, event):
        pass

    def on_undo(self, event):
        pass

    #for the pview/page menu item
    def on_zoomIn(self, event):
        pass

    def on_zoomOut(self, event):
        pass

    def on_goToPage(self, event):
        pass

    def on_adjustFont(self, event):
        pass

    #for the advance menu item
    def on_checkWord(self, event):
        pass

    def on_rke(self, event):
        pass

    def on_downloadBook(self, event):
        pass

    def on_getVoices(self, event):
        pass

    #for the help menu item
    def on_about(self, event):
        pass

    def on_userGuide(self, event):
        pass

    def on_license(self, event):
        pass

    def on_website(self, event):
        pass
