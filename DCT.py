from __future__ import division
import numpy as np
from scipy.fftpack import dct

class DCT:
    def __init__(self, qNMatrix, image, N):
        self.qNMatrix = qNMatrix
        self.image = image
        self.N = N

    def localDct(self):
        for x in range(0, self.image.shape[0], 8 * self.N):
            for y in range(0, self.image.shape[1], 8 * self.N):
                matrix = self.image[x: x + 8 * self.N][y: y + 8 * self.N]
                self.image[x: x + 8 * self.N][y: y + 8 * self.N] = self.computeDctAndMultiply(self, matrix)

    def computeDctAndMultiply(self, matrix):
        newMatrix = dct(dct(matrix, norm = 'ortho').T, norm='ortho')
        finalMatrix = np.zeros(shape=(self.N*8, self.N*8))

        #TODO: Controllare
        for x in range(0, self.N * 8):
            for y in range(0, self.N * 8):
                finalMatrix[x][y] = newMatrix[x][y] / self.qNMatrix[x][y]

        return finalMatrix
