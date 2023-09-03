import random
import shutil
#创建文件
def build_file():
    file=open('test.txt','w+')
    n=int(input("请输入你要创建的文件的行数："))
    for i in range(n-1):
        s=chr(random.randint(32,126))
        file.write(s+'\n')
    s=chr(random.randint(32,126))
    file.write(s)
build_file()
#复制文件
def copy_file():
    shutil.copy('test.txt','copy_test.txt')
copy_file()
