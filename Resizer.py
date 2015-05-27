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

        # Get the new length value of rows
        if divmod(row, (8 * self.n_value))[1] != 0:

            n_row = row
            while divmod(n_row, (8 * self.n_value))[1] != 0:
                n_row += 1

        else:
            n_row = row

        # Get the new length value of columns
        if divmod(column, (8 * self.n_value))[1] != 0:

            n_column = column
            while divmod(n_column, (8 * self.n_value))[1] != 0:
                n_column += 1

        else:
            n_column = column

        # Create the new array with new dimensions
        self.new_image = np.zeros(shape=(n_row, n_column))

        # Copy the old array to the new one
        for i in range(len(self.image)):
            for j in range(len(self.image[0])):
                self.new_image[i][j] = self.image[i][j]

        # Get last elements
        last_row = self.image[-1, :]
        last_col = self.image[:, -1]
        last_element = self.image[-1, -1]

        # Fill the last rows
        for i in range(row, n_row):
            for j in range(0, column):
                self.new_image[i][j] = last_row[j]

        # Fill the last columns
        for x in range(column, n_column):
            for z in range(0, row):
                self.new_image[z][x] = last_col[z]

        # Fill the last value
        for g in range(column, n_column):
            for h in range(row, n_row):
                self.new_image[h][g] = last_element

    def get_image_resized(self):
        return self.new_image
