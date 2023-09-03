import random
import statistics
import numpy as np
from typing import List
#创建n行m列的文件
def build_file(n:int,m:int):
    f=open('test.txt','w+')
    for i in range(n-1):
        f.write(str(random.randint(0,100)))
        for j in range(m-1):
            f.write(','+str(random.randint(0,100)))
        f.write('\n')
    f.write(str(random.randint(0,100)))
    for i in range(m-1):
        f.write(','+str(random.randint(0,100)))
build_file(10,3)
#求出第二列的相关数据
def caculate():
    l=[]
    f=open('test.txt','r')
    lines=f.readlines()
    for line in lines:
        line_array=line.split(',')
        l.append(int(line_array[1]))
    print(f'该文件第二列数据的最大值为{max(l)},最小值为{min(l)},平均值为{np.mean(l)},中位数为{statistics.median(l)}')
caculate()