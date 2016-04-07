# coding: utf-8
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


class Example(object):

    @classmethod
    def test_contout(cls):
        hand_img = cv.imread("../lib/images/hand.png", 1)
        hand_img_gray = cv.cvtColor(hand_img, cv.COLOR_BGR2GRAY)

        # find contours
        ret, hand_img_thr = cv.threshold(hand_img_gray, 200, 255, cv.THRESH_BINARY_INV)
        hand_img_thr, hand_contours, hierarchy = cv.findContours(hand_img_thr, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

        # draw contours
        hand_img_contours = hand_img.copy()
        hand_img_contours = cv.drawContours(hand_img_contours, hand_contours, -1, (255, 0, 0), 3)
        cv.imshow("Con", hand_img_contours)

        # calculate image moments
        for i, contour in enumerate(hand_contours):
            M = cv.moments(contour)
            print i, "moment:", M

        # calculate features of contour
        for i, contour in enumerate(hand_contours):
            area = cv.contourArea(contour)   # or use M['m00'] to calculate area of contour
            length = cv.arcLength(contour, True)
            print i, "Area:", area, "Length", length

        cv.waitKey(0)

    @classmethod
    def contour_features(cls):
        hand_img = cv.imread("../lib/images/hand.png", 1)
        hand_img_gray = cv.cvtColor(hand_img, COLOR_BGR2GRAY)

        # find contours
        ret, hand_img_thr = cv.threshold(hand_img_gray, 200, 255, cv.THRESH_BINARY_INV)
        hand_img_thr, hand_contours, hierarchy = cv.findContours(hand_img_thr, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
        contour = hand_contours[1]

        # contour appriximate
        epsilon = 0.01 * cv.arcLength(contour, True)
        appri_contour = cv.approxPolyDP(contour, epsilon, True)
        hand_img_contours = hand_img.copy()
        hand_img_contours = cv.drawContours(hand_img_contours, [appri_contour], -1, (255, 0, 0), 3)
        cv.imshow("Approx", hand_img_contours)

        # convexHull
        hull = cv.convexHull(contour)
        hand_img_contours = hand_img.copy()
        hand_img_contours = cv.drawContours(hand_img_contours, [hull], -1, (255, 0, 0), 3)
        cv.imshow("Convex", hand_img_contours)

        # boundingRect
        x, y, w, h = cv.boundingRect(contour)
        hand_img_rect = hand_img.copy()
        hand_img_rect = cv.rectangle(hand_img_rect, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv.imshow("boundingRect", hand_img_rect)

        # minAreaRect
        rect = cv.minAreaRect(contour)
        box = cv.boxPoints(rect)
        box = cv.int0(box)
        hand_img_rect_ra = hand_img.copy()
        hand_img_rect_ra = cv.drawContours(hand_img_rect_ra, [box], -1, (255, 0, 0), 2)
        cv.imshow("boundingRect_ra", hand_img_rect_ra)

        # minEnclosingCircle
        (x, y), r = cv.minEnclosingCircle(contour)
        print x, y, r
        hand_img_circle = hand_img.copy()
        hand_img_circle = cv.circle(hand_img_circle, (int(x), int(y)), int(r), (255, 0, 0), 2)
        cv.imshow("minEnclosingCircle", hand_img_circle)

        cv.waitKey(0)

    @classmethod
    def contour_properties(cls):
        # get contour
        image = cv.imread("../lib/images/hand.png", 0)
        ret, image_thre = cv.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv.THRESH_OTSU)
        hand_img_thr, hand_contours, hierarchy = cv.findContours(image_thre, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
        contour = hand_contours[0]

        cv.drawContours(image, [contour], -1, 0, 2)
        cv.imshow("Image", image)

        # high-weight rate
        x, y, w, h = cv.boundingRect(contour)
        print "h-w rate:", float(h)/w

        # extent
        cnt_area = cv.contourArea(contour)
        rect_area = w*h
        print "extent:", float(cnt_area) / rect_area
        # solidity
        hull = cv.convexHull(contour)
        hull_area = cv.contourArea(hull)
        print "solidity:", float(cnt_area) / hull_area

        # Equivalent Diameter
        equi_diameter = cv.sqrt(4*cnt_area/np.pi)

        # Direction
        (x, y), (MA, ma), angle = cv.fitEllipse(contour)
        print "direction:", angle

        # all pixel of contour-mask
        mask = cv.zeros(image.shape[0:2], np.uint8)
        cv.drawContours(mask, [contour], 0, 255, -1)
        pixel_points = cv.transpose(np.array(np.nonzero(mask)))
        print pixel_points

        # max and min pixel location
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(image, mask=mask)
        print "min value ", min_val, "at", min_loc, "\n", "max value ", max_val, "at", max_loc

        # pole
        leftmost = tuple(contour[contour[:, :, 0].argmin()][0])
        rightmost = tuple(contour[contour[:, :, 0].argmax()][0])
        topmost = tuple(contour[contour[:, :, 1].argmin()][0])
        bottommost = tuple(contour[contour[:, :, 1].argmax()][0])
        print leftmost, rightmost, topmost, bottommost

        cv.waitKey(0)

    @classmethod
    def find_convexity_defects(cls):
        # get contours
        hand_img = cv.imread("../lib/images/hand.png", 0)
        ret, hand_thre = cv.threshold(hand_img, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)
        hand_contours_img, hand_contours, hierarchy = cv.findContours(hand_thre, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

        # find biggest contour
        contour = max(hand_contours, key=cv.contourArea)

        hull = cv.convexHull(contour, returnPoints=False)
        defects = cv.convexityDefects(contour, hull)

        for defect in defects:
            s, e, f, d = defect[0]
            start = tuple(contour[s][0])
            end = tuple(contour[e][0])
            far = tuple(contour[f][0])
            cv.line(hand_img, start, end, 0, 2)
            cv.circle(hand_img, far, 5, 0, -1)

        cv.imshow('imag', hand_img)
        cv.waitKey(0)
        cv.destroyAllWindows()

    @classmethod
    def point_polygon_test(cls):
        # get contour
        hand_img = cv.imread("../lib/images/hand.png", 0)
        ret, hand_thre = cv.threshold(hand_img, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)
        hand_contours_img, hand_contours, hierarchy = cv.findContours(hand_thre, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
        contour = max(hand_contours, key=cv.contourArea)

        dist = cv.pointPolygonTest(contour, (50, 50), True)
        print dist

    @classmethod
    def match_shape(cls):
        stars_img = cv.imread("../lib/images/stars.png", 0)
        ret, stars_img_thre = cv.threshold(stars_img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
        contours_img, stars_contours, hierarchy = cv.findContours(stars_img_thre, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
        stars_contours = sorted(stars_contours, key=cv.contourArea, reverse=True)[0: 3]

        contours_num = len(stars_contours)
        similarity_matrix = np.zeros((contours_num, contours_num), np.float16)
        for i in range(contours_num):
            for j in range(contours_num):
                similarity_matrix[i, j] = cv.matchShapes(stars_contours[i], stars_contours[j], 1, 0.0)

        print "similarity:", similarity_matrix


if __name__ == "__main__":
    # Example.test_contout()
    # Example.contour_properties()
    # Example.find_convexity_defects()
    # Example.point_polygon_test()
    Example.match_shape()








































