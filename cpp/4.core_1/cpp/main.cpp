//
//  Chapter4 core_1
//  @author: Liu Weijie
//
#include "opencv2/core.hpp"
#include "opencv2/highgui.hpp"
#include <iostream>

using namespace cv;
using namespace std;


class Pratice {

public:

    int num;

    static void createMat() {
        cout << "this is createMat" << endl;
        Mat image1, image2;
        image1 = imread("../../0.StaticSource/images/google.png");
        image1 = image2;
        Mat image3(image1);

        Mat image4;
        image1.copyTo(image4)
        Mat image5 = image1.clone();        

    }
};


int main(int argc, char** argv) {

    Pratice::createMat();
    return 0;
}