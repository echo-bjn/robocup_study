#include "ros/ros.h"

int main(int argc, char *argv[])
{
    ros::init(argc,argv,"erGouZi");
    ros::NodeHandle nh;

    //ros::param设置
    //1.全局
    ros::param::set("/radiusA",10);
    //2.相对
    ros::param::set("radiusB",100);
    //3.私有
    ros::param::set("~radiusC",1000);
    
    //ros::NodeHandle设置
    //1.全局
    nh.setParam("/radiusA_nh",10);
    //2.相对
    nh.setParam("radiusB_nh",100);
    //3.私有
    ros::NodeHandle nh_private("~");
    nh_private.setParam("radiusC_nh",1000);
    return 0;
}
