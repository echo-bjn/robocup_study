/*
    订阅方：订阅人的消息
        1.包含头文件
            #include "plumbing_pub_sub/Person.h"
        2.初始化ROS节点
        3.创建ROS节点句柄
        4.创建订阅者对象
        5.处理订阅的数据
        6.spin()
*/

//1.包含头文件
#include "ros/ros.h"
#include "plumbing_pub_sub/Person.h"

void doPerson(const plumbing_pub_sub::Person::ConstPtr& person){
    ROS_INFO("订阅的人的信息:%s,%d,%.2f",person->name.c_str(),person->age,person->height);
}

int main(int argc, char *argv[])
{
    setlocale(LC_ALL,"");
    ROS_INFO("这是订阅方");
    //2.初始化ROS节点
    ros::init(argc,argv,"jiaZhang");
    //3.创建ROS节点句柄
    ros::NodeHandle nh;
    //4.创建订阅者对象 和 5.处理订阅的数据
    ros::Subscriber sub=nh.subscribe("liaoTian",10,doPerson);
    //6.spin()
    ros::spin();
    return 0;
}
