n=233
l_1=list(range(1,234))
count=0
while len(l_1)>1:
    l_2=l_1[:] #复制列表
    for i in range(0,len(l_2)):
        count+=1
        if count%3==0:
            l_1.remove(l_2[i])
print("最后剩下的人是最初的%d号"%l_1[0])