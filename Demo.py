import os
import wx
from cStringIO import StringIO

MAIN_WINDOW_DEFAULT_SIZE = (500, 300)

class Processing:

    def __init__(self, image_path):
        self.image_path = image_path

        x = wx.ImageFromStream(self.image_path)

        image = wx.Image.LoadFile(x, type=wx.BITMAP_TYPE_BMP)

        print image

class Frame(wx.Frame):
    
    def __init__(self, parent, id, title):
        style=wx.DEFAULT_FRAME_STYLE ^ (wx.RESIZE_BORDER) # XOR to remove the resizeable border        
        wx.Frame.__init__(self, parent, id, title=title, size=MAIN_WINDOW_DEFAULT_SIZE, style=style)
        self.Center() # open in the centre of the screen
        self.panel = wx.Panel(self)

        self.image_path = ''

        self.CreateMenuBar()

    def CreateMenuBar(self):

        "Create a menu bar with Open, Exit items"
        menuBar = wx.MenuBar()
        # Tell our Frame about this MenuBar
        self.SetMenuBar(menuBar)
        menuFile = wx.Menu()
        menuBar.Append(menuFile, '&File')
        # NOTE on wx ids - they're used everywhere, we don't care about them
        # Used to handle events and other things
        # An id can be -1 or wx.ID_ANY, wx.NewId(), your own id
        # Get the id using object.GetId()
        fileOpenMenuItem = menuFile.Append(-1, '&Open Image', 'Open a picture')
        #print "fileOpenMenuItem.GetId()", fileOpenMenuItem.GetId()
        self.Bind(wx.EVT_MENU, self.OnOpen, fileOpenMenuItem)

        # add a 'mirror' option, disable it for now
        # we add mirrorMenuItem to self so that we can reference it later
        #self.mirrorMenuItem = menuFile.Append(-1, '&Mirror Image', 'Mirror the image horizontally')
        #self.mirrorMenuItem.Enable(False) # we can't mirror an image until we've loaded one in, so start with 'mirror' disabled
        #self.Bind(wx.EVT_MENU, self.OnMirrorImage, self.mirrorMenuItem)
        
        # create a menu item for Exit and bind it to the OnExit function       
        exitMenuItem = menuFile.Append(-1, 'E&xit', 'Cancel')
        self.Bind(wx.EVT_MENU, self.OnExit, exitMenuItem)
        
        # add a Help menu with an About item
        #menuHelp = wx.Menu()
        #menuBar.Append(menuHelp, '&Help')
        #helpMenuItem = menuHelp.Append(-1, '&About', 'About screen')
        #self.Bind(wx.EVT_MENU, self.OnAbout, helpMenuItem)

    def OnOpen(self, event):
        dlg = wx.FileDialog(self, message="Open an Image...", defaultDir=os.getcwd(), defaultFile="", style=wx.OPEN)
        
        # Call the dialog as a model-dialog so we're required to choose Ok or Cancel
        if dlg.ShowModal() == wx.ID_OK:
            self.image_path = dlg.GetPath()

        p = Processing(self.image_path)

                        
        dlg.Destroy() # we don't need the dialog any more so we ask it to clean-up
        
    def OnExit(self, event):
        self.Destroy()
        
    
class App(wx.App):
    
    def OnInit(self):

        self.frame = Frame(parent=None, id=-1, title='Fourier Transform Configurator')
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True
    
if __name__ == "__main__":

    app = App(redirect=False)
    app.MainLoop()