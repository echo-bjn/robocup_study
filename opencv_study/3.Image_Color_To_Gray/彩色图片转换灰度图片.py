#将彩色图片转换成灰度图片
import cv2 as cv
import numpy as np

#1.读取彩色图片
img=cv.imread('3.Image_Color_To_Gray/color_image.jpg')

#2.将彩色图片降维
H,W,C=img.shape
img_gray=np.zeros((H,W))

#3.平均法，将同一个像素位置的3个通道RGB值进行平均
for h in range(H):
    for w in range(W):
        img_gray[h][w]=1/3*img[h][w][0]+1/3*img[h][w][1]+1/3*img[h][w][2]
        
#4.输出灰度图片
cv.imwrite('3.Image_Color_To_Gray/gray_image.jpg',img_gray)