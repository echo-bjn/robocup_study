import random
f=open('data.txt','w+')
for i in range(100000-1):
    f.write(str(random.randint(1,100))+'\n')
f.write(str(random.randint(1,100)))