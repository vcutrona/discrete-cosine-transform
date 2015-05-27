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

                #print self.image
                # matrix = self.image[x: x + 8 * self.N, y: y + 8 * self.N]

                # matrix = np.array([[231,	32,	233,	161,	24,	71,	140,	245],
                #                    [247,	40,	248,	245,	124,	204,	36,	107],
                #                    [234,	202,	245,	167,	9,	217,	239,	173],
                #                    [193,	190,	100,	167,	43,	180,	8,	70],
                #                    [11,	24,	210,	177,	81,	243,	8,	112],
                #                    [97,	195,	203,	47,	125,	114,	165,	181],
                #                    [193,	70,	174,	167,	41,	30,	127,	245],
                #                    [87,	149,	57,	192,	65,	129,	178,	228]])

                # print "Dct applicata a [" + str(x) + "," +  str(x + 8 * self.N) + " ] [" + str(y) + "," +  str(y + 8 * self.N) + " ] "
                #print self.image[x: x + 8 * self.N, y: y + 8 * self.N]
                #print "matrix prof"
                #print matrix
                #self.image[x: x + 8 * self.N, y: y + 8 * self.N] = self.dct(matrix)
                #dct2 =  dct(dct(matrix, norm='ortho', axis=1), norm='ortho', axis=0)
                #print "DCT"
                #print self.image[x: x + 8 * self.N, y: y + 8 * self.N]
                #print dct2
                #self.image[x: x + 8, y: y + 8] = dct2
                #print "image"
                #print self.image[x: x + 8, y: y + 8]
                #print "goback"
                #print self.idct(self.image[x: x + 8 * self.N, y: y + 8 * self.N])
                #print self.l_idct(self.image[x: x + 8, y: y + 8])

    def local_idct(self):

        # Execute I-DCT2 in all arrays 8*N
        for x in range(0, self.image.shape[0], 8 * self.value_n):
            for y in range(0, self.image.shape[1], 8 * self.value_n):
                matrix = self.image[x: x + 8 * self.value_n, y: y + 8 * self.value_n]
                self.image[x: x + 8 * self.value_n, y: y + 8 * self.value_n] = self.l_idct(matrix)

    def local_quantization(self):
        return self

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

