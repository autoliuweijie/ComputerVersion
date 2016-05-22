# coding: utf-8
from numpy import *
from cv2 import *
from matplotlib import pyplot as plt


class Example(object):

    @classmethod
    def test_canny(cls):
        src_img = imread("../lib/images/whiteblock.pngq", 0)
        edge_img = Canny(src_img, 100, 200)
        imshow("Edge", edge_img)
        waitKey(0)


if __name__ == "__main__":
    Example.test_canny()