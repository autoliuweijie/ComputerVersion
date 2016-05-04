# coding: utf-8
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


class Example(object):

    @classmethod
    def test_brief_description(cls):

        img = cv.imread("../lib/images/saber.jpg", 1)
        img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        star = cv.xfeatures2d.StarDetector_create()
        brief = cv.xfeatures2d.BriefDescriptorExtractor_create()

        kp = star.detect(img_gray, None)
        ds = brief.compute(img_gray, kp)

        print len(kp), len(ds[0]), ds[1]


if __name__ == "__main__":
    Example.test_brief_description()