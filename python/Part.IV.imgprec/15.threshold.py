# coding: utf-8
from numpy import *
from cv2 import *
from matplotlib import pyplot as plt


class Example(object):

    @classmethod
    def test_threshold(cls):
        src_img = imread("../lib/images/google.png", 0)

        thresh1, thresh1_img = threshold(src_img, 170, 255, THRESH_BINARY)
        thresh2, thresh2_img = threshold(src_img, 170, 255, THRESH_BINARY_INV)
        thresh3, thresh3_img = threshold(src_img, 0, 255, THRESH_BINARY + THRESH_OTSU)

        print thresh1, thresh2, thresh3

        imshow("Src", src_img)
        imshow("THRESH_BINARY", thresh1_img)
        imshow("THRESH_BINARY_INV", thresh2_img)
        imshow("OTSU", thresh3_img)
        waitKey(0)

    @classmethod
    def local_adaptive_threshold(cls):
        src_img = imread("../lib/images/google.png", 0)
        thresh_img = adaptiveThreshold(src_img, 255, ADAPTIVE_THRESH_GAUSSIAN_C, THRESH_BINARY, 11, 2)
        imshow("Adaptive threshold", thresh_img)
        waitKey(0)


if __name__ == "__main__":
    Example.test_threshold()