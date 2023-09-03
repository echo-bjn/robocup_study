//1.包含ros头文件
#include "ros/ros.h"
//2.编写main函数
int main(int argc, char *argv[])
{
    setlocale(LC_ALL,"");//防止中文输出乱码
    //3.初始化ros节点
    ros::init(argc,argv,"hello");
    //4.输出日志
    ROS_INFO("hahahahaha,哈哈");
    return 0;
}