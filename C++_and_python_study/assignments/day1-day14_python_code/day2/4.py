#水仙花数
for x in range(100,1000):
    a=x//100 #x百位上的数字
    b=x//10%10 #x十位上的数字
    c=x%10
    if a**3+b**3+c**3==x:
        print(x)