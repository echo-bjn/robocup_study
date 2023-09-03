/*
    修改乌龟GUI的背景颜色参数
*/

#include "ros/ros.h"

int main(int argc, char *argv[])
{
    ros::init(argc,argv,"change_bgColor");
    ros::NodeHandle nh;
    nh.setParam("/turtlesim/background_r",50);
    nh.setParam("/turtlesim/background_g",50);
    nh.setParam("/turtlesim/background_b",50);
    return 0;
}
