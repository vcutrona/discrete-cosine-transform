from __future__ import division
import numpy as np
from scipy.fftpack import dct
from scipy.fftpack import idct


class LocalDCT:

    def __init__(self, image, matrix_qn, value_n):

        # Initialize variables
        self.matrix_qn = matrix_qn
        self.image = image
        self.value_n = value_n

    def local_dct(self):

        # Execute DCT2 in all arrays 8*N
        for x in range(0, self.image.shape[0], 8 * self.value_n):
            for y in range(0, self.image.shape[1], 8 * self.value_n):
                matrix = self.image[x: x + 8 * self.value_n, y: y + 8 * self.value_n]
                self.image[x: x + 8 * self.value_n, y: y + 8 * self.value_n] = self.l_dct(matrix)

    def local_idct(self):

        # Execute I-DCT2 in all arrays 8*N
        for x in range(0, self.image.shape[0], 8 * self.value_n):
            for y in range(0, self.image.shape[1], 8 * self.value_n):
                matrix = self.image[x: x + 8 * self.value_n, y: y + 8 * self.value_n]
                self.image[x: x + 8 * self.value_n, y: y + 8 * self.value_n] = self.l_idct(matrix)

        # Check values
        for i in range(len(self.image)):
            for j in range(len(self.image[0])):
                if self.image[i][j] < 0:
                    self.image[i][j] = 0
                if self.image[i][j] > 255:
                    self.image[i][j] = 255

    def local_quantization(self):
        for x in range(0, self.image.shape[0], 8 * self.value_n):
            for y in range(0, self.image.shape[1], 8 * self.value_n):
                div = self.image[x][y] // self.matrix_qn[x % (8 * self.value_n)][y % (8 * self.value_n)]
                if np.fabs(self.image[x][y] - self.matrix_qn[x % (8 * self.value_n)][y % (8 * self.value_n)] * div) \
                        > np.fabs(self.image[x][y] - self.matrix_qn[x % (8 * self.value_n)][y % (8 * self.value_n)] * (div + 1)):
                    self.image[x][y] = div + 1
                else:
                    self.image[x][y] = div

    def local_dequantization(self):
        for x in range(0, self.image.shape[0], 8 * self.value_n):
            for y in range(0, self.image.shape[1], 8 * self.value_n):
                self.image[x][y] = self.image[x][y] * self.matrix_qn[x % (8 * self.value_n)][y % (8 * self.value_n)]

    # Compute DCT2
    @staticmethod
    def l_dct(matrix):
        return dct(dct(matrix, axis=1, norm='ortho'), axis=0, norm='ortho')

    # Compute I-DCT2
    @staticmethod
    def l_idct(matrix):
        return idct(idct(matrix, axis=0, norm='ortho'), axis=1, norm='ortho')

    def get_image_compressed(self):
        return self.image
