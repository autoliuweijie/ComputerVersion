import cv2 as cv
import numpy as np


class Example(object):

    @classmethod
    def test_BackgroundSubtractorMOG(cls):

        cap = cv.VideoCapture(0)

        fgbg = cv.createBackgroundSubtractorMOG2()  # there is a bug

        while True:

            ret, frame = cap.read()

            fgmask = fgbg.apply(frame)

            cv.imshow('frame', fgmask)
            k = cv.waitKey(30) & 0xff
            if k == 27:
                break

        cap.release()
        cv.destroyAllWindows()

    @classmethod
    def test_BackgroundSubtractorKNN(cls):

        cap = cv.VideoCapture(0)

        kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE,(3,3))
        fgbg = cv.createBackgroundSubtractorKNN()

        while True:
            ret, frame = cap.read()
            fgmask = fgbg.apply(frame)
            fgmask = cv.morphologyEx(fgmask, cv.MORPH_OPEN, kernel)
            cv.imshow('frame', fgmask)
            k = cv.waitKey(30) & 0xff
            if k == 27:
                break

        cap.release()
        cv.destroyAllWindows()


if __name__ == "__main__":

    # Example.test_BackgroundSubtractorMOG()
    Example.test_BackgroundSubtractorKNN()