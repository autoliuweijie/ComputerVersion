# coding: utf-8
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


class Example(object):

    @classmethod
    def test_meanshift(cls):
        """
            这是一个用SIFT特征找到目标, 然后用backhist + meanshift来跟踪的例子.
            这个组合并不好, 因为SIFT依靠的是类似角点的特征而找到的目标, 用backhist是靠颜色, 难以找到
        """

        cap = cv.VideoCapture("/Users/liuweijie/Desktop/output.mp4")

        target = cv.imread("../lib/images/book.png", 1)
        target_hsv = cv.cvtColor(target, cv.COLOR_BGR2HSV)
        target_hist = cv.calcHist([target], [0, 1], None, [180, 256], [0, 180, 0, 256])
        cv.normalize(target_hist, target_hist, 0, 255, cv.NORM_MINMAX)

        # find init tracker_window by sift
        h, w = target_hsv.shape[0:2]
        sift = cv.xfeatures2d.SIFT_create()
        bf = cv.BFMatcher(normType=cv.NORM_L2, crossCheck=True)
        kp1, ds1 = sift.detectAndCompute(target, None)
        while True:

            ret, frame = cap.read()
            kp2, ds2 = sift.detectAndCompute(frame, None)

            matches = bf.match(ds1, ds2)

            src_pts = np.float32([kp1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
            dst_pts = np.float32([kp2[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)
            M, mask = cv.findHomography(src_pts, dst_pts, cv.RANSAC, 5.0)

            find_level = float(len(mask[mask==1]))/len(mask)
            if find_level >= 0.2:
                pts = np.float32([[0, 0], [0, h-1], [w-1, h-1], [w-1, 0]]).reshape(-1, 1, 2)
                dst = cv.perspectiveTransform(pts, M)
                h = int(dst[2, 0, 1]) - int(dst[0, 0, 1])
                w = int(dst[2, 0, 0]) - int(dst[0, 0, 0])
                tracker_window = (int(dst[0, 0, 0]), int(dst[0, 0, 1]), w, h)
                break

        # tracking
        term_crit = ( cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1)
        is_true, frame = cap.read()
        while is_true:

            frame_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
            histback_res = cv.calcBackProject([frame_hsv], [0, 1], target_hist, [0, 180, 0, 256], 1)

            ret, tracker_window = cv.meanShift(histback_res, tracker_window, term_crit)

            x, y, w, h = tracker_window
            cv.rectangle(frame, (x, y), (x+w, y+h), 255, 2)

            cv.imshow("frame", frame)
            k = cv.waitKey(30) & 0xff
            if k == 113:
                break

            is_true, frame = cap.read()

    @classmethod
    def test_camshift(cls):

        cap = cv.VideoCapture("/Users/liuweijie/Desktop/output.mp4")
        target = cv.imread("../lib/images/book.png", 1)

        # find init tracker_window
        tracker_window = (630, 300, 400, 550)  # top-left, w and h

        # tracking
        term_crit = ( cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1)
        target_hsv = cv.cvtColor(target, cv.COLOR_BGR2HSV)
        target_hist = cv.calcHist([target_hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
        while True:

            ret, frame = cap.read()
            frame_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
            histback = cv.calcBackProject([frame_hsv], [0, 1], target_hist, [0, 180, 0, 256], 1)

            ret, tracker_window = cv.CamShift(histback, tracker_window, term_crit)

            pts = cv.boxPoints(ret)
            pts = np.int0(pts)
            cv.polylines(frame, [pts], True, 255, 2)

            cv.imshow("img", frame)
            k = cv.waitKey(30) & 0xff
            if k == 113:
                break


if __name__ == "__main__":
    # Example.test_meanshift()
    Example.test_camshift()