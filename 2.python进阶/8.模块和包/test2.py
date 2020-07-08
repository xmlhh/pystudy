#! /usr/bin/python3
#-*- coding:utf-8 -*-
"""
#文件名称：test2.py
#编写人员：LHH
#项 目 组：系统组
#创建日期：2020/07/08
#功能描述：模块2
#修改描述：
#备注：
"""


#全局变量
title = "模块2"

#函数
def say():
    print('Hi, 我是模块2.')

#类
class Cat(object):
    pass

#模块内部执行，外部导入不执行
if __name__ == "__main__":
    print(__name__)

    print('test2模块内部测试代码:')
    say()