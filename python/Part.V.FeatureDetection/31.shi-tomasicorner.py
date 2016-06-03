# coding: utf-8
import cv2 as cv
import numpy as np


class Example(object):

    @classmethod
    def test_tomasi_corner(cls):
        img = cv.imread("../lib/images/blacktable.png", 1)
        img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        corners = cv.goodFeaturesToTrack(img_gray, 25, 0.1, 10)  # 25 is the numbers of corner, 0.1 is the thresh, 10 is the mingrap

        for corner in corners:
            cv.circle(img, tuple(corner[0]), 2, [0, 255, 0], 2)

        cv.imshow('img', img)
        cv.waitKey(0)
        cv.destroyAllWindows()


if __name__ == "__main__":
    Example.test_tomasi_corner()