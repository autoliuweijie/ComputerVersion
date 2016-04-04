# coding: utf-8
from numpy import *
from cv2 import *


class Example(object):

    @classmethod
    def test_filter2D(cls):
        src_img = imread("../lib/images/google.png", 0)
        kernel = ones((5, 5), float32)/25.0
        dst_img = filter2D(src_img, CV_8UC3, kernel)
        imshow("Filter", dst_img)
        waitKey(0)

    @classmethod
    def test_blur(cls):
        src_img = imread("../lib/images/saber.jpg")
        # dst_img = blur(src_img, (5, 5))
        # dst_img = GaussianBlur(src_img, (5, 5), 1)
        dst_img = bilateralFilter(src_img, 5, 75, 75)
        imshow("Blur", dst_img)
        waitKey(0)

if __name__ == "__main__":
    # Example.test_filter2D()
    Example.test_blur()