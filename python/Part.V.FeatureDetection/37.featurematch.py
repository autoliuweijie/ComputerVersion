# coding: utf-8
import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np


class Example(object):

    @classmethod
    def test_brute_match(cls):
        target_img = cv.imread("../lib/images/kobehead2.png", 0)
        background_img = cv.imread("../lib/images/kobebryant.jpg", 0)

        sift = cv.xfeatures2d.SIFT_create()
        kp1, ds1 = sift.detectAndCompute(target_img, None)
        kp2, ds2 = sift.detectAndCompute(background_img, None)

        bf = cv.BFMatcher(normType=cv.NORM_L2, crossCheck=True)
        matches = bf.match(ds1, ds2)  # find kp1 math points from kp2

        blackbord = cv.drawMatches(target_img, kp1, background_img, kp2, matches, target_img)
        cv.imshow('test', blackbord)
        cv.waitKey(0)


if __name__ == "__main__":
    Example.test_brute_match()
