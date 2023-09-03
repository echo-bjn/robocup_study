def function(arg):
    l=[]
    for i in range(len(arg)):
        if i%2==1:
            l.append(arg[i])
    return l
li_1=[1,2,3,4,5,6,7,8,9,10]
li_2=function(li_1)
print(f'原列表为{li_1}')
print(f'列表奇数位的列表为{li_2}')