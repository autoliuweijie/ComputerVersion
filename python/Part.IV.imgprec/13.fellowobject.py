# coding: utf-8
from numpy import *
from cv2 import *


class Example(object):

    @classmethod
    def fellow_object(cls):
        capture = VideoCapture(0)
        namedWindow("Src")
        namedWindow("Mask")
        namedWindow("Dst")

        low_thresh = array([110, 50, 50])
        up_thresh = array([140, 255, 255])
        while True:
            ret, frame = capture.read()

            if ret is True:
                hsv = cvtColor(frame, COLOR_BGR2HSV)
                mask = inRange(hsv, low_thresh, up_thresh)
                dst = bitwise_and(frame, frame, mask=mask)

                imshow("Src", frame)
                imshow("Mask", mask)
                imshow("Dst", dst)

                c = waitKey(33)
                if c == ord('q'):
                    break

            else:
                break

if __name__ == "__main__":
    Example.fellow_object()