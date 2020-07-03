#! /usr/bin/python3
#-*- coding:utf-8 -*-
"""
#文件名称：func_param_and_return.py
#编写人员：LHH
#项目组：研发四部Team3
#创建日期：2020/02/03
#功能描述：函数的参数和返回值
#修改描述：
#备注：
"""


"""
函数参数的使用：
    参数写在函数名后的括号里；
    多个参数之间用逗号,分隔
"""
def func_sum(num1, num2):
    result = num1 * num2
    #print('%d + %d = %d' % (num1, num2, result))
    return result

if __name__=="__main__":
    sum_ret = func_sum(5, 9)
    print('计算结果：%d' % sum_ret)

