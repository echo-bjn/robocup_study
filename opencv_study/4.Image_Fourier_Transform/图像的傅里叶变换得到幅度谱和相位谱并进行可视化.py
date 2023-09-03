import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def magitude_phase_split(iimg):
    #1.读入iimg的灰度图像(参数0表示读入灰度图像)
    img=cv.imread(iimg,0)
    #利用numpy库中的fft进行傅里叶变换
    img_fft=np.fft.fft2(img)
    #将四个角的中心点移到矩阵中心
    img_fft=np.fft.fftshift(img_fft)
    
    #2.相位谱，利用np.angle()函数
    phase_spectrum=np.angle(img_fft)
    
    #3.幅度谱，利用np.abs()函数,为了使幅度谱更有视觉效果，所以进行了对数变换
    img_fft=np.log(1+np.abs(img_fft))
    magnitude_spectrum=np.abs(img_fft)
    
    #4.可视化显示幅度谱和相位谱
    #plt.subplot(m,n,p)或者plt.subplot(mnp)函数表示分区绘图,(m,n)表示总共有m行n列,p表示位于第几幅图
   plt.subplot(1,2,1),plt.imshow(magnitude_spectrum,cmap='gray'),plt.title('magnitude_spectrum')
    plt.axis('off')
    plt.subplot(1,2,2),plt.imshow(phase_spectrum,cmap='gray'),plt.title('phase_spectrum')
    plt.axis('off')
    plt.show()
    
if __name__ == '__main__':
    magitude_phase_split('original image1.jpg')
