def caculate(*num):
    l=[]
    lidx=[]
    avg=sum(num)/len(num)
    for i in num:
        l.append(i)
    for i in range(len(l)):
        if l[i]>avg:
            lidx.append(i)
    return avg,lidx

(aver,index)=caculate(1,2,3,4,5,6,7,8,9,10)
print(f'所有参数的平均值为{aver},参数比平均值大的索引为{index}')