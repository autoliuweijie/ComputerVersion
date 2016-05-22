# coding:utf-8
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


class Example(object):

    @classmethod
    def test_watershed(cls):
        img = cv.imread('../lib/images/coins.png', 1)

        # 以下是为分割创建初始标签

        gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        thresh, bin_img = cv.threshold(gray_img, 0, 255, cv.THRESH_BINARY_INV+cv.THRESH_OTSU)

        SE = cv.getStructuringElement(cv.MORPH_CROSS, (5, 5))
        sure_bg = cv.morphologyEx(bin_img, cv.MORPH_DILATE, SE)
        sure_bg = cv.bitwise_not(sure_bg)  # 确定是背景的区域

        distance_img = cv.distanceTransform(bin_img, cv.DIST_L2, 5)  # 距离变换, 灰度值表示距离最近灰度值为0点的距离
        thresh, sure_fg = cv.threshold(distance_img, 0.7*distance_img.max(), 255, cv.THRESH_BINARY)  # 确实是前景的区域
        sure_fg = np.uint8(sure_fg)

        unknown_era = cv.subtract(bin_img, sure_fg)  # 不确定区域

        ret, marks_img = cv.connectedComponents(sure_fg)  # 分配标签
        marks_img += 2  # 各个确定区域从2开始标号
        marks_img[sure_bg == 255] = 1  # 背景区域标记为1
        marks_img[unknown_era == 255] = 0  # 不确定的区域标记为0

        # 开始分割

        new_marks_img = cv.watershed(img, marks_img)  # 得到分割后的新标记图片, 边界的用-1表示
        img[new_marks_img == -1] = [0, 0, 255]

        plt.subplot(1, 1, 1), plt.imshow(img[:, :, ::-1]), plt.colorbar()
        plt.show()


if __name__ == "__main__":
    Example.test_watershed()