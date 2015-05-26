
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

        print 'Righe:', n_row,' Colonne:', n_column

        new_image = [[0] * n_column] * n_row

        for row in range(len(new_image)):

            for column in range(len(new_image[0])):
                # 
                # if row > len(new_image):
                #
                #
                # if self.image[row][column] > 255:
                #     new_image[row][column] = 255
                # elif self.image[row][column] < 0:
                #     new_image[row][column] = 0
                # else:
                #     new_image[row][column] = self.image[row][column]


    def get_new_image(self):
        return self.new_image
