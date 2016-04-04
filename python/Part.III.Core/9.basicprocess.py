# coding: utf-8
from numpy import *
from cv2 import *


class Example(object):

    @classmethod
    def logicCalc(cls):
        img1 = imread("../lib/images/saber.jpg")
        img2 = imread("../lib/images/google.png")

        w = 250
        p = 250
        roi = img1[w:img2.shape[0]+w, p:img2.shape[1]+p]

        img2gray = cvtColor(img2, COLOR_BGR2GRAY)
        ret, mask = threshold(img2gray, 200, 255, THRESH_BINARY)
        mask_inv = bitwise_not(mask)

        img1_bg = bitwise_and(roi, roi, mask=mask_inv)
        imshow("src", img1_bg)
        imshow("Image", mask_inv)
        waitKey(0)

if __name__ == "__main__":
    Example.logicCalc()