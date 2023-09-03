import numpy as np
import cv2 as cv

#1.幅度谱和相位谱分离函数
def magnitude_phase_split(img):
    #np.fft.fft2()函数：计算二维的傅里叶变换
    dft=np.fft.fft2(img)
    #np.fft.fftshift()函数：将图像中的低频部分移动到图像的中心
    dft_shift=np.fft.fftshift(dft)
    #幅度谱,np.abs()函数：可以求绝对值/复数的模长
    magnitude_spectrum=np.abs(dft_shift)
    #相位谱,np.angle()函数：可以求得复数的辐角主值
    phase_spectrum=np.angle(dft_shift)
    return magnitude_spectrum,phase_spectrum

#2.幅度谱与相位谱结合函数
def magnitude_phase_combine(img_m,img_p):
    #根据数学原理来结合
    img_mandp=img_m*np.e**(1j*img_p)
    #利用np.fft.ifft2()函数实现傅里叶反变换
    img_mandp=np.uint8(np.abs(np.fft.ifft2(img_mandp)))
    img_mandp=img_mandp/np.max(img_mandp)*255
    return img_mandp

if __name__ == '__main__':
    #读取图像
    img1=cv.imread('original image1.jpg',0)
    img2=cv.imread('original image2.jpg',0)

    #分离幅度谱与相位谱
    img1_m,img1_p=magnitude_phase_split(img1)
    img2_m,img2_p=magnitude_phase_split(img2)

    #合并幅度谱与相位谱
    #original image1(红苹果)的幅度谱和original image2(青苹果)的相位谱
    img_1mAnd2p=magnitude_phase_combine(img1_m,img2_p)
    #original image1(红苹果)的相位谱和original image2(青苹果)的幅度谱
    img_1pAnd2m=magnitude_phase_combine(img2_m,img1_p)

    #输出图像
    cv.imwrite('image_1magnitude_2phase.jpg',img_1mAnd2p)
    cv.imwrite('image_1phase_2magnitude.jpg',img_1pAnd2m)
