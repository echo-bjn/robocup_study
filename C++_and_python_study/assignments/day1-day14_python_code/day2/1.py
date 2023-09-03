s=input("请输入一个字符串：")
alpha=0 #字母个数
space=0 #空格个数
digit=0 #数字个数
others=0 #其他字符个数
for i in s:
    if i.isalpha():
        alpha+=1
    elif i.isspace():
        space+=1
    elif i.isdigit():
        digit+=1
    else:
        others+=1
print("英文字母有%d个，空格有%d个，数字有%d个，其他字符有%d个"%(alpha,space,digit,others))    