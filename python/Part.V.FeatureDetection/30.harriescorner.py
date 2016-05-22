# coding: utf-8
import cv2 as cv
import numpy as np


class Example(object):

    @classmethod
    def test_cornerharries(cls):
        img = cv.imread("../lib/images/blacktable.png", 1)

        img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        img_gray = np.float32(img_gray)
        dst = cv.cornerHarris(img_gray, 3, 5, 0.05)

        img[dst >= 0.1*dst.max()] = [0, 0, 255]

        cv.imshow('img', img)
        cv.waitKey(0)
        cv.destroyAllWindows()

    @classmethod
    def test_corner_subpix(cls):
        img = cv.imread("../lib/images/blacktable.png", 1)
        img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        # 找到角点团
        img_gray = np.float32(img_gray)
        corners_img = cv.cornerHarris(img_gray, 3, 5, 0.05)
        thresh, corners_thresh = cv.threshold(corners_img, 0.1*corners_img.max(), 255, 0)

        # 找到角点团的中心
        ret, labels, stats, centers = cv.connectedComponentsWithStats(np.uint8(corners_thresh))

        # 在角点团的中心附件进行精确的寻找
        criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 100, 0.001)
        corners = cv.cornerSubPix(img_gray, np.float32(centers), (5, 5), (-1, -1), criteria)

        print corners

        res = np.hstack((corners, centers))

        res = np.int0(res)
        img[res[:,1],res[:,0]] = [0,0,255]
        img[res[:,3],res[:,2]] = [0,255,0]

        cv.imshow("img_thresh", img)
        cv.waitKey(0)
        cv.destroyAllWindows()


if __name__ == "__main__":
    # Example.test_cornerharries()
    Example.test_corner_subpix()