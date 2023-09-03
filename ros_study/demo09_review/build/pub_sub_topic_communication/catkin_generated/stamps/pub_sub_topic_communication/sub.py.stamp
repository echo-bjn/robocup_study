#! /usr/bin/env python

"""
    使用python实现消息发布:
        1.导包
        2.初始化ROS节点
        3.初始化订阅者对象
        4.回调函数处理数据
        5.spin()
"""

# 1.导包
import rospy
from std_msgs.msg import String

def doMsg(msg):
    rospy.loginfo("花花订阅到的数据为%s",msg.data)

if __name__ == "__main__":
    # 2.初始化ROS节点
    rospy.init_node("HuaHua")
    # 3.初始化发布者对象 和 4.回调函数处理数据
    sub=rospy.Subscriber("fang",String,doMsg,queue_size=10)
    # 5.spin()
    rospy.spin()