#! /usr/bin/python3
#-*- coding:utf-8 -*-
"""
#文件名称：exception.py
#编写人员：LHH
#项 目 组：系统组
#创建日期：2020/07/07
#功能描述：异常
#修改描述：
#备注：
"""

repeat_num = 45
"""
异常：
1.异常的概念： 程序运行时停止执行并提示错误信息， 称之为抛出异常
2.捕获异常： 
3.异常的传递：
4.自定义异常：
"""

print("****************1.简单的捕获异常*****************")
"""
开发中，如果对某些代码的执行不能确定是否正确， 用try()来捕获异常
简单的语法格式：
try:
    执行的代码块    
except:
    异常处理
"""
is_ok = True
while True:
    #简单的捕获异常并处理
    try:
        num = int(input('请输入数字： '))
        is_ok = True
    except:
        print('您的输入有误，请重新输入数字！')
        is_ok = False

    if not is_ok:
        continue
    else:
        break

print("%s" % ('-' * (repeat_num - 15)))



print("****************2.根据错误类型捕获异常*****************")
"""
针对不同类型的异常，做出不同的响应， 这个时候就需要捕获错误类型
语法：
try
    pass
except 错误类型1：
    pass
except (错误类型2, 错误类型3)：
    pass
except Exception as result:
    print('未知错误 %s' % result)
"""


print("%s" % ('-' * (repeat_num - 15)))



print("****************3.捕获未知错误*****************")
"""

"""

print("%s" % ('-' * (repeat_num - 15)))



print("****************4.捕获异常完整语法*****************")
"""

"""

print("%s" % ('-' * (repeat_num - 15)))



print("****************5.异常的传递性*****************")
"""

"""

print("%s" % ('-' * (repeat_num - 15)))



print("****************6.应用场景案例*****************")
"""

"""

print("%s" % ('-' * (repeat_num - 15)))

print("%s\n" % ('-' * repeat_num))