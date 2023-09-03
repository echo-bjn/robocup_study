import cv2 as cv
import numpy as np

#手动实现高斯滤波核(所要处理的图像:img,高斯滤波核大小:K_size*K_size 和 标准差:sigma)
def gaussian_filter(img,K_size,sigma):
    #1.获取图像的shape(确保为三维)
    #(H,W,C)其中H和W表示高度方向和宽度方向的像素点个数，C代表颜色通道数
    #image.shape返回的是图像的(H,W,C)，一个元组
    #元组的len表示元组内元素的个数
    if len(img.shape)==3:
        (H,W,C)=img.shape
    #如果不是彩色图像，即灰度图像，有可能len(img.shape)=2,则需要元组维度扩展
    #np.expand_dims(img,axis=i)表示在i位置添加数据,i=-1表示img.shape最后加上一个数1,即将元组扩展维度
    else:
        img=np.expand_dims(img,axis=-1)
        (H,W,C)=img.shape
    
    #2.进行原图像的zero padding(由于需要将图像的边缘也进行高斯滤波,所以将图像边缘加上一圈宽度为pad的像素点,因此需要在图像的边缘补0)
    pad=K_size//2
    #np.zeros((2,5),dtype=np.int) 两行五列的整型矩阵
    out=np.zeros((H+pad*2,W+pad*2,C),dtype=np.float64)
    #利用python的切片操作
    out[pad:pad+H,pad:pad+W]=img.copy().astype(np.float64)
    
    #3.实现高斯滤波核
    K=np.zeros((K_size,K_size),dtype=np.float64)
    for x in range(-pad,-pad+K_size):
        for y in range(-pad,-pad+K_size):
            K[y+pad,x+pad]=np.exp(-(x**2+y**2)/(2*(sigma**2)))
    K/=2*np.pi*sigma*sigma
    #确保高斯滤波核的所有值加起来为1
    K/=K.sum()

    #4.用手动实现的高斯滤波核进行滤波
    tmp=out.copy()
    for y in range(H):
        for x in range(W):
            for c in range(C):
                #实现互相关操作
                out[pad+y,pad+x,c]=np.sum(K*tmp[y:y+K_size,x:x+K_size,c])
    #将out中大于255的数全赋值为255,小于0的数全赋值为0,确保三通道的像素值在0-255之间
    out=np.clip(out,0,255)
    #再次使用python的切片操作,np.unit8类型可以为图像创建一个容器，使得图像能够正确显示
    out=out[pad:pad+H,pad:pad+W].astype(np.uint8)
    return out

if __name__ == '__main__':
    #读取图像
    image=cv.imread('1.Gaussian_Filtering_Kernel/original image.jpg')
    #手动高斯滤波(可以自己选择高斯滤波核的大小和标准差,修改对应的值,不过滤波核的边长得取奇数)
    out=gaussian_filter(image,K_size=5,sigma=2.0)
    #储存结果并自动显示处理过的图像
    cv.imwrite('1.Gaussian_Filtering_Kernel/out image.jpg',out)
    cv.imshow('result',out)
    #cv.waitKey()能控制cv.imshow()所显示图像的时间
    '''
    cv2.waitKey()是一个键盘绑定函数。它的时间量度是毫秒ms。
    函数会等待(n)里面的n毫秒,看是否有键盘输入。
    若有键盘输入,则返回按键的ASCII值。没有键盘输入,则返回-1.一般设置为0,他将无限等待键盘的输入。
    cv2.destroyAllWindows() 用来删除窗口的,()里不指定任何参数,则删除所有窗口,删除特定的窗口,往()输入特定的窗口值。
    '''
    cv.waitKey(0)
    cv.destroyAllWindows()