# coding: utf-8
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


class Example(object):

    @classmethod
    def line_detect_by_houghcircles(cls):
        cicle_img = cv.imread("../lib/images/cicle.png", 1)
        cicle_gray = cv.cvtColor(cicle_img, cv.COLOR_BGR2GRAY)
        cicle_edges = cv.Canny(cicle_gray, 50, 150, apertureSize=3)

        circles = cv.HoughCircles(cicle_edges, cv.HOUGH_GRADIENT, 1, 20, param1=50, param2=30)
        for circle in circles[0]:
            center = (circle[0], circle[1])
            radius = circle[2]
            cv.circle(cicle_img, center, radius, (0, 255, 0), 2)

        cv.imshow("cicle_img", cicle_img)
        cv.waitKey(0)
        cv.destroyAllWindows()


if __name__ == "__main__":
    Example.line_detect_by_houghcircles()
