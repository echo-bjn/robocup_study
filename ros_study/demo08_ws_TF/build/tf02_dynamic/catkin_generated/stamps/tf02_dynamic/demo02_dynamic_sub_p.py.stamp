#! /usr/bin/env python

"""
    订阅方实现:订阅坐标变换消息,传入被转换的坐标点,调用转换算法
    流程：
        1.导包
        2.初始化节点
        3.创建订阅对象
        4.组织被转换的坐标点
        5.转换逻辑实现,调用tf封装的算法
        6.输出结果
"""

import rospy
import tf2_ros
from tf2_geometry_msgs import tf2_geometry_msgs

if __name__ == "__main__":
    rospy.init_node("dynamic_sub_p")
    
    #创建缓存对象
    buffer=tf2_ros.Buffer()
    #创建订阅对象(将缓存传入)
    sub=tf2_ros.TransformListener(buffer)
    
    #组织被转换的坐标点
    ps=tf2_geometry_msgs.PointStamped()
    ps.header.stamp=rospy.Time()
    ps.header.frame_id="turtle1"
    ps.point.x=2.0
    ps.point.y=3.0
    ps.point.z=5.0

    #转换逻辑实现,调用tf封装的算法
    rate=rospy.Rate(10)
    while not rospy.is_shutdown():
        try:
            #转换实现
            '''
                参数1:被转换的坐标点
                参数2:目标坐标系
                返回值:转换后的坐标点

                PS:运行时存在的问题,跑出一个异常 world 不存在
                    原因:订阅数据是一个耗时操作,可能在调用transform转换函数时,
                        坐标系的相对关系还没有订阅到,因此出现异常
                    解决:
                        方案1:在调用转换函数前,执行休眠
                        方案2:进行异常处理 try语句 (建议)
            '''
            ps_out=buffer.transform(ps,"world")
            rospy.loginfo("转换后的坐标(%.2f,%.2f,%.2f),参考的坐标系:%s",
                        ps_out.point.x,
                        ps_out.point.y,
                        ps_out.point.z,
                        ps_out.header.frame_id
                        )
        except Exception as e:
            rospy.logwarn("错误提示:%s",e)
            
        rate.sleep()