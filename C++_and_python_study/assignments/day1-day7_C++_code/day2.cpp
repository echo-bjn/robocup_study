#include <iostream>
#include<math.h>
//判断一个数是否为质数
bool isprime(int num){
    bool flag=1;
    for(int i=2;i<=sqrt(num);i++){
        if(num%i==0){
            flag=0;
            break;
        }
    }
    return flag;
}
//分解质因数函数
void decompose(){
    int n;
    std::cout<<"请输入一个整数：";
    std::cin>>n;
    std::cout<<n<<"=";
    for(int i=2;i<=n;i++){
        //如果i是质数并且n可以整除i的话则按如下进行
        if(isprime(i)&&(n%i==0)){
            //i小于n时，输出”i*“
            if(i<n) std::cout<<i<<"*";
            //i等于n时，输出i
            else if(n==i) std::cout<<i<<std::endl;
            n/=i;
            i=i-1;
        }
    }
}
//main函数
int main() {
    decompose();
    return 0;
}