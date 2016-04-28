# coding: utf-8
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


class Example(object):

    @classmethod
    def test_surf(cls):
        # image with noise
        img = cv.imread("../lib/images/hand.png")
        img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        noise = np.uint8(10*np.random.rand(img.shape[0], img.shape[1]) - 5.0)
        img_gray = cv.add(img_gray, noise)
        img_gray = cv.GaussianBlur(img_gray, (5, 5), 10)

        surf = cv.xfeatures2d.SURF_create(400)
        kp, ds = surf.detectAndCompute(img_gray, None)
        print surf.getHessianThreshold(), len(kp)

        surf.setHessianThreshold(1000)
        kp, ds = surf.detectAndCompute(img_gray, None)
        print surf.getHessianThreshold(), len(kp)

        cv.drawKeypoints(img_gray, kp, img, flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

        cv.imshow("img", img)
        cv.waitKey(0)
        cv.destroyAllWindows()


if __name__ == "__main__":
    Example.test_surf()
