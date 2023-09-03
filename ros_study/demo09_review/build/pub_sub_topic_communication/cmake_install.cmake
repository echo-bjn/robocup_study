# Install script for directory: /home/robocup/Documents/ros_study/demo09_review/src/pub_sub_topic_communication

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/robocup/Documents/ros_study/demo09_review/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

# Set default install directory permissions.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "/usr/bin/objdump")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/pub_sub_topic_communication/msg" TYPE FILE FILES "/home/robocup/Documents/ros_study/demo09_review/src/pub_sub_topic_communication/msg/Person.msg")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/pub_sub_topic_communication/cmake" TYPE FILE FILES "/home/robocup/Documents/ros_study/demo09_review/build/pub_sub_topic_communication/catkin_generated/installspace/pub_sub_topic_communication-msg-paths.cmake")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/robocup/Documents/ros_study/demo09_review/devel/include/pub_sub_topic_communication")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/robocup/Documents/ros_study/demo09_review/devel/share/roseus/ros/pub_sub_topic_communication")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/robocup/Documents/ros_study/demo09_review/devel/share/common-lisp/ros/pub_sub_topic_communication")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/robocup/Documents/ros_study/demo09_review/devel/share/gennodejs/ros/pub_sub_topic_communication")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/home/robocup/anaconda3/bin/python3" -m compileall "/home/robocup/Documents/ros_study/demo09_review/devel/lib/python3/dist-packages/pub_sub_topic_communication")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages" TYPE DIRECTORY FILES "/home/robocup/Documents/ros_study/demo09_review/devel/lib/python3/dist-packages/pub_sub_topic_communication")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/robocup/Documents/ros_study/demo09_review/build/pub_sub_topic_communication/catkin_generated/installspace/pub_sub_topic_communication.pc")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/pub_sub_topic_communication/cmake" TYPE FILE FILES "/home/robocup/Documents/ros_study/demo09_review/build/pub_sub_topic_communication/catkin_generated/installspace/pub_sub_topic_communication-msg-extras.cmake")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/pub_sub_topic_communication/cmake" TYPE FILE FILES
    "/home/robocup/Documents/ros_study/demo09_review/build/pub_sub_topic_communication/catkin_generated/installspace/pub_sub_topic_communicationConfig.cmake"
    "/home/robocup/Documents/ros_study/demo09_review/build/pub_sub_topic_communication/catkin_generated/installspace/pub_sub_topic_communicationConfig-version.cmake"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/pub_sub_topic_communication" TYPE FILE FILES "/home/robocup/Documents/ros_study/demo09_review/src/pub_sub_topic_communication/package.xml")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pub_sub_topic_communication" TYPE PROGRAM FILES "/home/robocup/Documents/ros_study/demo09_review/build/pub_sub_topic_communication/catkin_generated/installspace/pub.py")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pub_sub_topic_communication" TYPE PROGRAM FILES "/home/robocup/Documents/ros_study/demo09_review/build/pub_sub_topic_communication/catkin_generated/installspace/sub.py")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pub_sub_topic_communication" TYPE PROGRAM FILES "/home/robocup/Documents/ros_study/demo09_review/build/pub_sub_topic_communication/catkin_generated/installspace/pub_a.py")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pub_sub_topic_communication" TYPE PROGRAM FILES "/home/robocup/Documents/ros_study/demo09_review/build/pub_sub_topic_communication/catkin_generated/installspace/sub_a.py")
endif()

