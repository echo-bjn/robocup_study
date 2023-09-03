import numpy as np
#matplotlib库提供了丰富的三维绘图工具
from matplotlib import pyplot as plt
#从mpl_toolkits.mplot3d库中导入对象Axes3D，生成具有三维格式的对象Axes3D
from mpl_toolkits.mplot3d import Axes3D

def gaussian_filtering_kernel(K_size,sigma):
    #三维作图可视化显示高斯滤波核 
    #定义三维格式坐标轴图像
    ax1=plt.axes(projection='3d')
    #定义三维数据
    pad=K_size//2
    xx=np.arange(-pad,-pad+K_size,1)
    yy=np.arange(-pad,-pad+K_size,1)
    #np.meshgrid()生成网格点坐标矩阵
    X,Y=np.meshgrid(xx,yy)
    #K为高斯滤波核
    K=np.zeros((K_size,K_size),dtype=np.float64)
    for x in range(-pad,-pad+K_size):
        for y in range(-pad,-pad+K_size):
            K[y+pad,x+pad]=np.exp(-(x**2+y**2)/(2*(sigma**2)))
    K/=2*np.pi*sigma*sigma
    #确保高斯滤波核的所有值加起来为1
    K/=K.sum()
    Z=K
    #作图
    ax1.plot_surface(X,Y,Z)
    plt.show()

if __name__ == '__main__':
    KK_size=int(input('请输入高斯滤波核的边长：'))
    ssigma=float(input('请输入高斯滤波核的标准差：'))
    gaussian_filtering_kernel(KK_size,ssigma)