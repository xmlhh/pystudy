#! /usr/bin/python3
#-*- coding:utf-8 -*-
"""
#文件名称：function_base.py
#编写人员：LHH
#项目组：系统组
#创建日期：2020/07/03
#功能描述：函数
#修改描述：
#备注：
"""


repeat_num = 45

print("****************1.函数*****************")
"""
语法
Python 定义函数使用 def 关键字，一般格式如下：

def 函数名（参数列表）:
    函数体
    return [返回值]
"""

def func1():
    pass

def func2(str):
    print(str)
    return

def func3(a, b):
    sum = a + b
    return sum

#函数调用
func1()
func2('函数调用')
print('求和：', func3(5, 8))

print("%s\n" % ('-' * repeat_num))



print("****************2.函数（参数）*****************")
"""
函数参数：
    1.位置参数, 根据参数位置来确定参数, 实参和形参位置必须一致
    2.关键字参数, 根据关键字来确定参数, 在使用关键字参数调用时, 可以任意调换参数传参的位置。
    3.默认参数：
        def 函数名(...，形参名，形参名=默认值)：
            代码块
    4.可变参数和不可变参数： 在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。
"""
def func4(str1, str2):
    print("str1: ", str1)
    print("str2: ", str2)
    print()

#位置参数
print('位置参数:')
#参数个数位置不一致，导致错误
# func4('python')
# func4('python', 'c++', 'java')
func4('python', 'c++')

print("%s" % ('-' * (repeat_num - 15)))

#关键字参数
print('关键字参数:')
func4('python', str2='c++')
func4(str2='c++', str1='python')
#位置参数必须放在关键字参数之前，否则会报错
# func4(str1='python', 'c++')

print("%s" % ('-' * (repeat_num - 15)))

#默认参数
print('默认参数:')

def func5(str1, str2='go', str3='qt'):
    print("str1: ", str1)
    print("str2: ", str2)
    print("str3: ", str3)
    print()

func5('python')
func5('python', 'c++')

#这样子语法错误
# def func6(str1='c++', str2, str3):
#     pass

#python提供内置函数用于查看函数有哪些默认参数，
# “函数名.__defaults__”查看函数的默认值参数的当前值，其返回值是一个元组
print('查看函数默认参数：', func5.__defaults__)

print("%s" % ('-' * (repeat_num - 15)))

#可变参数和不可变参数
def change_string(str):
    str = 'java'
    print('函数内a的值: ', str)
    return

str = 'python'
change_string(str)
print('函数外a的值: ', str)  # 结果是 python


def change_list(mylist):
    "修改传入的列表"
    mylist.extend([1, 2, 3, 4])
    print("函数内取值: ", mylist)
    return

mlist = [10, 20, 30]
change_list(mlist)
print("函数外取值: ", mlist)

#前者change_string函数的参数相当于值传递，实参不变
#后者change_list函数的参数相当于引用传递，实参被改变


print("%s\n" % ('-' * repeat_num))



print("****************3.匿名函数(lambda表达式)*****************")
"""
lambda 表达式, 又称匿名函数, 常用来表示内部仅包含 1 行表达式的函数
lambda 表达式的语法格式如下：
    name = lambda [list] : 表达式
该语法格式转换成普通函数的形式，如下所示：
    def name(list):
        return 表达式
    name(list)
相比函数，lamba 表达式具有以下 2 个优势：
    对于单行函数，使用 lambda 表达式可以省去定义函数的过程，让代码更加简洁；
    对于不需要多次复用的函数，使用 lambda 表达式可以在用完之后立即释放，提高程序执行的性能。
"""
#普通函数
def func6(a, b):
    return a * b
print(func6(5, 8))

#lambda表达式
funclambda = lambda a, b: a * b
print(funclambda(5, 8))

print("%s\n" % ('-' * repeat_num))



print("****************4.函数返回值*****************")
"""
1.返回空值None
2.单值返回
3.多值返回, 返回的是元组
"""
#返回空值
print('返回空值: ', end='')
def func_none():
    return

res = func_none()
print(res)

#单值返回
print('单值返回: ', end='')
def func_single(str1, str2):
    return str1 + str2

res = func_single('hello ', 'python')
print(res)

#多值返回，返回的是元组
print('多值返回，返回的是元组: ', end='')
def func_single(str1, str2):
    return str1, str2

res = func_single('hello ', 'python')
print(res)

print("%s\n" % ('-' * repeat_num))