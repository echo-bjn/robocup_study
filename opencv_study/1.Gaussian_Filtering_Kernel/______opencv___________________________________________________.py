import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#二维高斯滤波核
def gaussian_kernel_2d(K_size,sigma):
    return cv.getGaussianKernel(K_size,sigma)*cv.getGaussianKernel(K_size,sigma).T
def gaussian_filtering_kernel(K_size,sigma):
    #三维作图可视化显示高斯滤波核 
    #定义三维格式坐标轴图像
    ax1=plt.axes(projection='3d')
    #定义三维数据
    pad=K_size//2
    xx=np.arange(-pad,-pad+K_size,1) #np.arange()：3个参数时,分别是起点、终点、步长
    yy=np.arange(-pad,-pad+K_size,1)
    #np.meshgrid()生成网格点坐标矩阵

    #K为高斯滤波核
    K=gaussian_kernel_2d(K_size,sigma)
    Z=K
    #作图
    ax1.plot_surface(X,Y,Z)
    plt.show()

if __name__ == '__main__':
    KK_size=int(input('请输入高斯滤波核的边长：'))
    ssigma=float(input('请输入高斯滤波核的标准差：'))
    gaussian_filtering_kernel(KK_size,ssigma)