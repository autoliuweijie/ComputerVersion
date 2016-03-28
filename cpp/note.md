Note of opencv
===

##Mat


###Mat::zeros()  Mat::ones()

        Mat mask = Mat::zero(iamge.rows, image.cols, CV_8UC1);


###Mat.setTo(Scalar& s, InputArray mask=noArray())

    为指定的区域赋值：

        Mat imageRoi = image(Rect(0,0,250,250));
        imageRoi.setTo(Scalar(255, 0, 0));

        Mat mask = Mat::zero(iamge.rows, image.cols, CV_8UC1);
        mask(Rect(0, 0, 250, 250)).setTo(255);


###Mat.copyTo(OutputArray& iamge1, InputArray mask=noArray())

    复制图像

        Mat newImage
        iamge.copyTo(newImage);


###Mat.at<Vec3b>(i,j)

    访问像素点

        int bChannel = image.at<Vec3b>(i,j)[0];
        int gChannal = image.at<Vec3b>(i,j)[1];
        int rChannal = image.at<Vec3b>(i,j)[2];


##others


###addWeighter()

    图像加权叠加

        addWeighted(image1, 0.3, iamge2, 0.7, 0.0, dstImage);