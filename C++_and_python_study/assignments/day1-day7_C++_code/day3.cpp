#include<iostream>
#include<string>
#include<sstream>
//方法1：直接截取各位数字法
void cutout_num(int n){
    int number=0,a[1000]={0};//number记录n的位数，a[1000]记录每位具体的值
    //每次截取一位后，将n/10赋值于n
    for(int i=0;i<1000;i++){
        a[i]=n%10;
        n=n/10;
        if(n==0){
            number=i+1;
            break;
        }
    }
    std::cout<<"这个数字有"<<number<<"位"<<std::endl;
    std::cout<<"这个数字逆序输出为:";
    for(int i=0;i<number;i++) std::cout<<a[i];
}
//方法2：字符串法
void str_num(int n){
    std::string str_n;
    //利用stringstream来实现字符串和整数的转换
    std::stringstream ss;
    ss<<n;
    ss>>str_n;
    std::cout<<"这个数字有"<<str_n.length()<<"位"<<std::endl;
    std::cout<<"这个数字逆序输出为:";
    for(int i=str_n.length()-1;i>=0;i--) std::cout<<str_n[i];
}
//main函数
int main(){
    int n;
    std::cout<<"请输入一个正整数：";
    std::cin>>n;
    std::cout<<"方法1——直接截取各位数字法："<<std::endl;
    cutout_num(n);
    std::cout<<std::endl;
    std::cout<<"方法2——字符串法："<<std::endl;
    str_num(n);
    std::cout<<std::endl;
    return 0;
}