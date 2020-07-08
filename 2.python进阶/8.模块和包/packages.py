#! /usr/bin/python3
#-*- coding:utf-8 -*-
"""
#文件名称：packages.py
#编写人员：LHH
#项 目 组：系统组
#创建日期：2020/07/08
#功能描述：包
#修改描述：
#备注：
"""


repeat_num = 45


"""
包的概念： 包含多个模块的特殊目录， 目录下有一个特殊文件 __init__.py
包的命名方式： 和变量名一致， 小写字母+_
包的优点： 使用import导入包，可以一次性导入所有模块 

注意： 外部要使用包中的模块， 需要在  __init__.py 文件中指定对外界提供的模块列表
如：从当前目录导入模块列表
from . import 模块1
from . import 模块2
"""


#案例：请看chat目录
'''
新建一个python包: chat包目录， 创建Python Package会默认生成 __init__.py 空文件
在 chat包 目录下， 新建一个 server.py 文件并定义 send() 方法
在 chat包 目录下， 新建一个 client.py 文件并定义 recv() 方法
在外部导入 chat 包
'''
#此处导入chat包
import chat

#调用包内模块的方法
chat.server.send_msg('哈喽， 您好！')
msg = chat.client.recv_msg()
print(msg)

print("%s\n" % ('-' * repeat_num))
