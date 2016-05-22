import cv2 as cv
import numpy as np


class Example(object):

    @classmethod
    def test_findHomography(cls):

        target_img = cv.imread("../lib/images/kobehead2.png", 0)
        search_img = cv.imread("../lib/images/kobebryant.jpg", 0)

        # get sift features
        sift = cv.xfeatures2d.SIFT_create()
        kp1, ds1 = sift.detectAndCompute(target_img, None)
        kp2, ds2 = sift.detectAndCompute(search_img, None)

        # match features
        bf = cv.BFMatcher(normType=cv.NORM_L2, crossCheck=True)
        matches = bf.match(ds1, ds2)  # find kp1 math points from kp2

        # find homography
        src_pts = np.float32([kp1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
        dst_pts = np.float32([kp2[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)
        M, mask = cv.findHomography(src_pts, dst_pts, cv.RANSAC, 5.0)

        # draw the matches
        h,w = target_img.shape
        pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
        dst = cv.perspectiveTransform(pts, M)
        cv.polylines(search_img, [np.int32(dst)], True, 255, 10, cv.LINE_AA)

        # draw img
        matchesMask = mask.ravel().tolist()
        draw_params = dict(
            matchColor = (0,255,0), # draw matches in green color singlePointColor = None,
            matchesMask = matchesMask, # draw only inliers
            flags = 2
        )
        img3 = cv.drawMatches(target_img, kp1, search_img, kp2, matches, None, **draw_params)

        cv.imshow('img', img3)
        cv.waitKey(0)


if __name__ == "__main__":
    Example.test_findHomography()