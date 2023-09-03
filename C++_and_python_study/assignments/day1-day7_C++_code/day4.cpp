#include<iostream>
void solution()
{
    //left_person表示剩下的总人数
    //num[233]记录各自的编号
    int num[233]={0},left_person=233;
    for(int i=0;i<233;i++) num[i]=i+1;
    while(left_person!=1)
    {
        int k=0;
        flag:
        for(int i=0;i<233;i++)
        {
            if(num[i]!=0)
            {
                k=k+1;
                if(k>3) k=k%3;
                if(k==3) 
                {
                    //数到3的人就把num[i]赋值为0,表示出局
                    num[i]=0;
                    left_person-=1;
                }
            }
            if(left_person==1) break;
        }
        if(left_person==1) break;
        else goto flag;      
    }
    for(int i=0;i<233;i++)
    {
        if(num[i]!=0) std::cout<<"最后剩下的是原来的"<<num[i]<<"号"<<std::endl;
    }
}
int main()
{
    solution();
    return 0;
}