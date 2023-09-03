import numpy as np
from scipy import ndimage as ndi 
from skimage import feature
from matplotlib import pyplot as plt

#Canny边缘检测算法是基于高斯函数导数来计算梯度的强度,能够提取图像边界。
def Canny_Algorithm():
    #1.产生一个正方形噪声图像  
    img=np.zeros((128,128))
    img[32:-32,32:-32]=1
    #ndi.rotate()函数可以进行图像旋转
    img=ndi.rotate(img,15,mode='constant')
    #高斯滤波使图像变模糊
    img=ndi.gaussian_filter(img,4)
    #np.random.random((100,20))代表生成100行20列的浮点数，浮点数都是从0-1随机的
    img+=0.2*np.random.random(img.shape)

    #2.对上述生成的图像进行两个simga值的Canny边缘检测,直接调用skiskimage库中的feature.canny()函数    
    '''
    函数:feature.canny(image,sigma=1.0,low_threshold=None,high_threshold=None,mask=None,use_quantiles=False)
    sigma:高斯滤波器的标准差
    low_threshold:Canny算法最后一步中，小于该阈值的像素直接置为0
    high_threshold:Canny算法最后一步中，大于该阈值的像素直接置为255
    '''
    edges1=feature.canny(img)
    edges2=feature.canny(img,sigma=3)
    edges3=feature.canny(img,sigma=5)

    #3.展示结果
    #plt.subplot()中的sharex和sharey表示subplot中x轴和y轴的刻度，True表示所有的subplot都保持相同的刻度
    fig,(ax1,ax2,ax3,ax4)=plt.subplots(nrows=1,ncols=4,figsize=(12,3),sharex=True,sharey=True)

    #绘制四幅灰度图,去除坐标轴
    ax1.imshow(img,cmap=plt.cm.gray)
    ax1.axis('off')
    ax1.set_title('noisy image',fontsize=20)

    ax2.imshow(edges1,cmap=plt.cm.gray)
    ax2.axis('off')
    ax2.set_title(r'Canny filter,$\sigma=1$',fontsize=20)

    ax3.imshow(edges2,cmap=plt.cm.gray)
    ax3.axis('off')
    ax3.set_title(r'Canny filter,$\sigma=3$',fontsize=20)

    ax4.imshow(edges3,cmap=plt.cm.gray)
    ax4.axis('off')
    ax4.set_title(r'Canny filter,$\sigma=5$',fontsize=20)

    #显示图像
    fig.tight_layout()
    plt.show()
if __name__ == '__main__':
    Canny_Algorithm()