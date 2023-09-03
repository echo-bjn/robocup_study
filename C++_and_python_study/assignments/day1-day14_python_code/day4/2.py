list=[1,5,9,15,27,38]
num=int(input("请输入你要插入的数字："))
if (num>list[len(list)-1]):
    list.append(num)
else:
    for i in range(len(list)):
        if num<list[i]:
            list.insert(i,num)
            break
print("插入后的数组为：",end='')
print(list)