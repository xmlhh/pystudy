#! /usr/bin/python3
#-*- coding:utf-8 -*-
"""
#文件名称：function_main.py
#编写人员：LHH
#项目组：研发四部Team3
#创建日期：2020/02/03
#功能描述：函数调用
#修改描述：
#备注：
"""

import func_base as base #函数基础使用模块
import func_param_and_return as pr #函数的参数和返回模块
import func_nested_call as nestcall #函数的嵌套调用模块
import func_param_and_return_advanced as pra #函数的参数和返回模块

#__pycache__ #模块的缓存目录
#该目录下的.pyc文件是模块缓存文件
#提高程序执行效率


repeat_num = 45

print("****************1.函数基础使用*****************")

"""
# 函数调用：
#     1）自身文件调用：函数名()
#     2）跨文件调用：
#         import 文件名
#         文件名.函数名()
"""
#调用func_base.py文件的九九乘法表函数
if __name__=="__main__":
    base.MultipleTable()

print("%s\n" % ('-' * repeat_num))


print("****************2.函数的参数和返回值*****************")

#求两个数的乘积
if __name__=="__main__":
    num1 = 7
    num2 = 9
    sum_ret = pr.func_sum(num1, num2)
    print('两个数求和：\n%d * %d = %d' % (num1, num2, sum_ret))

print("%s\n" % ('-' * repeat_num))


print("****************3.函数的嵌套调用*****************")
if __name__=="__main__":
    nest_ret = nestcall.func_3(8, 5)
    print('函数嵌套调用计算结果：\n%.02f' % nest_ret)

print("%s\n" % ('-' * repeat_num))


print("****************4.函数的参数和返回值进阶*****************")


print("%s\n" % ('-' * repeat_num))

