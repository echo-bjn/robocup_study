#!/usr/bin/env python3

import rospy
import tf2_ros
from tf2_geometry_msgs import tf2_geometry_msgs

if __name__ == "__main__":
    rospy.init_node("tfs_sub_p")
    
    #创建缓存对象
    buffer=tf2_ros.Buffer()
    #创建订阅对象(将缓存传入)
    sub=tf2_ros.TransformListener(buffer)
    
    #组织被转换的坐标点
    ps=tf2_geometry_msgs.PointStamped()
    ps.header.stamp=rospy.Time.now()
    ps.header.frame_id="son1"
    ps.point.x=1.0
    ps.point.y=2.0
    ps.point.z=3.0

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
            ts=buffer.lookup_transform("son2","son1",rospy.Time(0))
            rospy.loginfo("父级坐标系:%s,子级坐标系:%s,偏移量(%.2f,%.2f,%.2f)",
                        ts.header.frame_id,
                        ts.child_frame_id,
                        ts.transform.translation.x,
                        ts.transform.translation.y,
                        ts.transform.translation.z
                        )

            #转换实现
            ps_out=buffer.transform(ps,"son2")
            rospy.loginfo("转换后的坐标(%.2f,%.2f,%.2f),参考的坐标系:%s",
                        ps_out.point.x,
                        ps_out.point.y,
                        ps_out.point.z,
                        ps_out.header.frame_id
                        )
        except Exception as e:
            rospy.logwarn("错误提示:%s",e)
            
        rate.sleep()