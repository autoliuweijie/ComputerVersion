# coding: utf-8
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


class Example(object):

    @classmethod
    def test_erode_dilate(self):

        img = cv.imread("../lib/images/google.png", 0)
        cv.bitwise_not(img, img)

        # kernel = np.ones((5, 5), np.uint8)
        kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
        erode_img = cv.morphologyEx(img, cv.MORPH_ERODE, kernel, iterations=1)  # 腐蚀
        dilate_img = cv.morphologyEx(img, cv.MORPH_DILATE, kernel, iterations=1)  # 膨胀

        plt.subplot(3, 1, 1), plt.imshow(img, cmap='gray'), plt.title("Src Img")
        plt.subplot(3, 1, 2), plt.imshow(erode_img, cmap='gray'), plt.title("Erode Img")
        plt.subplot(3, 1, 3), plt.imshow(dilate_img, cmap='gray'), plt.title("Dilate Img")
        plt.show()

    @classmethod
    def test_open_close(self):

        img = cv.imread("../lib/images/google.png", 0)
        cv.bitwise_not(img, img)

        kernel = cv.getStructuringElement(cv.MORPH_CROSS, (5, 5))
        open_img = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)  # 开运算
        close_img = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)  # 闭运算

        plt.subplot(3, 1, 1), plt.imshow(img, cmap='gray'), plt.title("Src Img")
        plt.subplot(3, 1, 2), plt.imshow(open_img, cmap='gray'), plt.title("Open Img")
        plt.subplot(3, 1, 3), plt.imshow(close_img, cmap='gray'), plt.title("Close Img")
        plt.show()

    @classmethod
    def test_gradient_tophat_bottomhat(cls):

        img = cv.imread("../lib/images/google.png", 0)
        cv.bitwise_not(img, img)

        kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
        gradient_img = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)  # 形态学梯度
        tophat_img = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)  # 顶帽运算
        bottomhat_img = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)  # 底帽运算

        plt.subplot(4, 1, 1), plt.imshow(img, cmap='gray'), plt.title("Src Img")
        plt.subplot(4, 1, 2), plt.imshow(gradient_img, cmap='gray'), plt.title("Gradient Img")
        plt.subplot(4, 1, 3), plt.imshow(tophat_img, cmap='gray'), plt.title("Tophat Img")
        plt.subplot(4, 1, 4), plt.imshow(bottomhat_img, cmap='gray'), plt.title("Bottomhat Img")
        plt.show()


if __name__ == "__main__":

    Example.test_erode_dilate()
    # Example.test_open_close()
    # Example.test_gradient_tophat_bottomhat()