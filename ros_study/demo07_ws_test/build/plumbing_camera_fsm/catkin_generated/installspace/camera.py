#!/usr/bin/env python3

import rospy
import cv2 as cv
#ROS传输图片信息库
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

if __name__ == "__main__":
   
    rospy.init_node("camera_node")  
    pub=rospy.Publisher("image",Image,queue_size=10)
    
    rate=rospy.Rate(10)
    
    bridge=CvBridge()
    #读取笔记本前置摄像头
    video=cv.VideoCapture(0)

    while not rospy.is_shutdown():
        #img为截取的摄像头视频的一帧一帧图像
        ret,img=video.read()
        #摄像头是和人对立的，将图像左右调换回来正常显示。
        img=cv.flip(img, 1)
        cv.imshow("camera_node",img)
        cv.waitKey(30)
        #bridge.cv2_to_imgmsg(img,"bgr8")转换格式(cv2->imgmsg)
        msg=bridge.cv2_to_imgmsg(img,"bgr8")
        pub.publish(msg)
        rate.sleep()