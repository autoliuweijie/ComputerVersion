# coding: utf-8
"""
    read, show, write an image.
    @author: Liu Weijie
    @date: 2016-03-28
"""
from numpy import *
from cv2 import *
from matplotlib import pyplot as plt


def showImageWithPlt(image):
    b, g, r = split(image)
    image = merge([r, g, b])
    plt.imshow(image)
    plt.show()


if __name__ == "__main__":

    image1 = imread("../lib/images/google.png")
    print image1.shape
    # namedWindow("Image")
    # imshow("Image", image1)
    # # showImageWithPlt(image1)
    # waitKey(0)
    # destroyAllWindows()