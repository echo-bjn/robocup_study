#生命游戏
import numpy as np
import random
import time
#Universe类
class Universe:
    #构造函数
    def __init__(self,height,width):
        #总世界的一个切片是Universe
        self.height=height
        self.width=width
        self.Universe=world[0:height,0:width]
        for i in range(height):
            for j in range(width):
                self.Universe[i][j]=' '
    #显示当前小世界状态
    def Show(self):
        print(self.Universe)
    #激活细胞
    def Seed(self):
        l=[]
        for i in range(int(self.height*self.width/4)):
            m=random.randint(0,self.height-1)
            n=random.randint(0,self.width-1)
            l.append([m,n])
        for i in range(int(self.height*self.width/4)):
            self.Universe[l[i][0]][l[i][1]]='*'
    #判断细胞是否存活
    def Alive(self,m,n):
        if self.Universe[m][n]=='*':
            return True
        else:
            return False
    #判断邻近存活细胞的数量
    def Neighbors(self,m,n):
        num=0
        #内部
        if m>0 and m<self.height-1 and n>0 and n<self.width-1:
            for i in range(m-1,m+2):
                for j in range(n-1,n+2):
                        if self.Alive(i,j):
                            if not(i==m and j==n): 
                                num+=1                       
        #上边界
        elif m==0:
            if n==0:
                if(self.Alive(0,1)): num+=1
                if(self.Alive(1,0)): num+=1
                if(self.Alive(1,1)): num+=1
            elif n==self.width-1:
                if(self.Alive(0,n-1)): num+=1
                if(self.Alive(1,n)): num+=1
                if(self.Alive(1,n-1)): num+=1
            else:
                for i in range(0,2):
                    for j in range(n-1,n+2):
                        if self.Alive(i,j):
                            if not(i==m and j==n): 
                                num+=1 
        #下边界
        elif m==self.width-1:
            if n==0:
                if(self.Alive(m,1)): num+=1
                if(self.Alive(m-1,0)): num+=1
                if(self.Alive(m-1,1)): num+=1
            elif n==self.width-1:
                if(self.Alive(m,n-1)): num+=1
                if(self.Alive(m-1,n)): num+=1
                if(self.Alive(m-1,n-1)): num+=1
            else:
                for i in range(m-1,m+1):
                    for j in range(n-1,n+2):
                        if self.Alive(i,j):
                            if not(i==m and j==n): 
                                num+=1 
        #左边界
        elif n==0 and m!=0 and m!=self.height-1:
                for i in range(m-1,m+2):
                    for j in range(0,2):
                        if self.Alive(i,j):
                            if not(i==m and j==n): 
                                num+=1 
        #右边界
        elif n==self.width-1 and m!=0 and m!=self.height-1:
                for i in range(m-1,m+2):
                    for j in range(n-1,n+1):
                        if self.Alive(i,j):
                            if not(i==m and j==n): 
                                num+=1 
        return num
    #判断细胞在下一世代存活或死亡
    def Next(self,m,n):
        if self.Alive(m,n):
            if self.Neighbors(m,n)<2:
                return False
            elif self.Neighbors(m,n)==2 or self.Neighbors(m,n)==3:
                return True
            elif self.Neighbors(m,n)>3:
                return False
        else:
            if self.Neighbors(m,n)==3:
                return True
            else:
                return False
    #平行世界
    def Step(self):
        Universe_next=self.Universe
        for i in range(self.height):
            for j in range(self.width):
                if self.Next(i,j):
                    Universe_next[i][j]='*'
                else:
                    Universe_next[i][j]=' '
        Universe_next,self.Universe=self.Universe,Universe_next
    
if __name__ == '__main__':
    #建立世界,一个80*15的二维网络,' '表示死亡的细胞，'*'表示存活的细胞
    world=[]
    for i in range(15):
        world.append(' ')
    world=[world]*80
    world=np.array(world)
    #建立小世界
    U=Universe(15,15)
    U.Seed()
    U.Show()
    while 1==1:
        U.Step()
        U.Show()
        time.sleep(0.2)
        print('\033[2J')