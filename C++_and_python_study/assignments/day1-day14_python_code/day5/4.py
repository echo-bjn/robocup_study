import os
import random
import string
#新建目录img
def mkdir():
    os.mkdir("img")
    print("文件夹创建成功")
mkdir()
#四位验证码文件名
def file_name():
    name=random.sample(string.ascii_letters+string.digits,4)
    return "".join(name)
#建立文件
def build_file():
    os.chdir("img")
    list1=[file_name() for i in range(100)]
    for name in list1:
        with open(name+".png","w") as file:
            pass
build_file()