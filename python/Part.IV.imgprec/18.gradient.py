# coding: utf-8
from numpy import *
from cv2 import *
from matplotlib import pyplot as plt


class Example(object):

    @classmethod
    def test_sobel(cls):
        src_img = imread("../lib/images/whiteblock.png", 0)
        random_m = uint8(100.0*random.rand(src_img.shape[0], src_img.shape[1]))

        src_img = add(src_img, random_m)
        imshow("Src", src_img)

        # src_img = GaussianBlur(src_img, (5, 5), 100)
        # imshow("Src2", src_img)

        dst_img_inx = Sobel(src_img, CV_32F, 1, 0, ksize=5)
        dst_img_iny = Sobel(src_img, CV_32F, 0, 1, ksize=5)
        dst_img_lap = Laplacian(src_img, CV_32F)

        dst_img_inx = convertScaleAbs(dst_img_inx, alpha=(1.0/1.0))
        dst_img_iny = convertScaleAbs(dst_img_iny, alpha=(1.0/1.0))
        dst_img_lap = convertScaleAbs(dst_img_lap, alpha=(1.0/1.0))


        imshow("Dst_x", dst_img_inx)
        imshow("Dst_y", dst_img_iny)
        imshow("Laplacian", dst_img_lap)
        waitKey(0)




if __name__ == "__main__":
    Example.test_sobel()
    # a = array([[300.0]], float32)
    # b = uint8(a)
    # print b