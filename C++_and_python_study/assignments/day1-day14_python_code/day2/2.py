a=int(input("请输入一个数字:"))
times=int(input("请输入一个数字，作为相加的个数:"))
sum=0
record=a
print("sum=",end="")
for i in range(1,times+1):
    if i!=times:
        print("%d+"%a,end="")
    else:
        print("%d"%a,end="=")
    sum=a+sum
    a=a+record*(10**i)
print(sum)