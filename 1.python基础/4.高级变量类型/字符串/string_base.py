#! /usr/bin/python3
#-*- coding:utf-8 -*-
"""
#文件名称：string_base.py
#编写人员：LHH
#项目组：系统组
#创建日期：2020/07/02
#功能描述：字符串的基础、基本操作、切片
#修改描述：
#备注：
"""

repeat_num = 45

print("****************1.字符串的基础*****************")
"""
字符串的定义：
    可以使用双引号""，单引号''定义一个字符串；
    如果字符串内部需要使用", 则可用''定义字符串；
    如果字符串内部需要使用', 则可用""定义字符串；
    区分大小写
"""
str1 = "hello python"
str2 = '我的名字是 "LHH"'
print(str1)
print(str2)
print(str2[7])

print('遍历字符串，单个字符输出：')
for ch in str2:
    print(ch)

print("%s\n" % ('-' * repeat_num))


print("****************2.字符串的基本操作*****************")

#1）统计
print('str1字符串的长度：\t', len(str1))
print('str2字符串的长度：\t', len(str2))
print('HH在字符串的次数：\t', str2.count('HH'))
print('HH在字符串中的位置：\t', str2.index('HH'))
# 注意，使用index方法，如果传递的字符或字符串不存在，会报错
# print('HH在字符串中的位置：\t', str2.index('Hi'))

#2）判断方法
str_space = '    \t\n\r'
print('判断是否是空白字符：\t', str_space.isspace())

#以下三个方法都不能判断小数
num_str = "1.1"
#unicode 字符串
# num_str = "\u00b2"
#中文数字
# num_str = "二零二零"
print(num_str)
print(num_str.isdecimal())
print(num_str.isdigit())
print(num_str.isnumeric())

#3）字符串的查找和替换
#index方法，如果指定的字符串不存在，会报错
#find方法，如果指定的字符串不存在，会返回-1；如存在，则返回开始的索引
print('index: \t', str2.index('HH'))
print('find: \t', str2.find('HH'))
print('find: \t', str2.find('hh'))

print('替换：\t', str2.replace('LHH', 'PYTHON'))
print("%s\n" % ('-' * repeat_num))

#4）文本对齐和去空白字符
tang_poem = ['          唐伯虎点秋香',
             '   周星驰        ',
             '      别人笑我太疯癫;',
             '  我笑他人看不穿。',
             '         不见武陵豪杰墓;          ',
             '     无花无酒锄作田。  ']

for str_poem in tang_poem:
    #print(str_poem.lstrip())    #去左边空白字符
    #print(str_poem.rstrip())    #去右边空白字符
    #print(str_poem.strip())     #去两边空白字符
    str_poem = str_poem.strip()
    # print('|\t%s\t\t|' % str_poem.center(10, ' '))  #半角空格
    print('|\t%s\t|' % str_poem.center(10, '　'))   #全角空格
    # print('|%s|' % str_poem.ljust(10, '　'))
    # print('|%s|' % str_poem.rjust(10, '　'))
print("%s\n" % ('-' * repeat_num))

#5）拆分和拼接
string_poem = '\t\n 登鹳雀楼 \t \n   &&王之涣\t白日依山尽； \n\n    \t黄河入海流。\t\t\t欲穷千里目；\t  更上一层楼。\t\t\n'
print(string_poem)

poem_list = string_poem.split()  #split()默认以\t、\r、\n、空格分割字符串
print('字符串默认分割得到的列表：\n%s\n' % poem_list)

# poem_list = string_poem.split('&&')
# print('字符串按&&分割得到的列表：\n%s\n' % poem_list)

string_poem_ret = '|'.join(poem_list)
print('列表+"|"合并得到的字符串：\n%s\n' % string_poem_ret)

string_poem_ret = string_poem_ret.split('&&')
print('字符串按&&分割得到的列表：\n%s\n' % string_poem_ret)

string_poem_ret = ''.join(string_poem_ret)
print('列表合并得到的字符串：\n%s\n' % string_poem_ret)

print("%s\n" % ('-' * repeat_num))



print("****************3.字符串的切片*****************")
"""
切片：
    适用于字符串、列表、元祖，不能对字典切片
    格式：字符串[开始索引:结束索引:步长]
    顺序：0、1、2、...n
    倒序：-n、-n+1、... -2、-1
    左闭右开
    开始索引、结束索引、数字均可省略，冒号:不能省略
"""

num_str = "0123456789"

#截取完整字符串
print('完整字符串[:]: \t\t%s' % num_str[:])

#截取从2到5位置的字符串
print('[2-5]: \t\t\t\t%s' % num_str[2:6])
print('[2-5): \t\t\t\t%s' % num_str[2:5])
print('(2-5]: \t\t\t\t%s' % num_str[3:6])
print('(2-5): \t\t\t\t%s' % num_str[3:5])

#截取从开始到5位置的字符串
print('从开始到5，[:6]: \t\t%s' % num_str[:6])

#截取从2到末尾的字符串
print('从2到末尾，[2:]: \t\t%s' % num_str[2:])
#截取从2到末尾-1的字符串
print('从2到末尾-1，[2:-1): \t%s' % num_str[2:-1])

#从开始位置，每隔一个字符截取
print('间隔一个字符，[::2]: \t%s' % num_str[::2])
#从索引1开始，每隔一个字符截取
print('间隔一个字符，[1::2]: \t%s' % num_str[1::2])

#截取字符串末尾3个字符串
print('末尾3个字符串，[:]: \t%s' % num_str[-3:])

#字符串的逆序
print('逆序：\t\t\t\t%s' % num_str[-1::-1])
print('逆序：\t\t\t\t%s' % num_str[::-1])

print("%s\n" % ('-' * repeat_num))

