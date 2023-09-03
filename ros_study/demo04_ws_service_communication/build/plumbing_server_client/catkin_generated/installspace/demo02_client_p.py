#!/usr/bin/env python3

"""
    客户端：解析客户端请求，产生响应
        1.导包
        2.初始化ROS节点
        3.创建客户端对象
        4.组织请求的数据并发送请求并处理响应

    优化实现:
        可以在执行节点时，动态传入参数
"""

#1.导包
import rospy
#from plumbing_server_client.srv import AddInts,AddIntsRequest,AddIntsResponse
from plumbing_server_client.srv import *

if __name__ == "__main__":
    #判断参数长度
    if len(sys.argc) !=3:
        rospy.logerr("传入的参数个数不对")
        sys.exit(1)

    #2.初始化ROS节点
    rospy.init_node("erBao")
    #3.创建客户端对象
    client=rospy.ServiceProxy("addInts",AddInts)
    #4.组织请求的数据并发送请求并处理响应
    #解析传入的参数
    num1=int(sys.argv[1])
    num2=int(sys.argv[2])
    response=client.call(num1,num2)
    rospy.loginfo("响应的数据:%d",response.sum)