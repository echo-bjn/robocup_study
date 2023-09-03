import os
import random
#遍历文件，将文件名字和内容的所有python都换成class
def replace_name_content():
    #先找到所有文件
    files=filter(lambda filename:filename.endswith('.txt'),os.listdir('test'))
    #分离文件名和后缀
    basefiles=[os.path.splitext(filename)[0] for filename in files]
    #文件重命名,将python换成class
    for filename in basefiles:
        if 'python' in filename:
            filename_new=filename.replace('python','class')
            oldname=os.path.join('test',filename+'.txt')
            newname=os.path.join('test',filename_new+'.txt')
            os.rename(oldname,newname)
    #修改文件内容，将python换成class
    for file in os.listdir('test'):
        lines_new=[]
        path=os.path.join(r'test',file)
        f=open(path,'r+')
        lines=f.readlines()
        for line_list in lines:
            #将换行符替换为空
            line_n=line_list.replace('\n','')
            line_new=line_n.replace('python','class')
            lines_new.append(line_new)
        ff=open(path,'w+')
        for i in range(len(lines_new)-1):
            ff.write(lines_new[i]+'\n')
        ff.write(lines_new[len(lines_new)-1])
replace_name_content()