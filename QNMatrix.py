from __future__ import division
import numpy as np


class QNMatrix:

    def __init__(self, value_n, value_quality):

        self.value_n = value_n
        self.value_quality = value_quality

        # Initialize Arrays
        self.matrix_qn = np.zeros(shape=(value_n * 8, value_n * 8))
        self.matrix_q = np.array(
            [[16, 11, 10, 16, 24, 40, 51, 61],
             [12, 12, 14, 19, 26, 58, 60, 55],
             [14, 13, 16, 24, 40, 57, 69, 56],
             [14, 17, 22, 29, 51, 87, 80, 62],
             [18, 22, 37, 56, 68, 109, 103, 77],
             [24, 35, 55, 64, 81, 104, 113, 92],
             [49, 64, 78, 87, 103, 121, 120, 101],
             [72, 92, 95, 98, 112, 100, 103, 99]])

    # Compute QF
    def get_qf(self):
        if self.value_quality >= 50:
            return (200 - 2 * self.value_quality) / 100
        else:
            return (5000 / self.value_quality) / 100

    # Compute Q1
    def get_quantization_q1(self):
        return np.rint(self.get_qf() * self.matrix_q)

    # Compute QN
    def get_qn(self):

        q1 = self.get_quantization_q1()

        # Create the QN Matrix
        for x in range(0, q1.shape[0]):
            for j in range(0, q1.shape[1]):
                for v in range(x * self.value_n, x * self.value_n + self.value_n):
                    for t in range(j * self.value_n, j * self.value_n + self.value_n):
                        self.matrix_qn[v][t] = q1[x][j]

        return self.matrix_qn
