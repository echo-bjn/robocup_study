#!/usr/bin/env python3

"""
    使用python实现消息发布:
        1.导包
        2.初始化ROS节点
        3.初始化发布者对象
        4.编写发布逻辑并发布数据
"""

# 1.导包
import rospy
from std_msgs.msg import String #发布消息的类型

if __name__ == "__main__":
    # 2.初始化ROS节点
    rospy.init_node("sanGouZi")#传入节点名称
    # 3.初始化发布者对象
    pub=rospy.Publisher("fang",String,queue_size=10)
    # 4.编写发布逻辑并发布数据
    #创建数据
    msg=String()
    #指定发布频率
    rate=rospy.Rate(1)
    #设置计数器
    count=0
    rospy.sleep(3) #正式发布数据前先休眠3s,让发布者先注册完,防止订阅者订阅数据的丢失
    #使用循环发布数据
    while not rospy.is_shutdown():
        count+=1
        msg.data="hello"+str(count)
        #发布数据
        pub.publish(msg)
        rospy.loginfo("发布的数据是%s",msg.data)
        rate.sleep()