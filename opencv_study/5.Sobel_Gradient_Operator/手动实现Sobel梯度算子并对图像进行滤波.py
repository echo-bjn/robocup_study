import cv2 as cv
import numpy as np
#sobel梯度算子可以计算图像梯度，计算图像梯度的作用是提取边界
#手动实现sobel梯度算子并进行滤波(所要处理的图像:img)
def Sobel_Filtering(img,K_size=3):
    #1.获取图像的shape
    if len(img.shape)==3:
        H,W,C=img.shape
    else:
        H,W=img.shape
    
    #2.进行原图像的zero padding
    pad=K_size//2
    out=np.zeros((H+pad*2,W+pad*2),dtype=np.float)
    #利用python的切片操作
    out[pad:pad+H,pad:pad+W]=img.copy().astype(np.float)
    out_v=out.copy()
    out_h=out.copy()

    #3.Sobel梯度算子
    #Sobel vertical
    Kv=[[1.,2.,1.],[0.,0.,0.],[-1.,-2.,-1.]]
    #Sobel horizontal
    Kh=[[1.,0.,-1.],[2.,0.,-2.],[1.,0.,-1.]]
    
    #4.用Sobel梯度算子进行滤波
    tmp=out.copy()
    for y in range(H):
        for x in range(W):
            #实现互相关操作
            out_v[pad+y,pad+x]=np.sum(Kv*tmp[y:y+K_size,x:x+K_size])
            out_h[pad+y,pad+x]=np.sum(Kh*tmp[y:y+K_size,x:x+K_size])
    #简化法结合横向纵向边界
    out_vh=out_v+out_h
    #将out_v,out_h,out_vh中大于255的数全赋值为255,小于0的数全赋值为0,确保像素值在0-255之间
    out_v=np.clip(out_v,0,255)
    out_h=np.clip(out_h,0,255)
    out_vh=np.clip(out_vh,0,255)

    #np.unit8类型可以为图像创建一个容器，使得图像能够正确显示
    out_v=out_v[pad:pad+H,pad:pad+W].astype(np.uint8)
    out_h=out_h[pad:pad+H,pad:pad+W].astype(np.uint8)
    out_vh=out_vh[pad:pad+H,pad:pad+W].astype(np.uint8)

    return out_v,out_h,out_vh

if __name__ == '__main__':
    #读取灰度图像
    image=cv.imread('original image.jpg',0)
    #手动滤波
    out_vv,out_hh,out_vvhh=Sobel_Filtering(image,K_size=3)
    #储存结果
    cv.imwrite('horizontal_edge_image.jpg',out_vv)
    cv.imwrite('vertical_edge_image.jpg',out_hh)
    cv.imwrite('horizontal+vertical_edge_image.jpg',out_vvhh)