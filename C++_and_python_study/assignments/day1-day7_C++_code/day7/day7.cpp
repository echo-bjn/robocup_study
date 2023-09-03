#include<iostream>
#include<fstream>
#include<cstdlib>
#include<ctime>
#include<filesystem>
//生成test.txt文件
void build_file()
{
    int n=0,num;
    std::ofstream fout("test.txt");
    std::cout<<"请输入你想指定的文件行数:";
    std::cin>>n;
    srand(time(0));
    for(int i=0;i<n-1;i++)
    {
        num=rand()%96+32;
        fout<<char(num)<<std::endl;
    }
    num=rand()%96+32;
    fout<<char(num);
}
//复制文件，生成copy_test.txt
void copy_file()
{
    char before[260]={0};
    char after[260]={0};
    std::cout<<"请输入原文件的路径:";
    std::cin>>before;
    std::cout<<"请输入目标文件的路径:";
    std::cin>>after;
    try
    {
        std::filesystem::copy(before,after,std::filesystem::copy_options::recursive);
    }
    catch(const std::exception& e)
    {
        std::cout<<"文件复制失败"<<std::endl;
        return;
    }
    std::cout<<"文件复制成功"<<std::endl;
}
int main()
{
    build_file();
    copy_file();
    return 0;
}