//
// Created by liuweijie on 16/3/18.
// Summary:
//     Mat image = imread("PATH/IMAGE.png")
//     imshow("WindowName", image);
//     cvtColor(image1, image2, COLOR_BRG2GRAY);
//     blur(image1, image2, Size(3, 3));
//     Canny(image1, image2, 0, 30, 3);
//     VideoCapture capture("PATH/VIDEO.avi");
//     Mat frame; capture >> frame;
//


#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>


using namespace cv;


class ChapterOneExample {

public:

    static void showImage();

    static void erodeImage();

    static void cannyEdge();

    static void videoPlayer();
};


int main(int argc, char** argv) {

    // ChapterOneExample::showImage();
    // ChapterOneExample::erodeImage();
    // ChapterOneExample::cannyEdge();
    ChapterOneExample::videoPlayer();
    return 0;

}


void ChapterOneExample::showImage() {

    Mat srcImage = imread("../../0.StaticSource/images/google.png");
    imshow("Init Picture", srcImage);
    waitKey(0);

}


void ChapterOneExample::erodeImage() {

    Mat srcImage = imread("../../0.StaticSource/images/google.png");
    imshow("Init Picture", srcImage);

    Mat element = getStructuringElement(MORPH_RECT, Size(15, 15));
    Mat destImage;

    erode(srcImage, destImage, element);

    imshow("Eroded Picture", destImage);

    waitKey(0);

}


void ChapterOneExample::cannyEdge() {

    Mat srcImage = imread("../../0.StaticSource/images/google.png");
    imshow("Init Image", srcImage);

    Mat desImage;
    cvtColor(srcImage, desImage, COLOR_BGR2GRAY);

    blur(desImage, desImage, Size(3, 3));

    Canny(desImage, desImage, 3, 9, 3);

    imshow("Canny Image", desImage);

    waitKey(0);

}


void ChapterOneExample::videoPlayer() {

    // VideoCapture capture("../img_lib/water.avi");  // 0 means get video from camera
    VideoCapture capture;
    capture.open(0); // 0 means get video from camera

    Mat frame, edge;
    char inKey;
    while(1) {

        capture >> frame;

        cvtColor(frame, edge, COLOR_BGR2GRAY);
        Canny(edge, edge, 0, 30, 3);

        inKey = (char)waitKey(30);
        if(inKey == 'q' || frame.empty()) {
            break;
        }

        imshow("Video", frame);
        imshow("Edge", edge);
    }
}