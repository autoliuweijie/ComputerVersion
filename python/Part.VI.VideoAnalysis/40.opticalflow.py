# coding:utf-8
import cv2 as cv
import numpy as np


class Example(object):

    @classmethod
    def lucas_kanade_tracker(self):
        """
        基于光流法的特征点跟踪
        """
        cap = cv.VideoCapture("/Users/liuweijie/Desktop/output.mp4")

        # ShiTomasi 角点检测的参数
        feature_params = dict(
            maxCorners=100,
            qualityLevel=0.3,
            minDistance=7,
            blockSize=7
        )

        # lucas kanade 算法的参数
        # maxLevel 为使用金字塔的层数
        lk_params = dict(
            winSize=(15, 15),
            maxLevel=2,
            criteria = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03)
        )

        # Create some random colors
        color = np.random.randint(0,255,(100,3))

        # Take first frame and find corners in it
        ret, old_frame = cap.read()
        old_gray = cv.cvtColor(old_frame, cv.COLOR_BGR2GRAY)
        p0 = cv.goodFeaturesToTrack(old_gray, mask = None, **feature_params)

        # Create a mask image for drawing purposes
        mask = np.zeros_like(old_frame)

        while(1):

            ret,frame = cap.read()
            frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

            # calculate optical flow 能够获取点的新位置
            p1, st, err = cv.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)

            # Select good points
            good_new = p1[st==1]
            good_old = p0[st==1]

            # draw the tracks
            for i,(new,old) in enumerate(zip(good_new,good_old)):
                a,b = new.ravel()
                c,d = old.ravel()
                mask = cv.line(mask, (a,b),(c,d), color[i].tolist(), 2)
                frame = cv.circle(frame,(a,b),5,color[i].tolist(),-1)
            img = cv.add(frame,mask)

            cv.imshow('frame',img)
            k = cv.waitKey(30) & 0xff
            if k == 27:
                break

            # Now update the previous frame and previous points
            old_gray = frame_gray.copy()
            p0 = good_new.reshape(-1,1,2)

        cv.destroyAllWindows()
        cap.release()

    @classmethod
    def optical_flow(cls):
        """
        用光流找出动的地方
        """
        cap = cv.VideoCapture("/Users/liuweijie/Desktop/output.mp4")

        ret, frame1 = cap.read()
        prvs = cv.cvtColor(frame1, cv.COLOR_BGR2GRAY)
        hsv = np.zeros_like(frame1)
        hsv[..., 1] = 255

        while True:

            ret, frame2 = cap.read()
            next = cv.cvtColor(frame2, cv.COLOR_BGR2GRAY)

            #cv2.calcOpticalFlowFarneback(prev, next, pyr_scale, levels, winsize, iterations, poly_n,
            #poly_sigma, flags[)
            #pyr_scale – parameter, specifying the image scale (<1) to build pyramids for each image;
            #pyr_scale=0.5 means a classical pyramid, where each next layer is twice smaller than the
            #previous one.
            #poly_n – size of the pixel neighborhood used to find polynomial expansion in each pixel;
            #typically poly_n =5 or 7.
            #poly_sigma – standard deviation of the Gaussian that is used to smooth derivatives used
            #as a basis for the polynomial expansion; for poly_n=5, you can set poly_sigma=1.1, for
            #poly_n=7, a good value would be poly_sigma=1.5.
            #flag 可  0 或 1,0  算快 1 慢但准确
            flow = cv.calcOpticalFlowFarneback(prvs, next, None, 0.5, 3, 15, 3, 5, 1.2, 0)  # flow是一个与图片大小相同, 两通道分别表示u, v

            # 将光流存在HSV图中
            mag, ang = cv.cartToPolar(flow[...,0], flow[...,1])
            hsv[...,0] = ang*180/np.pi/2
            hsv[...,2] = cv.normalize(mag,None,0,255,cv.NORM_MINMAX)
            rgb = cv.cvtColor(hsv,cv.COLOR_HSV2BGR)

            cv.imshow('frame2',rgb)
            cv.waitKey(30)

            prvs = next

        cap.release()
        cv.destroyAllWindows()


if __name__ == "__main__":
    # Example.lucas_kanade_tracker()
    Example.optical_flow()