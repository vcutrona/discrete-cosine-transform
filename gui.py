from numpy import copy
from Resizer import Resizer as rz
from QNMatrix import QNMatrix as qm
from LocalDCT import LocalDCT as ldct

import scipy.misc as misc
import matplotlib.pyplot as plt

from Tkinter import *
import tkFileDialog
import tkMessageBox


class GUI:

    def __init__(self, master):

        # Initialize variables
        self.image = []
        self.image_resized = []
        self.image_final = []
        self.matrix_qn = []

        # Create the GUI
        self.master = master
        master.title("Compressione con la DCT2")

        self.label = Label(master, text="Inserisci il percorso dell'Immagine")
        self.label.pack()

        self.imagePath = Text(master, height=1, width=30)
        self.imagePath.pack()
        self.imagePath.config(highlightbackground='Gray')
        self.imagePath.insert(END, '')

        self.greet_button = Button(master, text="Seleziona Immagine", command=self.openImage)
        self.greet_button.pack()

        self.label = Label(master, text="Inserisci il valore di N:")
        self.label.pack()

        self.nInput = Text(master, height=1, width=10)
        self.nInput.pack()
        self.nInput.config(highlightbackground='Gray')
        self.nInput.insert(END, "")

        self.label = Label(master, text="Inserisci il valore di Qualita:")
        self.label.pack()

        self.qualityInput = Text(master, height=1, width=10)
        self.qualityInput.pack()
        self.qualityInput.config(highlightbackground='Gray')
        self.qualityInput.insert(END, "")

        self.process_button = Button(master, text="Esegui Compressione", command=self.execute)
        self.process_button.pack()

    def openImage(self):

        path = tkFileDialog.askopenfilename()

        if path.strip() != '':
            self.imagePath.delete('1.0', 'end')
            self.imagePath.insert("1.0", path)

    def execute(self):

        # Save all output to file
        sys.stdout = open('Results.txt', 'w')

        # Check if image field is not empty
        if self.imagePath.get('1.0', 'end').strip() != '':

            # Check if N and Quality values are not empty
            if self.nInput.get('1.0', 'end').strip() == '':
                tkMessageBox.showwarning("Valore N", "Inserisci un valore numerico N")
            elif self.qualityInput.get('1.0', 'end').strip() == '':
                tkMessageBox.showwarning("Qualita", "Inserisci un valore numerico di Qualita")
            else:

                # Get input image
                self.image = misc.imread(self.imagePath.get('1.0', 'end').strip()).astype(float)

                # Get N and Quality values
                value_n = int(self.nInput.get('1.0', 'end').strip())
                value_quality = int(self.qualityInput.get('1.0', 'end').strip())

                # Check quality value
                if value_quality > 100:
                    value_quality = 100
                elif value_quality < 0:
                    value_quality = 0

                print 'Valore N:', value_n
                print 'Valore Qualita:', value_quality

                # Resize image to the new dimension
                resizer = rz(self.image, value_n)
                self.image_resized = resizer.get_image_resized()

                # Get the QN Matrix
                matrix_q = qm(value_n, value_quality)
                self.matrix_qn = matrix_q.get_qn()

                # Initialize Local DCT Class
                compression = ldct(copy(self.image_resized), self.matrix_qn, value_n)

                # Execute DCT2
                compression.local_dct()

                # Execute Quantization
                compression.local_quantization()

                # Execute de-quantization
                compression.local_dequantization()

                # Execute I-DCT2
                compression.local_idct()

                # Get the final compressed image
                self.image_final = compression.get_image_compressed()

                self.show_results()
        else:
            tkMessageBox.showwarning("Apertura Immagine", "Selezionare una immagine .bmp")

    def show_results(self):

        # Create the new figure
        figure = plt.figure()

        # Put the resize image
        before = figure.add_subplot(1, 2, 1)
        plt.imshow(self.image_resized, cmap=plt.cm.gray)
        before.set_title('Ridimensionata')

        # Put the compressed image
        after = figure.add_subplot(1, 2, 2)
        plt.imshow(self.image_final, cmap=plt.cm.gray)
        after.set_title('Compressa')

        # Show results
        figure.show()

if __name__ == "__main__":

    window = Tk()
    GUI(window)
    window.resizable(width=FALSE, height=FALSE)
    window.geometry('{}x{}'.format(250, 200))
    window.mainloop()
