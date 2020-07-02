#! /usr/bin/python3
#-*- coding:utf-8 -*-
"""
#文件名称：reference_local_and_global_variables.py
#编写人员：LHH
#项目组：系统组
#创建日期：2020/07/02
#功能描述：变量的引用、可变不可变类型、局部变量和全局变量（与其他语言不同，需注意）
#修改描述：
#备注：
"""

repeat_num = 45


print("****************1.变量的引用*****************")
"""
# 变量的引用
#     1）变量和数据都是保存在内存中，并且分开存储
#     数据保存在内存中的某个位置
#     变量保存数据在内存中的地址
#     变量中记录数据的地址，就叫引用
#     使用id()查看变量中数据在内存的地址
#     
#     2）调用函数传递传递的引用
#     3）函数返回值传递引用
"""
a = 1
print('变量a的值：\t\t', a)
print('变量a的地址：\t\t', id(a))

b = a
print('变量b的值：\t\t', b)
print('变量b的地址：\t\t', id(b))
print("%s" % ('-' * (repeat_num - 15)))

a = 2
print('变量a的值：\t\t', a)
print('变量a的地址：\t\t', id(a))
print('变量b的值：\t\t', b)
print('变量b的地址：\t\t', id(b))
print("%s" % ('-' * (repeat_num - 15)))


def func(num):
    print('函数内部 %d 对应的内存地址：%d' % (num, id(num)))
    ret = '返回值地址'
    print('函数内部返回数据的内存地址：%d' % id(ret))
    return ret

res = func(57)
print('函数外部返回数据的内存地址：%d' % id(res))

print("%s\n" % ('-' * repeat_num))


print("****************2.可变不可变类型*****************")
"""
# 不可变类型(内存中的数据不允许修改)：
#     数字类型：int, bool, float, complex, long(2,x)
#     字符串：str
#     元祖：tuple
#     
# 可变类型(内存中的数据允许修改)：
#     列表：list
#     字典：dict
#         字典的key只能用不可变类型
#         字典的value可以使任意类型
"""

print("%s\n" % ('-' * repeat_num))




print("****************3.局部变量和全局变量（与其他语言不同，需注意）*****************")
"""
# 局部变量：
#     生命周期：
#         在函数内部定义的变量，只能在函数内部使用，
#         函数执行结束后，局部变量被系统收回
#         不同函数内部定义相同名字的变量，互不干扰
# 全局变量：
#     在函数内部不能直接赋值和被修改，若赋值则是在函数内部定义同名的局部变量
#     函数内部修改：需要先使用global声明全局变量    
"""

g_num = 100

def func1():
    num = 1
    print('func1==> %d, %d' % (num, g_num))

def func2():
    '''不能修改全局变量'''
    num = 1
    # 此处希望修改全局变量的值
    # 在Python中，函数内部是不允许直接修改全局变量的值
    # 如果使用赋值语句，会在函数内部，定义一个局部变量
    # 如果在函数内部的局部变量名和全局变量名相同，则在局部变量定义之前是不能使用，
    # 因为此时的变量是没有定义的变量
    # print('func1==> %d, %d' % (num, g_num))
    g_num = num
    # 此时的g_num不是全局变量，而是函数内的局部变量
    print('func2==> %d, %d' % (num, g_num))

def func3():
    '''能修改全局变量'''
    num = 1
    # g_num = num
    global g_num
    g_num = 20
    print('func3==> %d, %d' % (num, g_num))


if __name__=="__main__":
    print('初始化的全局变量：')
    func1()
    func2()
    print('想修改却未被修改的全局变量：')
    func1()
    func3()
    print('修改后的全局变量：')
    func1()

print("%s\n" % ('-' * repeat_num))

