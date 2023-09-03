/*
    演示参数删除：
    实现:
        ros::NodeHandle
            deleteParam()
        ros::param
            del()
*/

#include "ros/ros.h"

int main(int argc, char *argv[])
{
    setlocale(LC_ALL,"");
    ros::init(argc,argv,"param_del_c");
    ros::NodeHandle nh;
    
    //NodeHandle
    bool flag1=nh.deleteParam("radius");
    if(flag1){
        ROS_INFO("radius删除成功!");
    }else{
        ROS_INFO("radius删除失败!");
    }

    //ros::param
    bool flag2=ros::param::del("radius_param");
    if(flag2){
        ROS_INFO("radius_param删除成功!");
    }else{
        ROS_INFO("radius_param删除失败!");
    }
    return 0;
}
