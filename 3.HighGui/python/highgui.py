"""
    chapter3 highgui of opencv
    @author: Liu Weijie
    @date: 2016-03-24
"""
from cv2 import *


class Example(object):

    MAX_SLIDER_VALUE = 100
    INIT_SLIDER_VALUE = 50

    saberImage = imread("../../0.StaticSource/images/saber.jpg")
    backgroundImage = imread("../../0.StaticSource/images/background.jpg")

    @classmethod
    def inputShowOutputImage(cls):
        srcImage = imread("../../0.StaticSource/images/google.png", 1)
        namedWindow("Image")
        imshow("Image", srcImage)
        imwrite("../../0.StaticSource/images/google3.png", srcImage)
        waitKey(0)

    @classmethod
    def sliderBar(cls):

        namedWindow("Merge Image")
        createTrackbar("merge rate", "Merge Image", cls.INIT_SLIDER_VALUE, cls.MAX_SLIDER_VALUE, cls.onChange)
        cls.onChange(cls.INIT_SLIDER_VALUE)
        waitKey(0)

    @classmethod
    def onChange(cls, value):
        alpha = float(getTrackbarPos("merge rate", "Merge Image")) / cls.MAX_SLIDER_VALUE
        dstImage = addWeighted(cls.saberImage, alpha, cls.backgroundImage, 1.0 - alpha, 0.0)
        imshow("Merge Image", dstImage)

if __name__ == "__main__":
    # Example.inputShowOutputImage()
    Example.sliderBar()
