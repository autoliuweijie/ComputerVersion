# coding: utf-8
from numpy import *
from cv2 import *
from matplotlib import pyplot as plt


class Example(object):

    @classmethod
    def image_pyrimid(cls):
        src_img = imread("../lib/images/saber.jpg")

        G = src_img.copy()
        g_pyrimid = [G]
        for i in range(6):
            G = pyrDown(G)
            g_pyrimid.append(G)

        l_pyrimid = [g_pyrimid[5]]
        for i in xrange(5, 0, -1):
            GE = pyrUp(g_pyrimid[i])
            l_pyrimid.append(subtract(g_pyrimid[i-1], GE))

        for i, image in enumerate(g_pyrimid):
            imshow("Gaussian"+str(i), image)

        for i, image in enumerate(l_pyrimid):
            imshow("Laplacian"+str(i), image)

        # recons
        basic_img = l_pyrimid[0]
        for i in range(1, 6):
            basic_img = pyrUp(basic_img)
            basic_img = add(basic_img, l_pyrimid[i])

        imshow("Src", src_img)
        imshow("Reconsture", basic_img)


        waitKey(0)


if __name__ == "__main__":
    Example.image_pyrimid()