/*
    需要：向服务端发送请求
*/

#include "ros/ros.h"
#include "turtlesim/Spawn.h"

int main(int argc, char *argv[])
{
    setlocale(LC_ALL,"");
    ros::init(argc,argv,"service_call");
    ros::NodeHandle nh;
    ros::ServiceClient client=nh.serviceClient<turtlesim::Spawn>("/spawn");
    turtlesim::Spawn spawn;
    spawn.request.x=1.0;
    spawn.request.y=4.0;
    spawn.request.theta=-1.57;
    spawn.request.name="turtle2";
    client.waitForExistence();
    bool flag=client.call(spawn);
    if(flag){
        ROS_INFO("乌龟生成成功，新乌龟叫：%s",spawn.request.name.c_str());
    }else{
        ROS_INFO("请求失败");
    }
    return 0;
}
