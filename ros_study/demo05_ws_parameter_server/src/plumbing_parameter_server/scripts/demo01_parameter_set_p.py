#! /usr/bin/env python

"""
    演示参数的新增和修改
    需求：在参数服务器中设置机器人属性、型号、半径
    实现：
        rospy.set_param()
"""

import rospy

if __name__ == "__main__":
    rospy.init_node("param_set_p")
    rospy.set_param("type_p","xiaoHuangChe")
    rospy.set_param("radius_p",0.5)
    rospy.set_param("radius_p",1.0)