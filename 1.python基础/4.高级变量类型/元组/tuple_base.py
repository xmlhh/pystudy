#! /usr/bin/python3
# #-*- coding:utf-8 -*-
"""
#文件名称：tuple_base.py
#编写人员：LHH
#项目组：系统组
#创建日期：2020/07/02
#功能描述：元祖的定义与基本操作
#修改描述：
#备注：
"""

repeat_num = 45

print("****************1.元祖的定义*****************")
"""
# 元祖():
#     元祖的元素不能修改，其他的与列表类似
#     tuple = ('元祖1', '元祖2', '元祖3', 元组4)
#     元祖通常保存不同数据类型
"""

name_tuple = ('元祖1', '元祖2', '元祖3')

print(name_tuple)
print(name_tuple[0])
print(name_tuple[1])
print(name_tuple[2])
# print(name_tuple[3])

#空元祖
empty_tuple = ()
print('类型：', type(empty_tuple))

#整型，非元祖
single_ = (5)
print('类型：', type(single_))

#一个元素的元祖
single_tuple = (5,)
print('类型：', type(single_tuple))
print("%s\n" % ('-' * repeat_num))


print("****************2.元祖的基本操作*****************")
#定义元祖
info_tuple = ('zhangsan', 'male', 19, 1.75)

#取值和取索引
print('取值：', info_tuple[0])
print('取索引：', info_tuple.index('zhangsan'))

#长度
print('长度：', len(info_tuple))

#统计数
print('统计19出现的个数：', info_tuple.count(19))
print("%s\n" % ('-' * repeat_num))


print("****************3.元祖的应用场景*****************")
"""
# 应用场景：
#     当元祖的数据类型一致时，用for循环遍历
#     当元祖的数据类型不一致时：
#         1）元祖作为函数的参数或返回值，函数接收任意多个参数或返回多个值
#         2）格式化字符串
#         3）让列表不允许修改，保护数据安全
"""

#元祖所有同类型数据，用for循环遍历
index = 0
for var in name_tuple:
    print('%d-->%s' % (index, var))
    index += 1
print()

#元祖作为函数的参数或返回值，python高级-函数时学习
info_tuple


#元祖格式化字符串
print('元祖格式化字符串：\n姓名: %s，性别: %s，年龄: %d，身高: %.2f' % info_tuple)

#列表不允许修改，保护数据安全，元祖与列表之间的转换
#list(元祖)：元祖转为列表
#tuple(列表)：列表转为元祖

print("****************4.元祖-列表相互转换*****************")
num_list = [1, 2, 3, 4, 5]
num_tuple = (6, 7, 8, 9, 0)
print(type(num_list))
print(type(num_tuple))
print('num_list to num_tuple: ', type(tuple(num_list)))
print('num_tuple to num_list: ', type(list(num_tuple)))

print("%s\n" % ('-' * repeat_num))
