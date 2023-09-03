#include<iostream>
#include<fstream>
#include<cstdlib>
#include<ctime>
void build_file()
{
    int n;
    std::ofstream ofs;
    ofs.open("data.txt",std::ios::out);
    srand(time(0));
    for(int i=0;i<99999;i++)
    {  
        n=rand()%100+1;
        ofs<<n<<std::endl;
    }
    n=rand()%100+1;
    ofs<<n;
    ofs.close();
}
int main()
{
    build_file();
    return 0;
}