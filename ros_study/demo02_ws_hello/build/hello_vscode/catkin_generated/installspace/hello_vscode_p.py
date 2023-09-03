#0.指定解释器
#! /usr/bin/env python

#1.导包
import rospy
#2.入口
if __name__ == "__main__":
    #3.初始化ros节点
    rospy.init_node("hello_p")
    #4.输出日志
    rospy.loginfo("hello vscode by python,你好鸭!")


#一些问题：
#一、
#现象：当不配置 CMakeLists.txt 执行 python 文件抛出异常：
# /usr/bin/env:“python”：没有那个文件或目录
#原因：当前 noetic 使用的是 python3
#解决：
#   1.直接声明解释器为 python3 (不建议)
#   2.通过软链接将 python 链接到 python3 (建议):sudo ln -s /usr/bin/python3 /usr/bin/python(命令)