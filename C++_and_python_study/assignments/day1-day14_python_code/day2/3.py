far=[]
high=100
for i in range(1,11):
    if i==1:
        far.append(high)
    else:
        far.append(high*2)
    high=high/2
print(f'经过的总距离:far={sum(far)}')
print(f'第十次反弹高度:high={high}')