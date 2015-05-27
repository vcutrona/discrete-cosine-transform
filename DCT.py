"""
[[231,	32,	233,	161,	24,	71,	140,	245]
[247,	40,	248,	245,	124,	204,	36,	107]
[234,	202,	245,	167,	9,	217,	239,	173]
[193,	190,	100,	167,	43,	180,	8,	70]
[11,	24	210,	177,	81,	243,	8,	112]
[97,	195	203,	47,	125	114,	165,	181]
[193,	70,	174,	167,	41,	30,	127,	245]
[87,	149,	57,	192,	65,	129,	178,	228]]

"""

from __future__ import division
import numpy as np
from scipy.fftpack import dct
from scipy.fftpack import idct
import matplotlib.pyplot as plt


class DCT:
    def __init__(self, qNMatrix, image, N):
        self.qNMatrix = qNMatrix
        self.image = image
        self.N = N

    def localDct(self):
        for x in range(0, self.image.shape[0], 8 * self.N):
            for y in range(0, self.image.shape[1], 8 * self.N):
                print self.image
                # matrix = self.image[x: x + 8 * self.N, y: y + 8 * self.N]

                matrix = np.array([[231,	32,	233,	161,	24,	71,	140,	245],
[247,	40,	248,	245,	124,	204,	36,	107],
[234,	202,	245,	167,	9,	217,	239,	173],
[193,	190,	100,	167,	43,	180,	8,	70],
[11,	24,	210,	177,	81,	243,	8,	112]
,[97,	195,	203,	47,	125,	114,	165,	181],
[193,	70,	174,	167,	41,	30,	127,	245],
[87,	149,	57,	192,	65,	129,	178,	228]])

                # print "Dct applicata a [" + str(x) + "," +  str(x + 8 * self.N) + " ] [" + str(y) + "," +  str(y + 8 * self.N) + " ] "
                #print self.image[x: x + 8 * self.N, y: y + 8 * self.N]
                print "matrix prof"
                print matrix
                #self.image[x: x + 8 * self.N, y: y + 8 * self.N] = self.computeDctAndMultiply(matrix)
                dct2 =  dct(dct(matrix.astype(float), norm='ortho', axis=1), norm='ortho', axis=0)
                print "DCT"
                #print self.image[x: x + 8 * self.N, y: y + 8 * self.N]
                print dct2
                self.image[x: x + 8, y: y + 8] = dct2
                print "image"
                print self.image[x: x + 8, y: y + 8]
                print "goback"
                #print self.goBackDct(self.image[x: x + 8 * self.N, y: y + 8 * self.N])
                print self.goBackDct(self.image[x: x + 8, y: y + 8])


        # ritorno all'immagine originale

        for x in range(0, self.image.shape[0], 8 * self.N):
            for y in range(0, self.image.shape[1], 8 * self.N):
                matrix = self.image[x: x + 8 * self.N, y: y + 8 * self.N]
                self.image[x: x + 8 * self.N, y: y + 8 * self.N] = self.goBackDct(matrix)


    def computeDctAndMultiply(self, matrix):
        newMatrix = dct(dct(matrix.astype(float), norm='ortho', axis=1), norm='ortho', axis=0)
        # finalMatrix = np.zeros(shape=(self.N * 8, self.N * 8))
        return newMatrix

    # per tornare indietro dalla dct
    def goBackDct(self, matrix):
        newMatrix = idct(idct(matrix.astype(float), norm='ortho', axis=0), norm='ortho', axis=1)
        return newMatrix

