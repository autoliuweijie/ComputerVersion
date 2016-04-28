import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


class Example(object):

    @classmethod
    def find_circle(cls):
        img1 = cv.imread("../lib/images/car1.jpg", 1)
        img2 = cv.imread("../lib/images/car2.jpg", 1)
        template = cv.imread('../lib/images/carcontroller.png', 1)

        img1_i = cv.cvtColor(img1, cv.COLOR_BGR2HSV)[:, :, 2]
        img2_i = cv.cvtColor(img2, cv.COLOR_BGR2HSV)[:, :, 2]
        template_i = cv.cvtColor(template, cv.COLOR_BGR2HSV)[:, :, 2]

        res = cv.matchTemplate(img1_i, template_i, cv.TM_CCOEFF)

        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

        top_left = max_loc
        bottom_right = (top_left[0] + template.shape[1], top_left[1] + template.shape[0])

        cv.rectangle(img1, top_left, bottom_right, 255, 2)

        plt.subplot(1, 2, 1), plt.imshow(res, cmap='gray')
        plt.subplot(1, 2, 2), plt.imshow(img1, cmap='gray')
        plt.show()


if __name__ == "__main__":
    Example.find_circle()