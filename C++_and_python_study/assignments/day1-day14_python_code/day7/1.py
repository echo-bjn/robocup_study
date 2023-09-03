import random
import statistics
import numpy as np
#创建10行3列的文件
def build_file():
    f=open('test.txt','w+')
    for i in range(9):
        f.write(str(random.randint(0,100)))
        for j in range(2):
            f.write(','+str(random.randint(0,100)))
        f.write('\n')
    f.write(str(random.randint(0,100)))
    for i in range(2):
        f.write(','+str(random.randint(0,100)))
build_file()
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