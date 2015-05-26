from __future__ import division
import numpy as np

__author__ = 'vinid'


class QMatrix:
    def __init__(self, quality, N):
        self.N = N
        self.qNMatrix = np.zeros(shape=(N*8, N*8))
        self.quality = quality
        self.qMatrix = np.array(
            [[16, 11, 10, 16, 24, 40, 51, 61],
             [12, 12, 14, 19, 26, 58, 60, 55],
             [14, 13, 16, 24, 40, 57, 69, 56],
             [14, 17, 22, 29, 51, 87, 80, 62],
             [18, 22, 37, 56, 68, 109, 103, 77],
             [24, 35, 55, 64, 81, 104, 113, 92],
             [49, 64, 78, 87, 103, 121, 120, 101],
             [72, 92, 95, 98, 112, 100, 103, 99]])

    def getQf(self):
        if self.quality >= 50:
            return (200 - 2 * self.quality) / 100
        else:
            return (5000 / self.quality) / 100

    def quantizationMatrixOne(self):
        return np.rint(self.getQf()*self.qMatrix)

    def transformQOne(self):
        qOne = self.quantizationMatrixOne()

        #for innestati per generare la qnmatrix love from enzo
        for x in range(0, qOne.shape[0]):
            for j in range (0, qOne.shape[1]):
                for v in range(x*self.N, x*self.N + self.N):
                    for t in range(j*self.N, j*self.N + self.N):
                        self.qNMatrix[v][t] = qOne[x][j]

        print qOne
        print self.qNMatrix
