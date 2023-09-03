#!/usr/bin/env python3

import rospy
import cv2 as cv
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

def do_img(msg):
    bridge=CvBridge()
    #bridge.imgmsg_to_cv2(msg,"bgr8")转换格式(imgmsg->cv2)
    img=bridge.imgmsg_to_cv2(msg,"bgr8") 

    gray=cv.cvtColor(img,cv.COLOR_RGB2GRAY)
    #直接用cv.canny导出格式更方便
    edge=cv.Canny(gray,100,200)

    cv.imshow("fsm_node",edge)
    cv.waitKey(30) 

if __name__ == "__main__":
    rospy.init_node("fsm_node")
    sub=rospy.Subscriber("image",Image,do_img,queue_size=10)
    rospy.spin()