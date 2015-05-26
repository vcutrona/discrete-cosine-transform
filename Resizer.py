import numpy as np


class Resizer:
    def __init__(self, image, n_value):
        self.image = image
        self.n_value = n_value
        self.new_image = []

        # Resize the image
        self.resize()

    def resize(self):

        row = self.image.shape[0]
        column = self.image.shape[1]

        print row
        print column

        if divmod(row, (8 * self.n_value))[1] != 0:

            n_row = row
            while divmod(n_row, (8 * self.n_value))[1] != 0:
                n_row += 1

        else:
            n_row = row

        if divmod(column, (8 * self.n_value))[1] != 0:

            n_column = column
            while divmod(n_column, (8 * self.n_value))[1] != 0:
                n_column += 1

        else:
            n_column = column

        print 'Righe:', n_row, ' Colonne:', n_column

        self.new_image = np.zeros(shape=(n_row, n_column))

        # estendiamo l'immagine
        for i in range(len(self.image)):
            for j in range(len(self.image[0])):
                self.new_image[i][j] = self.image[i][j]
        #prendiamo l'ultima riga, l'ultima colonna e l'ultimo elemento in basso a destra
        last_row = self.image[-1, :]
        last_col = self.image[:, -1]
        last_element = self.image[-1, -1]

        for i in range(row, n_row):
            for j in range(0, column):
                self.new_image[i][j] = last_row[j]

        for x in range(column, n_column):
            for z in range(0, row):
                self.new_image[z][x] = last_col[z]

        for g in range(column, n_column):
            for h in range(row, n_row):
                self.new_image[h][g] = last_element

        return self.get_new_image()


    def get_new_image(self):
        return self.new_image
