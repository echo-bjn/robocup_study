#!/usr/bin/env python3

"""
    需求：向服务端发送请求，生成一只小乌龟
"""

import rospy
from turtlesim.srv import *

if __name__ == "__main__":
    rospy.init_node("service_call_p")
    client=rospy.ServiceProxy("/spawn",Spawn)
    request=SpawnRequest()
    request.x=2.0
    request.y=2.0
    request.theta=-1.57
    request.name="turtle3"
    client.wait_for_service()
    try:
        response=client.call(request)
        rospy.loginfo("生成乌龟的名字叫%s",response.name)
    except Exception as e:
        rospy.logerr("请求处理异常")