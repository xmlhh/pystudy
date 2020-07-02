#! /usr/bin/python3
# #-*- coding:utf-8 -*-
"""
#文件名称：set.py
#编写人员：LHH
#项目组：系统组
#创建日期：2020/07/02
#功能描述：集合的定义与基本操作
#修改描述：
#备注：
"""

repeat_num = 45

print("*\n***************1.集合的定义*****************")
"""
# 集合:
#     集合（set）是一个无序的不重复元素序列。
#     可以使用大括号 { } 或者 set() 函数创建集合，
#     注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典
#     dataSet = ('元素1', '元素2', '元素3',...)
"""

platform_set = {'linux', 'mac', 'linux', 'windows', 'windows', 'linux'}
print('自动去重并随机排序：', platform_set)

# 判断元素是否在集合内
flu = 'linux'
if flu in platform_set:
    print(flu + '在集合内')
else:
    print(flu + '不在集合内')


print("%s\n" % ('-' * repeat_num))


print("****************2.两个集合间的运算*****************")
set1 = set('asdfgfdsa')
set2 = set('asdcvb')
print('set1: ', set1)
print('set2: ', set2)
print('set1 - set2（获取set1中存在，而set2中没有的元素的集合）: ', set1 - set2)
print('set2 - set1（获取set2中存在，而set1中没有的元素的集合）: ', set2 - set1)
print('set1 | set2（或）: ', set1 | set2)
print('set1 & set2（与）: ', set1 & set2)
print('set1 ^ set2（异或）: ', set1 ^ set2)

print("%s\n" % ('-' * repeat_num))


print("****************3.集合的基本操作*****************")
#添加
platform_set.add('android')
print('添加单个元素: ', platform_set)

#update(x), 参数可以是列表，元组，字典等
language = ['c/c++', 'qt', 'go', 'java', 'python']
platform_set.update(language)
print('添加列表多个元素: ', platform_set)

#删除
platform_set.remove('java')
#remove 元素不存在会发生错误
# platform_set.remove('asdf')
print('删除java元素: ', platform_set)

#discard 元素不存在不会发生错误
platform_set.discard('python')
platform_set.discard('asdf')
print('删除python元素: ', platform_set)

#随机删除某个元素
platform_set.pop()
print('随机删除某个元素: ', platform_set)

#其他
length = len(platform_set)
print('长度: ', length)




print("%s\n" % ('-' * repeat_num))


