# coding: utf-8
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


class Example(object):

    @classmethod
    def match_template(cls):
        img = cv.imread('../lib/images/bigheroback.png', 0)
        template = cv.imread('../lib/images/bighero.png', 0)

        # cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
        # 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED'
        res = cv.matchTemplate(img, template, cv.TM_CCOEFF)

        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

        top_left = max_loc
        bottom_right = (top_left[0] + template.shape[1], top_left[1] + template.shape[0])

        cv.rectangle(img, top_left, bottom_right, 255, 2)

        plt.subplot(1, 2, 1), plt.imshow(res, cmap='gray')
        plt.subplot(1, 2, 2), plt.imshow(img, cmap='gray')
        plt.show()

    @classmethod
    def match_template2(cls):
        img = cv.imread('../lib/images/faces.jpg', 0)
        template = cv.imread('../lib/images/face.png', 0)
        res = cv.matchTemplate(img, template, cv.TM_CCOEFF_NORMED)
        locs = np.where(res >= 0.5)
        for loc in zip(*locs[::-1]):
            cv.rectangle(img, loc, (loc[0] + template.shape[1], loc[1] + template.shape[0]), 255, 2)

        cv.imshow("img", img)
        cv.waitKey(0)
        cv.destroyAllWindows()


if __name__ == "__main__":
    Example.match_template()
    # Example.match_template2()