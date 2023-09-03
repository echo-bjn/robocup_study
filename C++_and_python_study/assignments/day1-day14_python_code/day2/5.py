#101-200找素数
import math
sum=0
for i in range(101,201):
    for j in range(2,int(math.sqrt(i))+1):
        if i%j!=0:
            flag=True
        else:
            flag=False
            break
    if flag==True:
        print("%d"%i,end=" ")
print("")