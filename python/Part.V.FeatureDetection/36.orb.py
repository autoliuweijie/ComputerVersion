# coding: utf-8
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


class Example(object):

    @classmethod
    def test_orb(cls):

        img = cv.imread("../lib/images/face.png", 1)
        img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        # in opencv2.4, and there is something wrong in opencv3.1.0
        orb = cv.ORB()  # cv.ORB_create() in opencv 3.1.0
        kp = orb.detect(img, None)
        kp, des = orb.compute(img_gray, kp)

        cv.drawKeypoints(img, kp, img, color=(0, 255, 0),  flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

        cv.imshow("img", img)
        cv.waitKey(0)


if __name__ == "__main__":
    Example.test_orb()