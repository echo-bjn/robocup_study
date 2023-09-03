import os
import random
#建立test目录以及i个文件,并且修改文件名和文件内容
def build_modify_dir_file(file_num:int,line_num:int):
    os.mkdir('test')
    for i in range(file_num):
        with open('test/'+f'{i+1}'+'.txt','a+') as file:
            for j in range(line_num-1):
                s=chr(random.randint(32,126))
                file.write(s+'\n')
            s=chr(random.randint(32,126))
            file.write(s)
            pass
    #先找到所有文件
    files=filter(lambda filename:filename.endswith('.txt'),os.listdir('test'))
    #分离文件名和后缀
    basefiles=[os.path.splitext(filename)[0] for filename in files]
    #文件重命名
    for filename in basefiles:
        oldname=os.path.join('test',filename+'.txt')
        newname=os.path.join('test',filename+'-python'+'.txt')
        os.rename(oldname,newname)
    #修改文件内容,在每行后面追加‘-python’
    for file in os.listdir('test'):
        lines_new=[]
        path=os.path.join(r'test',file)
        f=open(path,'r+')
        lines=f.readlines()
        for line_list in lines:
            #将换行符替换为空
            line_new=line_list.replace('\n','')
            line_new=line_new+'-python'
            lines_new.append(line_new)
        ff=open(path,'w+')
        for i in range(len(lines_new)-1):
            ff.write(lines_new[i]+'\n')
        ff.write(lines_new[len(lines_new)-1])
def main():
    file_num=int(input("请决定你要创建的文件数目："))
    line_num=int(input("请决定你要创建的文件中行的数目："))
    build_modify_dir_file(file_num,line_num)
if __name__ == '__main__':
    main()