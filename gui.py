"""
This moudule creates the GUI

"""

import Resizer as rz

from Tkinter import *
import tkFileDialog
import matplotlib.pyplot as plt
from scipy import misc

class GUI:

    imageFile = ""

    def __init__(self, master):
        self.master = master
        master.title("Progeto sulla DCT")

        self.label = Label(master, text="Metodi Del Calcolo Scientifico")
        self.label.pack()

        self.nInput = Text(master, height=1, width=30)
        self.nInput.pack()
        self.nInput.insert(END, "Enter the value for N")

        self.qualityInput = Text(master, height=1, width=30)
        self.qualityInput.pack()
        self.qualityInput.insert(END, "Enter the quality value")

        self.greet_button = Button(master, text="Open Image", command=self.openImage)
        self.greet_button.pack()

        self.process_button = Button(master, text="Process Image", command=root.quit)
        self.process_button.pack()

        self.close_button = Button(master, text="Close", command=exit)
        self.close_button.pack()

    def openImage(self):
        fileName = tkFileDialog.askopenfilename()
        print "Percorso del file: " + fileName
        self.imageFile = misc.imread(fileName)
        #self.imageFile.size
        #print self.imageFile

        resize = rz.Resizer(self.imageFile, 7)
        new_image = resize.get_new_image()

        print new_image

        plt.imshow(new_image, cmap=plt.cm.gray)
        plt.show()

root = Tk()
my_gui = GUI(root)
root.resizable(width=FALSE, height=FALSE)
root.geometry('{}x{}'.format(300, 300))
root.mainloop()