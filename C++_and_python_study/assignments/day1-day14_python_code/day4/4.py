list=[5,16,23,38,44,59,61,75,89,90,100]
m=int(input("请输入你要移动的位置数："))
for i in range(m):
    list.insert(0,list.pop())
print("移动完成后数组为：",end='')
print(list)