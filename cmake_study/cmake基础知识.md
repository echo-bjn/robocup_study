# CMake说明

CMake定义：高级编译配置工具

当多个人用不同的语言或者编译器开发一个项目，最终要输出一个可执行文件或者共享库(dll,so等等) 这时候就出现了CMake这个神器

所有操作都是通过编译CMakeLists.txt来完成的

绝大多数的linux系统都已经安装了CMake





# CMake写一个HelloWorld

【1】步骤一，自己创建一个新目录，然后cd到这个目录下，写一个helloworld (main.cpp)

```
首先 
vim main.cpp 

然后
#include<iostream>

int main(){
std::cout<<"hello,world"<<std::endl;
}
```

【2】步骤二，写一个CMakeLists.txt(注意这个文件名大小写不能变)

```
首先
vim CMakeLists.txt

然后
PROJECT (HELLO)
SET(SRC_LIST main.cpp)
MESSAGE(STATUS "This is BINARY dir" ${HELLO_BINARY_DIR})
MESSAGE(STATUS "This is SOURCE dir" ${HELLO_SOURCE_DIR})
ADD_EXECUTABLE(hello ${SRC_LIST})
```

【3】步骤三，使用cmake，生成makefile文件

```
cmake .
```

输出后目录下就生成了这些文件——CMakeFiles，CMakeCache.txt,cmake_install.cmake等文件，并且生成了Makefile

【4】步骤四，使用make命令编译

```
make
```

【5】最终生成了hello的可执行程序





# cmake语法



#### PROJECT关键字

可以用来指定工程的名字和支持的语言，默认支持所有的语言

PROJECT (HELLO) 指定了工程的名字，并且支持所有语言

PROJECT (HELLO CXX) 指定了工程的名字，并且支持语言是C++

PROJECT (HELLO C CXX) 指定了工程的名字，并且支持语言是C和C++



该式隐式定义了两个CMAKE的变量

<projectname>_BINARY_DIR,本例中是HELLO_BINARY_DIR

<projectname>_SOURCE_DIR,本例中是HELLO_SOURCE_DIR

MESSAGE关键字就可以直接使用这两个变量，当前都指向当前的工作目录

问题：如果更改了工程名，这两个变量名也会变

解决：又定义两个预定义变量： PROJECT_BINARY_DIR和PROJECT_SOURCE_DIR,这两个变量和HELLO_BINARY_DIR和HELLO_BINARY_DIR是一致的



#### SET关键字

用来显示指定变量的

SET(SRC_LIST main.cpp)      SRC_LIST变量就包含了main.cpp

也可以SET(SRC_LIST main.cpp t1.cpp t2.cpp)       这是在需要输出多个cpp文件的时候用到的

 

#### MESSAGE关键字

向终端输出用户自定义的信息

主要包含三种信息：
【1】SEND_ERROR，产生错误，生成过程被跳过

【2】STATUS，输出前缀为——的信息

【3】FATAL_ERROR，立即终止所有的cmake过程



#### ADD_EXECUTABLE关键字

生成可执行文件

ADD_EXECUTABLE(hello $(SRC_LIST))   生成的可执行文件名是hello，源文件读取变量SRC_LIST中的内容

也可以直接写ADD_EXECUTABLE(hello main.cpp)



```
PROJECT(HELLO)

ADD_EXECUTABLE(hello main.cpp)
```



注意：工程名的HELLO和生成的可执行文件hello是没有任何关系的





# 语法的基本规则

【1】变量使用${}方式取值，但是在IF控制语句中是直接使用变量名

【2】指令(参数1 参数2...)参数使用括号括起，参数之间使用空格或者分号隔开。

以上面的ADD_EXECUTABLE指令为例，如果存在另外一个func.cpp源文件，就要写成：ADD_EXECUTABLE(hello main.cpp func.cpp)或者ADD_EXECUTABLE(hello main.cpp;func.cpp)

【3】指令是大小写无关的，参数和变量是大小写相关的。但是，推荐全部使用大写指令



#### 语法注意事项

【1】SET(SRC_LIST main.cpp)可以写成SET(SRC_LIST "main.cpp")，如果源文件名中含有空格，就必须要加双引号

【2】ADD_EXECUTABLE(hello main)后缀".cpp"可以不加，他会自动去找.c和.cpp，最好不要这样写，可能会有两个文件main.cpp和main





# 内部构建和外部构建

【1】上述例子就是内部构建，它产生的临时文件特别多，不方便清理

【2】外部构建，就会把生成的临时文件放在build目录下，不会对源文件有任何影响强烈使用外部构建方式

