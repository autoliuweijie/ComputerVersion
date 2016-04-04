# coding: utf-8
from numpy import *
from cv2 import *


class Example(object):

    @classmethod
    def saveVideo(cls):
        capture = VideoCapture(0)
        codec = VideoWriter_fourcc(*'mp4v')
        w = capture.get(CAP_PROP_FRAME_WIDTH)
        h = capture.get(CAP_PROP_FRAME_HEIGHT)
        out = VideoWriter('~/Desktop/output.mp4', codec, 20.0, (int(w), int(h)))

        namedWindow("Video")
        while True:
            ret, frame = capture.read()

            if ret is True:
                imshow("Video", frame)
                out.write(frame)
                c = waitKey(33)
                if c == ord('q'):
                    break
            else:
                break

        capture.release()
        out.release()
        destroyAllWindows()


if __name__ == "__main__":
    Example.saveVideo()