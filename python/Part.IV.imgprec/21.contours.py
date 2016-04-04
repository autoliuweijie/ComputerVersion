# coding: utf-8
from numpy import *
from cv2 import *
from matplotlib import pyplot as plt


class Example(object):

    @classmethod
    def test_contout(cls):
        hand_img = imread("../lib/images/hand.png", 1)
        hand_img_gray = cvtColor(hand_img, COLOR_BGR2GRAY)

        # find contours
        ret, hand_img_thr = threshold(hand_img_gray, 200, 255, THRESH_BINARY_INV)
        hand_img_thr, hand_contours, hierarchy = findContours(hand_img_thr, RETR_TREE, CHAIN_APPROX_NONE)

        # draw contours
        hand_img_contours = hand_img.copy()
        hand_img_contours = drawContours(hand_img_contours, hand_contours, -1, (255, 0, 0), 3)
        imshow("Con", hand_img_contours)

        # calculate image moments
        for i, contour in enumerate(hand_contours):
            M = moments(contour)
            print i, "moment:", M

        # calculate features of contour
        for i, contour in enumerate(hand_contours):
            area = contourArea(contour)   # or use M['m00'] to calculate area of contour
            length = arcLength(contour, True)
            print i, "Area:", area, "Length", length

        waitKey(0)

    @classmethod
    def contour_features(cls):
        hand_img = imread("../lib/images/hand.png", 1)
        hand_img_gray = cvtColor(hand_img, COLOR_BGR2GRAY)

        # find contours
        ret, hand_img_thr = threshold(hand_img_gray, 200, 255, THRESH_BINARY_INV)
        hand_img_thr, hand_contours, hierarchy = findContours(hand_img_thr, RETR_TREE, CHAIN_APPROX_NONE)
        contour = hand_contours[1]

        # contour appriximate
        epsilon = 0.01 * arcLength(contour, True)
        appri_contour = approxPolyDP(contour, epsilon, True)
        hand_img_contours = hand_img.copy()
        hand_img_contours = drawContours(hand_img_contours, [appri_contour], -1, (255, 0, 0), 3)
        imshow("Approx", hand_img_contours)

        # convexHull
        hull = convexHull(contour)
        hand_img_contours = hand_img.copy()
        hand_img_contours = drawContours(hand_img_contours, [hull], -1, (255, 0, 0), 3)
        imshow("Convex", hand_img_contours)

        # boundingRect
        x, y, w, h = boundingRect(contour)
        hand_img_rect = hand_img.copy()
        hand_img_rect = rectangle(hand_img_rect, (x, y), (x+w, y+h), (255, 0, 0), 2)
        imshow("boundingRect", hand_img_rect)

        # minAreaRect
        rect = minAreaRect(contour)
        box = boxPoints(rect)
        box = int0(box)
        hand_img_rect_ra = hand_img.copy()
        hand_img_rect_ra = drawContours(hand_img_rect_ra, [box], -1, (255, 0, 0), 2)
        imshow("boundingRect_ra", hand_img_rect_ra)

        # minEnclosingCircle
        (x, y), r = minEnclosingCircle(contour)
        print x, y, r
        hand_img_circle = hand_img.copy()
        hand_img_circle = circle(hand_img_circle, (int(x), int(y)), int(r), (255, 0, 0), 2)
        imshow("minEnclosingCircle", hand_img_circle)

        waitKey(0)

    @classmethod
    def contour_properties(cls):
        # get contour
        image = imread("../lib/images/hand.png", 0)
        ret, image_thre = threshold(image, 0, 255, THRESH_BINARY_INV + THRESH_OTSU)
        hand_img_thr, hand_contours, hierarchy = findContours(image_thre, RETR_TREE, CHAIN_APPROX_NONE)
        contour = hand_contours[0]

        drawContours(image, [contour], -1, 0, 2)
        imshow("Image", image)

        # high-weight rate
        x, y, w, h = boundingRect(contour)
        print "h-w rate:", float(h)/w

        # extent
        cnt_area = contourArea(contour)
        rect_area = w*h
        print "extent:", float(cnt_area) / rect_area

        # solidity
        hull = convexHull(contour)
        hull_area = contourArea(hull)
        print "solidity:", float(cnt_area) / hull_area

        # Equivalent Diameter
        equi_diameter = sqrt(4*cnt_area/pi)

        # Direction
        (x, y), (MA, ma), angle = fitEllipse(contour)
        print "direction:", angle

        # all pixel of contour-mask
        mask = zeros(image.shape[0:2], uint8)
        drawContours(mask, [contour], 0, 255, -1)
        pixel_points = transpose(array(nonzero(mask)))
        print pixel_points

        # max and min pixel location
        min_val, max_val, min_loc, max_loc = minMaxLoc(image, mask=mask)
        print "min value ", min_val, "at", min_loc, "\n", "max value ", max_val, "at", max_loc

        # pole
        leftmost = tuple(contour[contour[:, :, 0].argmin()][0])
        rightmost = tuple(contour[contour[:, :, 0].argmax()][0])
        topmost = tuple(contour[contour[:, :, 1].argmin()][0])
        bottommost = tuple(contour[contour[:, :, 1].argmax()][0])
        print leftmost, rightmost, topmost, bottommost

        waitKey(0)








if __name__ == "__main__":
    # Example.test_contout()
    Example.contour_properties()










































