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
#在文件开头结尾追加'--python'
def add_file_content():
    with open('test.txt','r+') as f:
        content=f.read()
        f.seek(0,0)
        f.write('--python'+content)
        f.seek(0,2)
        f.write('--python')
add_file_content()
#比较两个文件
def contrast_file():
    f1=open('test.txt','r')
    f2=open('copy_test.txt','r')
    lines1=f1.readlines()
    lines2=f2.readlines()
    l=min(len(lines1),len(lines2))
    for i in range(l):
        if lines1[i]!=lines2[i]:
            print(f"test.txt和copy_test.txt的第{i+1}行不同")
    if l==len(lines1) and l!=len(lines2):
        print(f'test.txt比copy.txt少了{len(lines2)-len}行')
    elif l==len(lines2) and l!=len(lines1):
        print(f'test.txt比copy.txt多了{len(lines1)-len}行')
contrast_file()