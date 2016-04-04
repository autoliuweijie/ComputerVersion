# coding: utf-8
from numpy import *
from cv2 import *
from matplotlib import pyplot as plt


class Example(object):

    @classmethod
    def resize(cls):
        img = imread("../lib/images/google.png")
        rows, cols = img.shape[0:2]
        dst_img = resize(img, (2*cols, 2*rows), interpolation=INTER_LINEAR)
        imshow("dst", dst_img)
        waitKey(0)

    @classmethod
    def move(cls):
        img = imread("../lib/images/google.png")
        rows, cols = img.shape[0:2]
        mov_mat = array([[1.0, 0.0, 50.0], [0.0, 1.0, 50.0]])
        dst_img = warpAffine(img, mov_mat, (cols, rows))
        imshow("dst", dst_img)
        waitKey(0)

    @classmethod
    def rotate(cls):
        img = imread("../lib/images/google.png")
        rows, cols = img.shape[0:2]
        rotate_mat = getRotationMatrix2D((50, 50), 45, 1)
        dst_img = warpAffine(img, rotate_mat, (cols, rows))
        imshow("dst", dst_img)
        waitKey(0)

    @classmethod
    def any_affine_trans(cls):
        srcimg = imread("../lib/images/google.png")

        pts1 = array([[50.0, 50.0], [200.0, 50.0], [50.0, 200.0]], float32)  # must float32
        pts2 = array([[10.0, 100.0], [200.0, 50.0], [100.0, 250.0]], float32)

        M = getAffineTransform(pts1, pts2)

        dstimg = warpAffine(srcimg, M, (srcimg.shape[1], srcimg.shape[0]))

        plt.subplot(121)
        plt.imshow(srcimg)
        plt.subplot(122)
        plt.imshow(dstimg)
        plt.show()

    @classmethod
    def perspective_trans(cls):
        srcimg = imread("../lib/images/google.png")

        pts1 = array([[56,65],[368,52],[28,387],[389,390]], float32)  # must float32
        pts2 = array([[0,0],[300,0],[0,300],[300,300]], float32)

        M = getPerspectiveTransform(pts1, pts2)

        dstimg = warpPerspective(srcimg, M, (srcimg.shape[1], srcimg.shape[0]))

        plt.subplot(121)
        plt.imshow(srcimg)
        plt.subplot(122)
        plt.imshow(dstimg)
        plt.show()

if __name__ == "__main__":
    # Example.resize()
    # Example.move()
    # Example.any_affine_trans()
    Example.perspective_trans()