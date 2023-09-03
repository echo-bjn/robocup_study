#!/usr/bin/env python3

import rospy
import tf2_ros
from tf2_geometry_msgs import tf2_geometry_msgs
from geometry_msgs.msg import Twist
import math

if __name__ == "__main__":
    rospy.init_node("tfs_sub_p")
    
    #创建缓存对象
    buffer=tf2_ros.Buffer()
    #创建订阅对象(将缓存传入)
    sub=tf2_ros.TransformListener(buffer)


    #创建速度消息发布对象
    pub=rospy.Publisher("/turtle2/cmd_vel",Twist,queue_size=100)

    #转换逻辑实现,调用tf封装的算法
    rate=rospy.Rate(10)
    while not rospy.is_shutdown():
        try:
            #计算son1相对于son2的相对关系
            """
                A相对于B的信息
                参数1:目标坐标系B 
                参数2:源坐标系  A
                参数3:ros::Time(0) 取间隔最短的两个坐标系帧(son1相对于world和son2相对于world)计算相对关系
                返回值:geometry_msgs::TransformStamped 源坐标系A相对于目标坐标系B的相对关系
            """
            ts=buffer.lookup_transform("turtle2","turtle1",rospy.Time(0))
            # rospy.loginfo("父级坐标系:%s,子级坐标系:%s,偏移量(%.2f,%.2f,%.2f)",
            #             ts.header.frame_id,
            #             ts.child_frame_id,
            #             ts.transform.translation.x,
            #             ts.transform.translation.y,
            #             ts.transform.translation.z
            #             )
            
            #组织Twist消息
            twist=Twist()
            """ 
            组织速度消息只需要设置线速度的x与角速度的z
            linear.x=系数*(两个坐标系的直线距离(开方(x^2+y^2)))
            angular.z=系数*反正切(对边，邻边) 
            """          
            twist.linear.x=0.5*math.sqrt(math.pow(ts.transform.translation.x,2)+math.pow(ts.transform.translation.y,2))         
            twist.angular.z=4*math.atan2(ts.transform.translation.y,ts.transform.translation.x)             
            
            #发布消息
            pub.publish(twist)

        except Exception as e:
            rospy.logwarn("错误提示:%s",e)
            
        rate.sleep()