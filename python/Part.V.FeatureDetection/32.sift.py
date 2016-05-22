# coding: utf-8
import cv2 as cv
import numpy as np


class Example(object):

    @classmethod
    def test_sift_keypoints(cls):
        img = cv.imread("../lib/images/hand.png")
        img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        sift = cv.xfeatures2d.SIFT_create()
        # keypoints, descriptions = sift.detectAndCompute(img_gray, None)
        keypoints = sift.detect(img_gray, None)
        descriptions = sift.compute(img_gray, keypoints)

        img_sift = np.zeros(img.shape, np.uint8)
        cv.drawKeypoints(img_gray, keypoints, img_sift, flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)  # img mast be a colorful image
        print "description:", descriptions

        cv.imshow("img", img_sift)
        cv.waitKey(0)
        cv.destroyAllWindows()





if __name__ == "__main__":
    Example.test_sift_keypoints()