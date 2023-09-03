#include "ros/ros.h"
#include "turtlesim/Pose.h"
#include "tf2_ros/transform_broadcaster.h"
#include "geometry_msgs/TransformStamped.h"
#include "tf2/LinearMath/Quaternion.h"

//声明变量接收传递的参数
std::string turtle_name;

void doPose(const turtlesim::Pose::ConstPtr& pose){
    //获取位姿信息，转换成坐标系相对关系
    //1.创建发布对象
    static tf2_ros::TransformBroadcaster pub;
    //2.组织被发布的数据
    geometry_msgs::TransformStamped ts;
    ts.header.frame_id="world";
    ts.header.stamp=ros::Time::now();
    ts.child_frame_id=turtle_name;
    //坐标系偏移量设置
    ts.transform.translation.x=pose->x;
    ts.transform.translation.y=pose->y;
    ts.transform.translation.z=0;
    //坐标系四元数
    /*
        位姿信息中没有四元数，但是有个偏航角度，又已知乌龟是2d，没有翻滚和俯仰角度,
        所以得到乌龟的欧拉角：0,0,theta
    */
    tf2::Quaternion qtn;
    qtn.setRPY(0,0,pose->theta);
    ts.transform.rotation.x=qtn.getX();
    ts.transform.rotation.y=qtn.getY();
    ts.transform.rotation.z=qtn.getZ();
    ts.transform.rotation.w=qtn.getW();
    //3.发布
    pub.sendTransform(ts);
}

int main(int argc, char *argv[])
{
    setlocale(LC_ALL,"");
    //关键点1：订阅的话题名称,turtle1或者turtle2动态传入
    ros::init(argc,argv,"dynamic_pub");
    ros::NodeHandle nh;
    /*
        解析launch文件，通过args传入的参数
    */
    if(argc!=2){
        ROS_ERROR("请传入一个参数！");
    }
    else{
        turtle_name=argv[1];
    }
    ros::Subscriber sub=nh.subscribe(turtle_name+"/pose",100,doPose);
    ros::spin();
    return 0;
}