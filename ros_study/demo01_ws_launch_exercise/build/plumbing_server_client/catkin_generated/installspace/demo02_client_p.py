#!/usr/bin/env python3

import rospy
from plumbing_server_client.srv import *

if __name__ == "__main__":
    if len(sys.argv)!=3:
        rospy.logerr("传入的参数个数不对")
        sys.exit(1)
    rospy.init_node("heiEr")
    client=rospy.ServiceProxy("addInts",AddInts)
    num1=int(sys.argv[1])
    num2=int(sys.argv[2])
    client.wait_for_service()
    response=client.call(num1,num2)
    rospy.loginfo("响应的数据：%d",response.sum)