步骤：(1)建立一个build目录，可以在任何地方，建议在当前目录下

​			(2)进入build，运行cmake ..    当然..表示上级目录，你可以写CMakeLists.txt所在的绝对路径，生成的文件都在build目录下了

​			(3)在build目录下，运行make来构建工程



注意外部构建的两个变量

【1】HELLO_SOURCE_DIR 还是工程路径

【2】HELLO_BINARY_DIR 编译路径 也就是/root/cmake/build





# 让HELLO看起来更像一个工程

【1】为工程添加一个子目录src，用来放置工程源代码

【2】添加一个子目录doc，用来放置这个工程的文档hello.txt       *

【3】在工程目录添加文本文件COPYRIGHT，README       *

【4】在工程目录添加一个runhello.sh脚本，用来调用hello二进制       *

【5】将构建后的目标文件放入构建目录的bin子目录

【6】将doc目录的内容以及COPYRIGHT/README安装到/usr/share/doc/cmake/         *



#### 将目标文件放入构建目录的bin子目录

每个目录下都要有一个CMakeLists.txt说明

**·**外层CMakeLists.txt

```
PROJECT(HELLO)
ADD_SUBDIRECTORY(src bin)
```

**·**src下的CMakeLists.txt

```
ADD_EXECUTABLE(hello main.cpp)
```



#### ADD_SUBDIRECTARY指令

ADD_SUBDIRECTARY(source_dir [binary_dir] [EXCLUDE_FORM_ALL])

【1】这个指令用于向当前工程添加存放源文件的子目录，并可以指定中间二进制和目标二进制存放的位置

【2】EXCLUDE_FORM_ALL函数是将写的目录从编译器中排除，如程序中的example

【3】ADD_SUBDIRECTARY(src bin)

​         将src子目录加入工程并指定编译输出(包含编译中间结果)路径为bin目录

​	     如果不进行bin目录的指定，那么编译结果(包括中间结果)都将存放在build/src目录



#### 更改二进制的保存路径

SET指令重新定义EXECUTABLE_OUTPUT_PATH和LIBRARY_OUTPUT_PATH变量 来指定最终的目标二进制的位置

SET(EXECUTABLE_OUTPUT_PATH ${PROJECT_BINARY_DIR}/bin)

SET(LIBRARY_OUTPUT_PATH ${PROJECT_BINARY_DIR}/bin)



思考：加载哪个CMakeLists.txt当中

哪里改变目标存放路径，就在哪里加入上述的定义，所以应该在src下的CMakeLists.txt下写





# 安装

**·** 一种是从代码编译后直接make install安装

**·** 一种是打包时的指定目录安装 

​        -简单的可以这样指定目录：make install DESTDIR=/tmp/test

​        -稍微复杂一点可以这样指定目录：./configure -prefix=/usr



```
//目录树结构
指令：tree

输出
|-build                     //目录dir
|-CMakeLists.txt
|-COPYRIGHT                 //文本文件
|-doc                       //目录dir
   |-hello.txt
|-README                    //文本文件
|-runhello.sh               //脚本文件
|-src                       //目录dir
   |-CMakeLists.txt         
   |-main.cpp
   
3 directories, 7 files
```



#### 如何安装HelloWorld

使用CMAKE一个新的指令：INSTALL

​     INSTALL的安装可以包括：二进制、动态库、静态库以及文件、目录、脚本等

使用CMAKE一个新的变量：CMAKE_INSTALL_PREFIX



#### 安装文件COPYRIGHT和README

```
INSTALL(FILES COPYRIGHT README DESTINATION share/doc/cmake/)
//写在最外面的CMakeLists.txt里面
```

​	FILES:文件

​	DESTINATION:

​	1.写绝对路径

​	2.可以写相对路径，相对路径实际路径是：${CMAKE_INSTALL_PREFIX}/<DESTINATION 定义的路径>



#### 安装脚本runhello.sh

PROGRAMS：非目标文件的可执行程序安装(比如脚本之类)

```
INSTAll(PROGRAMS runhello.sh DESTINATION bin)
```

说明：实际安装到的是 /usr/bin



#### 安装doc中的hello.txt

**·** 一、是通过doc目录建立CMakeLists.txt,通过install下的file

**·** 二、是直接在工程目录通过

```
INSTALL(DIRECTORY  doc/ DESTINATION share/doc/cmake)
```



DIRECTORY后面连接的所在Source目录的相对路径

注意：abc和abc/有很大区别

​		目录名不以/结尾：这个目录将被安装为目标路径下的abc

​        目标名以/结尾：这个目录将被安装到目标路径



#### 安装过程

cmake..

make

make install
