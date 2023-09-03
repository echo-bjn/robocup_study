import math
import numpy as np
#Point类
class Point:
    #构造函数
    def __init__(self,x,y,z=0):
        self.x=x
        self.y=y
        self.z=z
        self.name='Point'
        print(f"创建了Point({self.x},{self.y},{self.z})")
    #析构函数
    def __del__(self):
        print(f"销毁了Point({self.x},{self.y},{self.z})")
    #打印函数
    def Print(self):
        print(f"Point({self.x},{self.y},{self.z})")
    #Point类重载加法运算符
    def __add__(self,other):
        x=self.x+other.x
        y=self.y+other.y
        z=self.x+other.z
        if other.name=='Vector':
            return Point(x,y,z)
        elif other.name=='Point':
            print("Point类之间不能相加,发生错误！")
            return
    #Point类重载减法运算符
    def __sub__(self,other):
        x=self.x-other.x
        y=self.y-other.y
        z=self.x-other.z
        if other.name=='Vector':
            return Point(x,y,z)
        elif other.name=='Point':
            return Vector(x,y,z)
    #Point类重载'=='符号
    def __eq__(self,other):
        if self.x==other.x and self.y==other.y and self.z==other.z and other.name=='Vector':
            return True
        else:
            return False 
    #Point类重载'<'符号
    def __lt__(self,other):
        if math.sqrt(self.x**2+self.y**2+self.z**2)<math.sqrt(other.x**2+other.y**2+other.z**2):
            return True
        else:
            return False
#Vector类
class Vector:
    #构造函数
    def __init__(self,x,y,z=0):
        self.x=x
        self.y=y
        self.z=z
        self.name=Vector
        print(f"创建了Vector({self.x},{self.y},{self.z})")
    #析构函数
    def __del__(self):
        print(f"销毁了Vector({self.x},{self.y},{self.z})")
    #打印函数
    def Print(self):
        print(f"Vector({self.x},{self.y},{self.z})")
    #Vector类重载加法运算符
    def __add__(self,other):
        x=self.x+other.x
        y=self.y+other.y
        z=self.z+other.z
        return Vector(x,y,z)
    #Vector类重载减法运算符
    def __sub__(self,other):
        x=self.x-other.x
        y=self.y-other.y
        z=self.z-other.z
        return Vector(x,y,z)
    #Vector类重载'<'符号
    def __lt__(self,other):
        if math.sqrt(self.x**2+self.y**2+self.z**2)<math.sqrt(other.x**2+other.y**2+other.z**2):
            return True
        else:
            return False
    #重载Vector类的乘法,将向量绕z轴逆时针旋转theta度
    def __mul__(self,theta):
        # *theta表示绕向量other逆时针旋转theta度
        u=np.array([0,0,1])
        v=np.array([self.x,self.y,self.z])
        sin_theta=np.sin(theta*np.pi/180)
        cos_theta=np.cos(theta*np.pi/180)
        v_new=v*cos_theta+np.cross(u,v)*sin_theta+np.dot(u,v)*u*(1-cos_theta)
        return Vector(round(v_new[0],2),round(v_new[1],2),round(v_new[2],2))
    #重载Vector类的除法，将向量绕z轴顺时针旋转theta度
    def __truediv__(self,theta):
        # /theta表示绕向量other顺时针旋转theta度
        theta_2=-theta
        u=np.array([0,0,1])
        v=np.array([self.x,self.y,self.z])
        sin_theta=np.sin(theta_2*np.pi/180)
        cos_theta=np.cos(theta_2*np.pi/180)
        v_new=v*cos_theta+np.cross(u,v)*sin_theta+np.dot(u,v)*u*(1-cos_theta)
        return Vector(round(v_new[0],2),round(v_new[1],2),round(v_new[2],2))