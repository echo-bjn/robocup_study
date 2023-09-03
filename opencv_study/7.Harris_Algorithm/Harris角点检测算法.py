import cv2 as cv
import numpy as np

#Harris角点检测算法可以进行图像中角点的识别
def Harris_Algorithm(img):
    #1.转换float32的灰度图像    
    #cv.cvtColor()可以实现色彩空间转换，cv.COLOR_RGB2GRAY参数可以将图像转换为灰度空间
    gray=cv.cvtColor(img,cv.COLOR_RGB2GRAY)
    gray=np.float32(gray)
    
    #2.进行Harris角点检测  
    '''
    cv.cornerHarris()参数：
    [1]img-数据类型为float32的输入图像
    [2]blockSize-角点检测要考虑的领域大小
    [3]ksize-Sobel求导中使用的窗口大小
    [4]k-角点检测方程中的自由参数，取值参数为[0.04,0.06]
    '''
    dst=cv.cornerHarris(gray,blockSize=10,ksize=3,k=0.04)
    
    #3.增大角点  
    #cv.dilate()可以实现图像膨胀，在这里使得角点更大
    dst=cv.dilate(dst,None)
    
    #4.将角点标记为红色  
    #一般与最大值相比，最大值为角点，若大于此值，则认为该点是角点，标记角点为红色
    img[dst>0.01*dst.max()]=[0,0,255]
    return img

if __name__ == '__main__':
    #读取图像
    img=cv.imread('original image.jpg')
    #Harris角点检测
    outimg=Harris_Algorithm(img)
    #输出图像
    cv.imwrite('Harris out image.jpg',outimg)
