//
// @authoer: Liu Weijie
// @date: 2016-03-21
//
#include <iostream>
#include <vector>
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"


using namespace std;
using namespace cv;


class Example {

public:

    static void inputShowOutputImage() {

        // imput image
        Mat google = imread("../../0.StaticSource/images/google.png", 1);

        // show image
        namedWindow("Google");
        imshow("Google", google);

        // output image
        imwrite("../../0.StaticSource/images/google2.png", google);

        waitKey(0);
        destroyAllWindows();

    }

    static void sliderBar() {

        Mat image1 = imread("../../0.StaticSource/images/saber.jpg");
        Mat image2 = imread("../../0.StaticSource/images/background.jpg");
        int sliderValue = 50;
        const int maxSliderVaule = 100;

        namedWindow("Merge Window");
        Mat* imageArray[2] = {&image1, &image2};
        createTrackbar("merge rate", "Merge Window", &sliderValue, Example::MAX_SLIDER_VALUE, Example::onChange, imageArray);

        Example::onChange(sliderValue, imageArray);

        waitKey(0);
    }

protected:

    static const int MAX_SLIDER_VALUE = 100;

    static void onChange(int value, void* imageArray_in) {

        Mat** imageArray = (Mat**)imageArray_in;
        Mat* image1 = imageArray[0];
        Mat* image2 = imageArray[1];

        float alpha = ((float)value)/((float)Example::MAX_SLIDER_VALUE);
        Mat dstImage;
        addWeighted(*image1, alpha, *image2, 1.0 - alpha, 0.0, dstImage);

        imshow("Merge Window", dstImage);
    }
};


int main(int argc, char** argv) {

    // Example:: inputShowOutputImage();
    Example:: sliderBar();

    return 0;
} 