#include<iostream>
#include<string>
//Person类
class Person
{
public:
    std::string name;//姓名信息用字符串
    int age;//年龄为整型
    bool gender;//0表示男性，1表示女性
    void personinfo()
    {
        std::cout<<"这位学生的名字是"<<name;
        if(gender) std::cout<<",性别女,";
        else std::cout<<",性别男,";
        std::cout<<"年龄为"<<age<<"岁。"<<std::endl;
    }
};
class Student:public Person
{
public:
    std::string college;//学院信息用字符串
    int Class;//班级为整型
    void personinfo()
    {
        Person::personinfo();
        std::cout<<"这位学生所在学院是"<<college<<",所在班级是"<<Class<<"班。"<<std::endl;
    }
};
//main函数
int main()
{
    Student A;
    std::cout<<"请输入这位同学的相关信息(名字，性别(0:男生，1：女生)，年龄，学院，班级)，以空格隔开："<<std::endl;
    std::cin>>A.name>>A.gender>>A.age>>A.college>>A.Class;
    A.personinfo();
    return 0;
}