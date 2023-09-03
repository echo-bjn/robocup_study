/*
    需求:订阅发布的坐标系的相对关系，传入一个坐标点，使用tf实现转换

    流程:1.包含头文件
        2.设置编码 节点初始化 NodeHandle(必须)
        3.创建订阅对象 ----->订阅坐标系相对关系
        4.组织一个坐标点数据
        5.转换算法 需要调用TF内置实现
        6.最后输出
*/

#include "ros/ros.h"
#include "tf2_ros/transform_listener.h"
#include "tf2_ros/buffer.h"
#include "geometry_msgs/PointStamped.h"
#include "tf2_geometry_msgs/tf2_geometry_msgs.h"

int main(int argc, char *argv[])
{
    setlocale(LC_ALL,"");
    ros::init(argc,argv,"dynamic_sub");
    ros::NodeHandle nh;
    
    //3.创建订阅对象
    //创建buffer缓存
    tf2_ros::Buffer buffer;
    //再创建监听对象(监听对象可以将订阅到的数据存入buffer)
    tf2_ros::TransformListener listener(buffer);
    
    //4.组织一个坐标点数据
    geometry_msgs::PointStamped ps;
    ps.header.frame_id="turtle1";
    //时间戳不一样
    ps.header.stamp=ros::Time(0.0);
    ps.point.x=2.0;
    ps.point.y=3.0;
    ps.point.z=5.0;

    //添加休眠,足够时间来让订阅者订阅到发布消息
    //ros::Duration(2).sleep();
    
    //5.转换算法
    ros::Rate rate(10);
    while(ros::ok())
    {
        //核心代码实现 ---要将ps转换成相对于world的坐标点
        geometry_msgs::PointStamped ps_out;
        /*
            调用了buffer的转换函数transform
            参数1:被转换的坐标点
            参数2:目标坐标系
            返回值输出的坐标点

            PS1:调用时必须包含头文件 tf2_geometry_msgs/tf2_geometry_msgs.h
            PS2:运行时存在的问题,跑出一个异常 world 不存在
                原因:订阅数据是一个耗时操作，可能在调用transform转换函数时，
                    坐标系的相对关系还没有订阅到，因此出现异常
                解决:
                    方案1:在调用转换函数前，执行休眠
                    方案2:进行异常处理 try语句 (建议)
        */
        try
        {
            ps_out=buffer.transform(ps,"world");
            //6.输出结果
            ROS_INFO("转换后的坐标值：(%.2f,%.2f,%.2f),参考的坐标系:%s",
                    ps_out.point.x,
                    ps_out.point.y,
                    ps_out.point.z,
                    ps.header.frame_id.c_str());
        }  
        catch(const std::exception& e)
        {
            ROS_INFO("异常消息:%s",e.what());
        }
        
        rate.sleep();
        ros::spinOnce();
    }
    return 0;
}
