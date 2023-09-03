#include <iostream>
//方法1：比较交换法
void solution_one(){
    int x,y,z,temp;
    std::cout<<"请输入三个整数：";
    std::cin>>x>>y>>z;//输入x，y，z
    //比较大小并交换，使得x，y，z顺序为从小到大
    if(x>y){
        temp=x;
        x=y;
        y=temp;
    }
        if(x>z){
        temp=x;
        x=z;
        z=temp;
    }
        if(y>z){
        temp=y;
        y=z;
        z=temp;
    }
    std::cout<<"从小到大输出为"<<x<<" "<<y<<" "<<z;
}
//方法2：排序算法
void solution_two(){
    std::cout<<"请输入三个整数：";
    int num[3]={0},temp;
    for(int i=0;i<3;i++){
        std::cin>>num[i];
    }
    //吊桶排序算法
    for(int i=0;i<2;i++){
        for(int j=0;j<2-i;j++){
            if(num[j]>num[j+1]){
                temp=num[j];
                num[j]=num[j+1];
                num[j+1]=temp;
            }
        }
    }
    std::cout<<"从小到大输出为"<<num[0]<<" "<<num[1]<<" "<<num[2];
}
int main() {
    std::cout<<"方法一：比较交换法"<<std::endl;
    solution_one();
    std::cout<<std::endl;
    std::cout<<"方法二：排序算法"<<std::endl;
    solution_two();
    std::cout<<std::endl;
    return 0;
}
