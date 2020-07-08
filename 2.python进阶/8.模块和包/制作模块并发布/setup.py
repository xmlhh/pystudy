#! /usr/bin/python3
#-*- coding:utf-8 -*-
"""
#文件名称：setup.txt
#编写人员：LHH
#项 目 组：系统组
#创建日期：2020/07/08
#功能描述：制作发布压缩包
#修改描述：
#备注：
"""

"""
制作发布压缩包步骤：
    1.创建setup.py文件，并设置distutils.core的setup()的信息
    2.构建模块：python3 setup.py build
    3.生成发布压缩包：python3 setup.py sdist
"""

from distutils.core import setup
from setuptools import setup, find_packages

setup(name='chat', #包名
    version='1.0.1',   #版本
    description='leon的发送和接收消息模块', #描述信息
    long_description='发送和接收消息模块', #完整描述信息
    author='leon',   #作者
    author_email='xxx@xxx.com',  #邮箱
    url='www.baidu.com', #网址
    # py_modules=[chat.server, chat.client]   #导出的模块
    packages = find_packages(),
    platforms = 'any',
)