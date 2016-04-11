# coding: utf-8
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


class Example(object):

    @classmethod
    def test_calcHist(cls):
        img = cv.imread('../lib/images/saber.jpg', 0)
        histogram = cv.calcHist([img], [0], None, [256], [0, 256])
        print histogram

        plt.subplot(3, 1, 1), plt.imshow(img, cmap='gray')
        plt.subplot(3, 1, 2), plt.plot(histogram), plt.xlim([0, 256])
        plt.subplot(3, 1, 3), plt.hist(img.ravel(), 256, [0, 256]), plt.xlim([0, 256])
        plt.show()

    @classmethod
    def test_calcHist2(cls):
        img = cv.imread('../lib/images/saber.jpg')
        plt.subplot(2, 1, 1), plt.imshow(img[:, :, ::-1])

        colors = ['b', 'g', 'r']
        plt.subplot(2, 1, 2), plt.xlim([0, 256])
        for i, color in enumerate(colors):
            histogram = cv.calcHist([img], [i], None, [256], [0, 256])
            plt.plot(histogram, color=color)
        plt.show()

    @classmethod
    def test_equalizeHist(cls):
        img = cv.imread('../lib/images/saber.jpg', 0)
        img_equ = cv.equalizeHist(img)
        res = np.hstack((img, img_equ))
        plt.subplot(3, 1, 1), plt.imshow(res, cmap='gray')
        plt.subplot(3, 1, 2), plt.hist(img.ravel(), 256, [0, 256]), plt.xlim([0, 256]), plt.title('Origin')
        plt.subplot(3, 1, 3), plt.hist(img_equ.ravel(), 256, [0, 256]), plt.xlim([0, 256]), plt.title('Equalize')
        plt.show()

    @classmethod
    def test_CLAHE(cls):
        img = cv.imread('../lib/images/saber.jpg', 0)
        clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        img_clahe = clahe.apply(img)
        res = np.hstack((img, img_clahe))
        plt.subplot(1, 1, 1), plt.imshow(res, cmap='gray')
        plt.show()


class Example2D(object):

    @classmethod
    def draw_hv2d_histogram(cls):
        img = cv.imread('../lib/images/skyandbuilding.png')
        img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
        img_hist = cv.calcHist([img_hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
        print img_hist
        plt.subplot(1, 1, 1), plt.imshow(img_hist, cmap='gray')
        plt.show()

    @classmethod
    def hist_back_project(cls):
        backgrond_img = cv.imread("../lib/images/faces.jpg")
        face = cv.imread("../lib/images/face.png")

        face_hsv = cv.cvtColor(face, cv.COLOR_BGR2HSV)
        backgrond_hsv = cv.cvtColor(backgrond_img, cv.COLOR_BGR2HSV)

        face_hs_hist = cv.calcHist([face_hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
        cv.normalize(face_hs_hist, face_hs_hist, 0, 255, cv.NORM_MINMAX)

        # backProject
        result_img = cv.calcBackProject([backgrond_hsv], [0, 1], face_hs_hist, [0, 180, 0, 256], 1)

        kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (6, 6))
        result_img = cv.filter2D(result_img, cv.CV_8U, kernel)
        thresh, result_img = cv.threshold(result_img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

        # show result
        result_img = cv.merge([result_img, result_img, result_img])
        res = cv.bitwise_and(result_img, backgrond_img)
        plt.subplot(111), plt.imshow(res[:, :, ::-1])
        plt.show()

if __name__ == "__main__":
    # Example.test_calcHist()
    # Example.test_calcHist2()
    # Example.test_equalizeHist()
    # Example.test_CLAHE()
    # Example2D.draw_hv2d_histogram()
    Example2D.hist_back_project()