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

        # for match in matches:
        #     print "(", match.queryIdx, ",", match.trainIdx, ")", " ", match.distance, match.imgIdx

        blackbord = cv.drawMatches(target_img, kp1, background_img, kp2, matches, target_img)
        cv.imshow('test', blackbord)
        cv.waitKey(0)

    @classmethod
    def test_brute_match2(cls):

        target_img = cv.imread("../lib/images/kobehead2.png", 0)
        search_img = cv.imread("../lib/images/kobebryant.jpg", 0)

        sift = cv.xfeatures2d.SIFT_create()
        kp1, ds1 = sift.detectAndCompute(target_img, None)
        kp2, ds2 = sift.detectAndCompute(search_img, None)

        bf = cv.BFMatcher(normType=cv.NORM_L2, crossCheck=True)
        matches = bf.knnMatch(ds1, ds2, k=1)  # something wrong in osx

        # print matches

    @classmethod
    def test_flann_match(cls):

        target_img = cv.imread("../lib/images/kobehead2.png", 0)
        search_img = cv.imread("../lib/images/kobebryant.jpg", 0)

        sift = cv.xfeatures2d.SIFT_create()
        target_kp, target_des = sift.detectAndCompute(target_img, None)
        search_kp, search_des = sift.detectAndCompute(search_img, None)

        FLANN_INDEX_KDTREE = 0
        index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
        search_params = dict(checks=50)
        flann = cv.FlannBasedMatcher(index_params, search_params)

        matches = flann.knnMatch(target_des, search_des, k=1)  # something wrong in osx

        # print(matches, len(matches))




if __name__ == "__main__":
    # Example.test_brute_match()
    # Example.test_brute_match2()
    Example.test_flann_match()