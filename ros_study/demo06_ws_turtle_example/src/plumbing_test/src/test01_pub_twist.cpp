/*
    需求：发布速度消息
        话题：/turtle1/cmd_vel
        消息：geometry_msgs/Twist

    1.包含头文件
    2.初始化ROS节点
    3.创建节点句柄
    4.创建发布对象
    5.发布逻辑实现
    6.spinOnce()
*/

#include "ros/ros.h"
#include "geometry_msgs/Twist.h"

int main(int argc, char *argv[])
{
    ros::init(argc,argv,"my_control");
    ros::NodeHandle nh;
    ros::Publisher pub=nh.advertise<geometry_msgs::Twist>("/turtle1/cmd_vel",10);
    ros::Rate rate(10);
    geometry_msgs::Twist twist;
    twist.linear.x=1.0;
    twist.linear.y=0.0;
    twist.linear.z=0.0;
    twist.angular.x=0.0;
    twist.angular.y=0.0;
    twist.angular.z=1.0;
    while(ros::ok())
    {
        pub.publish(twist);
        rate.sleep();
        ros::spinOnce();
    }
    return 0;
}