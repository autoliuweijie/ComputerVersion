"""
    @Author: Liu Weijie

    summary:
        src = cv2.imread("PATH")

"""


import numpy as np
import cv2


class ChapterOneExample:

    @classmethod
    def showImage(cls):
        src_image = cv2.imread("../../0.StaticSource/images/google.png")
        cv2.imshow("Init Image", src_image)
        cv2.waitKey(0)
        cv2.destroyWindow("Init Image")

    @classmethod
    def erodeImage(cls):
        src_image = cv2.imread("../../0.StaticSource/images/google.png")
        cv2.imshow("Init Image", src_image)

        element = np.ones((5, 5), np.uint8)
        dst_image = cv2.erode(src_image, element)
        cv2.imshow("Dst Image", dst_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    @classmethod
    def cannyEdge(cls):
        srcImage = cv2.imread("../../0.StaticSource/images/google.png")
        cv2.imshow("Init Image", srcImage)

        greyImage = cv2.cvtColor(srcImage, cv2.COLOR_BGR2GRAY)
        edge = cv2.Canny(greyImage, 0, 9, 3)
        cv2.imshow("Edge", edge)
        cv2.waitKey()
        cv2.destroyAllWindows()

    @classmethod
    def videoPlayer(cls):
        capture = cv2.VideoCapture(0)

        while True:
            num, frame = capture.read()

            grayImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            edge = cv2.Canny(grayImage, 9, 30, 3)

            cv2.imshow("Video", edge)
            c = cv2.waitKey(30)
            if c == ord("q"):
                break

        cv2.destroyAllWindows()


if __name__ == "__main__":
    # ChapterOneExample.showImage()
    # ChapterOneExample.erodeImage()
    # ChapterOneExample.cannyEdge()
    ChapterOneExample.videoPlayer()
