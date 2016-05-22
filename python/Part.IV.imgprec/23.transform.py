# coding: utf-8
"""
    @author: Liu Weijie
"""
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


class Example(object):

    @classmethod
    def draw_spectrum_by_numpy(cls):
        img = cv.imread("../lib/images/water.png", 0)

        img_ft = np.fft.fft2(img)
        img_ft = np.fft.fftshift(img_ft)
        img_ft_magnitude = 20 * np.log(np.abs(img_ft))

        plt.subplot(111)
        plt.imshow(img_ft_magnitude, cmap='gray', vmin=0, vmax=400)
        plt.title('Frequent Spectrum'), plt.xticks([]), plt.yticks([])
        plt.colorbar()
        plt.show()

    @classmethod
    def high_pass_filter_by_numpy(cls):
        # load image
        img = cv.imread("../lib/images/happy.png", 0)

        plt.subplot(2, 2, 1)
        plt.imshow(img, cmap='gray')
        plt.title('Input Image')

        # transform
        img_ft = np.fft.fft2(img)
        img_ft = np.fft.fftshift(img_ft)
        img_ft_magnitude = 20 * np.log(np.abs(img_ft))

        plt.subplot(2, 2, 2)
        plt.imshow(img_ft_magnitude, cmap='gray', vmin=0, vmax=400)
        plt.title('Frequent spectrum')
        plt.colorbar()

        # high pass filter
        x_center = img_ft.shape[1]/2
        y_center = img_ft.shape[0]/2
        x_threshold = 40
        y_threshold = 40
        img_ft[y_center-y_threshold:y_center+y_threshold, x_center-x_threshold:x_center+x_threshold] = 1
        img_ft_magnitude = 20 * np.log(np.abs(img_ft))

        plt.subplot(2, 2, 3)
        plt.imshow(img_ft_magnitude, cmap='gray', vmin=0, vmax=400)
        plt.title('Frequent spectrum after high pass filter')
        plt.colorbar()

        # inverse transform
        img_ft = np.fft.ifftshift(img_ft)
        img_back = np.fft.ifft2(img_ft)
        img_back = np.abs(img_back)

        plt.subplot(2, 2, 4)
        plt.imshow(img_back, cmap='gray')
        plt.title('Image after filter')

        plt.show()

    @classmethod
    def low_pass_filter_by_opencv(cls):
        # load image
        img = cv.imread("../lib/images/water.png", 0)

        plt.subplot(2, 2, 1)
        plt.imshow(img, cmap='gray')
        plt.title('Input Image')

        # transform
        dft = cv.dft(np.float32(img), flags=cv.DFT_COMPLEX_OUTPUT)
        dft_shift = np.fft.fftshift(dft)
        dft_magnitude = 20 * np.log(cv.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))

        plt.subplot(2, 2, 2)
        plt.imshow(dft_magnitude, cmap='gray')
        plt.title('Frequent Spectrum')

        # make a low_pass mask
        mask = np.zeros(dft_shift.shape[0:2])
        x_center = dft_shift.shape[1] / 2
        y_center = dft_shift.shape[0] / 2
        band_with = 200
        mask[y_center - band_with : y_center + band_with, x_center - band_with : x_center + band_with] = 1

        # filter in frequent zone
        dft_shift[:, :, 0] = dft_shift[:, :, 0] * mask
        dft_shift[:, :, 1] = dft_shift[:, :, 1] * mask
        dft_magnitude = 20 * np.log(cv.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))

        plt.subplot(2, 2, 3)
        plt.imshow(dft_magnitude, cmap='gray')
        plt.title('Frequent Spectrum After LP')

        # inverse to img
        dft = np.fft.ifftshift(dft_shift)
        img_back = cv.idft(dft)
        img_back = cv.magnitude(img_back[:, :, 0], img_back[:, :, 1])

        plt.subplot(2, 2, 4)
        plt.imshow(img_back, cmap='gray')
        plt.title("Image after filter")

        plt.show()

    @classmethod
    def improve_perfermance(cls):
        img = cv.imread("../lib/images/water.png", 0)
        rows, cols = img.shape
        print rows, cols
        nrows = cv.getOptimalDFTSize(rows)
        ncols = cv.getOptimalDFTSize(cols)
        print nrows, cols

        # numpy
        fft = np.fft.fft2(img, [nrows, ncols])

        # opencv
        right = ncols - cols
        bottom = nrows - rows
        nimg = cv.copyMakeBorder(img, 0, bottom, 0, right, cv.BORDER_CONSTANT, value=0)
        fft = cv.dft(np.float32(nimg), flags=cv.DFT_COMPLEX_OUTPUT)



if __name__ == "__main__":
    # Example.draw_spectrum_by_numpy()
    # Example.high_pass_filter_by_numpy()
    Example.low_pass_filter_by_opencv()
    # Example.improve_perfermance()