#!/usr/bin/env python3

"""
    发布方实现：订阅乌龟的位姿信息，转换成坐标系相关关系，再发布
    准备：
        话题：/turtle1/pose
        类型：/turtlesim/Pose

    流程：
        1.导包
        2.初始化ros节点
        3.创建订阅对象
        4.回调函数处理订阅到的信息
        5.spin()
"""

import rospy
from turtlesim.msg import Pose
import tf2_ros
from geometry_msgs.msg import TransformStamped
import tf.transformations

def doPose(pose):
    #1.创建发布坐标系相关关系的对象
    pub=tf2_ros.TransformBroadcaster()
    #2.将pose转换成坐标系相关关系消息
    ts=TransformStamped()
    ts.header.frame_id="world"
    ts.header.stamp=rospy.Time.now()
    ts.child_frame_id="turtle1"

    #子集坐标系相对于父级坐标系的偏移量
    ts.transform.translation.x=pose.x
    ts.transform.translation.y=pose.y
    ts.transform.translation.z=0
    #从欧拉角转换四元数
    qtn=tf.transformations.quaternion_from_euler(0,0,pose.theta)
    ts.transform.rotation.x=qtn[0]
    ts.transform.rotation.y=qtn[1]
    ts.transform.rotation.z=qtn[2]
    ts.transform.rotation.w=qtn[3]

    #3.发布
    pub.sendTransform(ts)

if __name__ == "__main__":
    rospy.init_node("dynamic_pub_p")
    sub=rospy.Subscriber("/turtle1/pose",Pose,doPose,queue_size=100)
    rospy.spin()