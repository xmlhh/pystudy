#! /usr/bin/python3
#-*- coding:utf-8 -*-
"""
#文件名称：if-else_while_for.py
#编写人员：LHH
#项目组：系统组
#创建日期：2020/07/01
#功能描述：条件语句和循环语句
#修改描述：
#备注：
"""

repeat_num = 45

print("****************1.if条件判断语句****************")
#1）if语句基本格式：
"""
#1
# if 条件:
#     条件成立后，要做的事
#     ....
#     ....
# 以上带缩进的代码是if的代码块

#2
# if 条件:
#     条件成立后，要做的事
#     ....
# else:
#     条件不成立后，要做的事
#     ....
"""

#age = input('请输入您的年龄：') #类型是str
age = int(input('请输入您的年龄：')) #类型是int
if age >= 18:
    print('您是成年人')
else:
    print('您是未成年人')


#2）逻辑运算符
#三种逻辑运算：与and、或or、非not
if age >= 0 and age <= 18:
    print('未成年人')
else:
    print('成年人')

is_py = True
if not is_py:
    print('This is python.')
else:
    print('This is not python.')


#3）if语句进阶格式：if-elif-else, 嵌套if
"""
# if 条件1:
#     条件1满足执行的代码
#     ......
# elif 条件2:
#     条件2满足执行的代码
#     ......
# elif 条件3:
#     条件3满足执行的代码
#     ......
# else:
#     以上条件都不满足执行的代码
#     ......
"""

"""
# if 条件1:
#     条件1满足执行的代码
#     ......
#     if 条件2#(条件1满足的基础上):
#         条件2满足执行的代码
#         ......
#     else#(条件1满足的基础上):
#         条件2不满足执行的代码
#         ......
# else:
#     条件1不满足执行的代码
#     ......
"""
print("%s\n" % ('-' * repeat_num))

#4）综合应用--石头剪刀布

import random as rd
#rd.randint(a, b), 返回[a, b]之间的整数，包含a和b
#b必须大于a, 否则会报错

#输入玩家要出的：1-石头，2-剪刀，3-布
player = int(input('玩家请出(1-石头，2-剪刀，3-布)：\n'))
#电脑随机出
computer = rd.randint(1, 3)
if player == 1:
    type_p = "石头"
elif player == 2:
    type_p = "剪刀"
else:
    type_p = "布"

if computer == 1:
    type_c = "石头"
elif computer == 2:
    type_c = "剪刀"
else:
    type_c = "布"

print('玩家出的是：%s, 电脑出的是：%s' % (type_p, type_c))
#判断
if (player == 1 and computer == 2) \
        or (player == 2 and computer == 3) \
        or (player == 3 and computer == 1):
    print('哈哈哈，你赢了')
elif player == computer:
    print('呃呃呃，平局')
else:
    print('呜呜呜，你输了')

print("%s\n" % ('-' * repeat_num))


print("****************2.while循环语句*****************")
#1）while循环语句的基本格式
"""
#初始化计数器记录循环次数
#while 条件判断:
#    条件成立执行的代码
#    ......
#    处理计数器
#循环结束
"""

#求0-100之间的所有数字之和
count = 0
result = 0

while count <= 100:
    result += count
    count += 1
print('0-100之间所有的数字和：%d' % result)

#求0-100之间所有偶数之和
count = 0
result = 0

while count <= 100:
    if count % 2 == 0:
        result += count
    count += 1
print('0-100之间所有的偶数和：%d' % result)
print("%s\n" % ('-' * repeat_num))

#2）break和continue
#break：退出while循环
#continue：退出后面的执行，继续while循环

i = 0
while i < 10:
    if i == 3:
        break
    print(i, end='')
    i += 1
print()

j = 0
while j < 10:
    if j == 3:
        j += 1
        continue
    print(j, end='')
    j += 1
print('\n')


#3）循环嵌套
"""
# while 条件1
#     条件1成立执行
#     ......
#     while 条件2（条件1成立的前提）
#         条件2成立执行
#         ......
#     计数器1
# 循环结束
"""

#案例1.打印6行小星星，第1行一个*,....第6行6个*
print('案例1：打印6行小星星，第1行一个*,....第6行6个*')
#方法一
star_row = 0
while star_row <= 5:
    star_col = 0
    while star_col <= star_row:
        print('*', end='')
        star_col += 1
    print('')
    star_row += 1
print()
#方法二
star = 0
while star <= 5:
    print('*' * (star + 1))
    star += 1
print('\n')

#案例2.打印九九乘法表
#转义字符：\t制表符、\n换行符
print('案例2：九九乘法表：')
row = 1
while row <= 9:
    col = 1
    while col <= row:
        print('%d * %d = %d\t' % (col, row, col * row), end='')
        col += 1
    print('')
    row += 1
print("%s\n" % ('-' * repeat_num))




print("****************3.for循环语句*****************")
#在4.高级变量类型：列表中详细说明
print("%s\n" % ('-' * repeat_num))


