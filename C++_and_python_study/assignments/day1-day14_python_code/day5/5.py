import os
import random
import string
#四位验证码文件名
def file_name():
    name=random.sample(string.ascii_letters+string.digits,4)
    return "".join(name)
#建立目录以及文件
def build_file():
    os.mkdir("img")
    list1=[file_name() for i in range(100)]
    for name in list1:
        with open("img/"+name + ".png" , "a+") as file:
            pass
build_file()
#随机更改50个文件的后缀
def change_filenamebehind(dirname,old_suffix,new_suffix):
    num=0
    #找出以png结尾的文件名
    pngfile=filter(lambda filename:filename.endswith(old_suffix),os.listdir(dirname))
    #分离文件名和后缀
    basefiles=[os.path.splitext(filename)[0] for filename in pngfile]
    #文件重命名
    for filename in basefiles:
        num+=1
        oldname=os.path.join(dirname,filename+old_suffix)
        newname=os.path.join(dirname,filename+new_suffix)
        os.rename(oldname,newname)
        print("%s重命名为%s成功"%(oldname,newname))
        if num==50:
            break
change_filenamebehind("img",".png",".jpg")