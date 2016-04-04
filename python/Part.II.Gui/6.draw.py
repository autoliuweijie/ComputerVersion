# coding: utf-8
from numpy import *
from cv2 import *


class Example(object):

    @classmethod
    def drawLine(cls):
        image = zeros((512, 512, 3), uint8)
        line(image, (0,0), (511, 511), (255, 0, 0), 5)
        circle(image,(447,63), 63, (0,0,255), -1)
        imshow("Image", image)
        waitKey(0)
        print image.dtype


if __name__ == "__main__":
    Example.drawLine()
