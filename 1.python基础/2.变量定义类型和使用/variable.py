#! /usr/bin/python3
#-*- coding:utf-8 -*-
"""
#文件名称：variable.py
#编写人员：LHH
#项目组：系统组
#创建日期：2020/07/01
#功能描述：python变量
#修改描述：
#备注：
"""

repeat_num = 45

print("****************1.变量的定义、使用、类型****************")
username = "n013543"
passwd = "admin"

print("用户名：", username)
print("密  码：", passwd)


#例子1：变量的定义和使用
#1）定义物品的单价（元）
_price = 3.5
#2）选择物品的个数或重量
_num = 8
#3）计算物品的总价（元）
_total = _price * _num
print('物品的总价：', _total)
#4)优惠3元
_total -= 3
print('付款的金额：', _total)

print("%s\n" % ('-' * repeat_num))


#例子2：变量的类型
"""
数据类型：数字型和非数字型
1.数字型：int/float/bool/complex(复数型)
    复数型：主要用于科学计算，如：平面场问题、波动问题、电容电感问题
2.非数字型：字符串、列表、元祖、字典

查看数据类型方式：
1.调试时，可在控制台查看数据类型
2.type函数查看数据类型
"""

name = "张三"       #str   类型
gender = True       #bool  类型
age = 19            #int   类型
height = 1.83       #float 类型
weight = 65         #int   类型
print('姓名:%s, 性别:%s, 年龄:%d, 身高:%f, 体重:%f' % (name, gender, age, height, weight))
print(type(name), type(gender), type(age), type(height), type(weight))

print("%s\n" % ('-' * repeat_num))


print("\n****************2.变量的计算和输入输出****************")
#-------------------1.不同类型变量之间的计算-------------------
#1）数字型变量之间直接计算：
#   如果变量为bool类型，在计算时：True对应的数字是1，False对应的数字是0
i = 9
f = 10.5
b = True
# i + f = 19.5, i + b = 9 + 1 = 10, f + b = 11.5

#2)字符串变量之间用 + 拼接字符串
first_name = "张"
last_name = "三"
print(first_name + last_name)
print(last_name + first_name)

#3)字符串变量和整数结合，使用*重复拼接相同的字符串
num = 10
repeat = "loveMR" * num #重复拼接10个loveMR
print(repeat)
print(first_name * num)
print(last_name * num)
print((first_name + last_name) * num)

#数字和字符串拼接: 字符串数字
joint1 = first_name + "10"
print(joint1)
joint2 = first_name + str(num)
print(joint2)

print("%s\n" % ('-' * repeat_num))

#-------------------2.变量的输入输出-------------------
#1)变量输入，用input函数
user_id = input('请输入您的账号(纯数字)：\n')
print('您输入的账号是：', user_id)

#2)类型转换函数int/float: 字符串转数字
print(int(user_id), type(user_id), type(int(user_id)))
print(float(user_id))
print(int('123'), type(int('123')))
print(float('123'), type(float('123')))
print("%s\n" % ('-' * repeat_num))

"""
#案例1：
#1.输入苹果的单价
#2.输入苹果的重量
#3.计算支付的总金额
"""
apple_price = input("请输入苹果的单价：\n")
apple_weight = input("请输入苹果的重量：\n")
price = float(apple_price)
weight = float(apple_weight)
total_amount = price * weight
print('总金额：', total_amount)
print("%s\n" % ('-' * repeat_num))

#3)变量的格式化输出
print("\n********变量的格式化输出********")
#输出格式：苹果单价xxx元/斤，购买了xxx斤，需要支付xxx元
#%s:字符串
#%d:整数
#%f:浮点数，%.02f表示只显示两位小数点
#%%:输出%
print("苹果单价%.02f元/斤，购买了%.02f斤，需要支付%.02f元" % (price, weight, total_amount))
student1_no = 9
print('学号：%06d' % student1_no)
student2_no = 123456789
print('学号：%06d' % student2_no)
scale = 0.76
print('数据比例是：%.2f%%, ' % scale * 100)
print()
print('数据比例是：%.2f%%' % (scale * 100))
print("%s\n" % ('-' * repeat_num))


#4)输出不换行 end=''
print('输出不换行', end='')
print('输出换行')
print("%s\n" % ('-' * repeat_num))


print("\n****************3.变量的命名规则**********************")
"""
变量命名：由字幕、数字、下划线组成
1.开头不允许有数字
2.不允许使用关键字
    关键字：keyword包
3.区分大小写

4.如果变量名需要多个单词组成时，按以下方式命名：
    1）每个单词都是用小写字母
    2）单词与单词之间用下划线连接，
    如：user_id, first_name, qq_number

5.驼峰命名法：
    1）小驼峰命名法：如firstName, lastName
    2）大驼峰命名法：如FirstName, LastName
"""
#关键字
import keyword
print(keyword.kwlist)
#['False', 'None', 'True', 'and', 'as', 'assert', 'async',
# 'await', 'break', 'class', 'continue', 'def', 'del', 'elif',
# 'else', 'except', 'finally', 'for', 'from', 'global', 'if',
# 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or',
# 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']




