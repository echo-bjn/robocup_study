#!/usr/bin/env python3

"""
    修改乌龟GUI的背景颜色参数
"""

import rospy

if __name__ == "__main__":
    rospy.init_node("change_bgColor_p")
    rospy.set_param("/turtlesim/background_r",100)
    rospy.set_param("/turtlesim/background_g",200)
    rospy.set_param("/turtlesim/background_b",0)