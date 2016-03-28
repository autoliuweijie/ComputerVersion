//
// Chapter 5
// @author: Liu weijie
//


#include "opencv2/highgui/highgui.hpp"
#include "opencv2/core/core.hpp"
#include <iostream>


using namespace std;
using namespace cv;


class Example {

public:

    static void mergeImage();
};


int main(int argc, char** argv) {

    Example::mergeImage();

    Mat bgImage = imread("../../0.StaticSource/images/saber.jpg", 1);
    Mat googleLogo = imread("../../0.StaticSource/images/googlelogo.png", 1);

    Mat mask = Mat::zeros(bgImage.size(), CV_8UC(1));
    mask(Rect(250, 250, googleLogo.cols, googleLogo.rows)).setTo(255);

    // Mat newImage;
    // bgImage.copyTo(newImage, mask);

    // Mat bgImageRoi = bgImage(Rect(250, 250, googleLogo.cols, googleLogo.rows));
    // bgImageRoi.setTo(Scalar(255,0,0));

    // for(int i=0; i<bgImageRoi.rows; ++i) {
    //     for(int j=0; j<bgImageRoi.cols; ++j) {

    //         int bChannel = googleLoge.at<Vec3b>(i,j)[0];
    //         int gChannal = googleLoge.at<Vec3b>(i,j)[1];
    //         int rChannal = googleLoge.at<Vec3b>(i,j)[2];
    //         if(!(bChannel == 0 && gChannal ==  0 && rChannal == 0)) {
    //             bgImageRoi.at<Vec3b>(i,j) = googleLoge.at<Vec3b>(i,j);
    //         }
    //     }
    // }

    // addWeighted(bgImageRoi, 0.5, googleLoge, 0.5, 0.0, bgImageRoi);

    imshow("test", mask);
    waitKey(0); 
}


void Example::mergeImage() {

    cout << "this is mergeImage" << endl;
}
