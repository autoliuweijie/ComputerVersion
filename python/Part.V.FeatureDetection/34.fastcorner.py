# coding: utf-8
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


class Example(object):

    @classmethod
    def fast_corner(cls):
        img = cv.imread("../lib/images/google.png", 1)
        img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        fast = cv.FastFeatureDetector_create(threshold=10, nonmaxSuppression=True)
        kp = fast.detect(img_gray, None)
        print len(kp), fast.getType(), fast.getThreshold()
        cv.drawKeypoints(img, kp, img, flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

        plt.subplot(1, 1, 1), plt.imshow(img[:, :, ::-1])
        plt.show()


if __name__ == "__main__":
    Example.fast_corner()