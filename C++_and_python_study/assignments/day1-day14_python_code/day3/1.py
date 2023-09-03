#猴子吃桃
def peach_sum():
    total=1
    for i in range(9,0,-1):
        total=(total+1)*2
        if i==1:
            print("第1天的桃子数为：%d"%total)
peach_sum()