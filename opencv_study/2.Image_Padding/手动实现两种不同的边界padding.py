import cv2 as cv
import numpy as np
'''
在滤波操作中，为了对图像边缘滤波器处理不到的像素进行滤波，故需要对图像进行padding操作。
下面实现了两种图像padding的操作，分别是zero padding和copy edge padding。
'''
#[1]zero padding(0填充)
def zero_padding(img,K_size):
    #1.获取图像的shape
    if len(img.shape)==3:
        (H,W,C)=img.shape
    else:
        img=np.expand_dims(img,axis=-1)
        (H,W,C)=img.shape
    #2.padding
    pad=K_size//2
    out=np.zeros((H+pad*2,W+pad*2,C),dtype=np.float64)
    out[pad:pad+H,pad:pad+W]=img.copy().astype(np.float64)
    out=out.astype(np.uint8)
    return out

#[2]copy edge padding(边缘复制填充)
def copy_edge_padding(img,K_size):
    #1.获取图像的shape
    if len(img.shape)==3:
        (H,W,C)=img.shape
    else:
        img=np.expand_dims(img,axis=-1)
        (H,W,C)=img.shape
    #2.padding
    pad=K_size//2
    out=np.zeros((H+pad*2,W+pad*2,C),dtype=np.float64)
    out[pad:pad+H,pad:pad+W]=img.copy().astype(np.float64)
    #上下左右四条边往外拓展
    for i in range(pad):
        out[pad-1-i,pad:pad+W]=out[pad,pad:pad+W]
        out[pad+H+i,pad:pad+W]=out[pad+H-1,pad:pad+W]
        out[pad:pad+H,pad-i-1]=out[pad:pad+H,pad]
        out[pad:pad+H,pad+W+i]=out[pad:pad+H,pad+W-1]
    #四个角复制图像最左上角，最右上角，最左下角，最右下角的四个像素点
    for i in range(pad):
        for j in range(pad):
            out[i][j]=out[pad][pad]
            out[pad+H+i][pad+W+j]=out[pad+H-1][pad+W-1]
            out[i][pad+W+j]=out[pad][pad+W-1]
            out[pad+H+i][j]=out[pad+H-1][pad]
    out=out.astype(np.uint8)
    return out

if __name__ == '__main__':
    #读取图像并进行padding
    image=cv.imread('2.Image_Padding/original image.jpg')
    KK_size=int(input('请输入你所使用的滤波器边长：'))
    out1=zero_padding(image,KK_size)
    out2=copy_edge_padding(image,KK_size)
    cv.imwrite('2.Image_Padding/zero padding image.jpg',out1)
    cv.imwrite('2.Image_Padding/copy edge padding image.jpg',out2)