#! /usr/bin/python3
#-*- coding:utf-8 -*-
"""
#文件名称：func_nested_call.py
#编写人员：LHH
#项目组：研发四部Team3
#创建日期：2020/02/03
#功能描述：函数的嵌套调用
#修改描述：
#备注：
"""

"""
定义多个函数：函数1，函数2，函数3
函数3调用函数2，函数2调用函数1
"""
#案例1.复合计算：求(a + b) * (c / d)的结果

def func_1(a, b):
    ret = a + b
    return ret

def func_2(c, d):
    ret = c / d
    ret *= func_1(c * d, c + d)
    return ret

def func_3(e, f):
    ret = func_2(e, f)
    return ret

if __name__=="__main__":
    ret = func_3(6, 3)
    print('函数的嵌套调用', ret)