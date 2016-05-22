# coding: utf-8
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


class Example(object):

    @classmethod
    def line_detect_by_houghlines(cls):
        hand_img = cv.imread('../lib/images/blacktable.png', 1)
        hand_gray = cv.cvtColor(hand_img, cv.COLOR_BGR2GRAY)
        hand_edges = cv.Canny(hand_gray, 50, 150, apertureSize=3)

        lines = cv.HoughLines(hand_edges, 1, np.pi/280, 200)
        print lines
        for line in lines:
            rho, theta = line[0]
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*rho
            y0 = b*rho
            x1 = int(x0 + 500*(-b))
            y1 = int(y0 + 500*(a))
            x2 = int(x0 - 500*(-b))
            y2 = int(y0 - 500*(a))

            cv.line(hand_img, (x1, y1), (x2, y2), (0, 0, 255), 2)

        cv.imshow("hand_img", hand_img)
        cv.waitKey(0)
        cv.destroyAllWindows()

    @classmethod
    def line_detect_by_houghlinesp(cls):
        hand_img = cv.imread('../lib/images/blacktable.png', 1)
        hand_gray = cv.cvtColor(hand_img, cv.COLOR_BGR2GRAY)
        hand_edges = cv.Canny(hand_gray, 50, 150, apertureSize=3)

        lines = cv.HoughLinesP(hand_edges, 1, np.pi/180, 100, 0, 10)
        for line in lines:
            x0, y0, x1, y1 = line[0]
            cv.line(hand_img, (x0, y0), (x1, y1), (0, 0, 255), 2)

        cv.imshow("hand_img", hand_img)
        cv.waitKey(0)
        cv.destroyAllWindows()



if __name__ == "__main__":
    # Example.line_detect_by_houghlines()
    Example.line_detect_by_houghlinesp()