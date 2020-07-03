#! /usr/bin/python3
#-*- coding:utf-8 -*-
"""
#文件名称：data_type_public_method.py
#编写人员：LHH
#项目组：系统组
#创建日期：2020/07/03
#功能描述：高级数据类型：字符串、列表、元祖、字典的公共方法
#修改描述：
#备注：
"""


repeat_num = 45

print("****************1.高级数据类型的公共方法*****************")
"""
# 1）len(item) 获取容器中元素的个数
# 2）del(item) 删除变量
# 3）max(item) 获取容器中元素的最大值
# 4）min(item) 获取容器中元素的最小值
# 字符串比较规则：'0' < 'A' < 'a'
"""
list = [1, 2, 3, 4, 5]
print('list元素：\t\t%s' % list)
print('长度/个数：\t\t%d' % len(list))

del list[0]
print('删除第1个元素：\t%s' % list)
del(list[0])
print('删除第1个元素：\t%s' % list)
del list


num_list = [1, 2, 3, 4, 5, 9, 8, 7, 6]
num_tuple = (1, 2, 3, 4, 5, 9, 8, 7, 6)
str = 'asdfgHJKLA'
dict = {'a':'x', 'y':'z', 'b':'w'}

print('min(list) 获取num_list列表中最小的值：\t%d' % min(num_list))
print('max(tuple) 获取num_tuple元祖中最大的值：\t%d' % max(num_tuple))

print('min(str) 获取str字符串中最小的字符：\t%s' % min(str))
print('max(str) 获取str字符串中最大的字符：\t%s' % max(str))

print('min(dict) 获取dict字典中最小的key值：\t%s' % min(dict))
print('max(dict) 获取dict字典中最大的key值：\t%s' % max(dict))

print("%s\n" % ('-' * repeat_num))



print("****************2.高级数据类型的切片*****************")
"""
切片：
    适用于字符串、列表、元祖，不能对字典切片
    格式：字符串[开始索引:结束索引:步长]
    顺序：0、1、2、...n
    倒序：-n、-n+1、... -2、-1
    左闭右开
    开始索引、结束索引、数字均可省略，冒号:不能省略
"""
print('#见string_base.py中的字符串切片')

print("%s\n" % ('-' * repeat_num))



print("****************3.算数运算符对比列表追加方法*****************")
"""
算数运算符：+、*，只适用于字符串、列表、元祖，不适用于字典
列表追加：
    list.extend(列表)
    list.append(元素)
    list.append(列表)
"""
num_list_1 = [1, 2, 3]
num_list_2 = [4, 5 ,6]

num_tuple_1 = (1, 2, 3)
num_tuple_2 = (4, 5 ,6)

print('列表拼接[1, 2, 3] + [4, 5 ,6]: \t%s' % (num_list_1 + num_list_2))
print('元祖拼接(1, 2, 3) + (4, 5 ,6): \t', (num_tuple_1 + num_tuple_2))

print('列表拼接[1, 2, 3] * 2: \t\t\t%s' % (num_list_1 * 2))
print('元祖拼接(4, 5 ,6) * 2 : \t\t\t', (num_tuple_2 * 2))

list = [12, 57]
print('list: \t\t\t\t\t', list)
print('num_list: \t\t\t\t', num_list)
num_list.extend(list)
print('num_list.extend(list)：\t', num_list)
num_list.append(list)
print('num_list.append(list)：\t', num_list)
del num_list[-1:]
print('del num_list[-1:]：\t\t', num_list)

print("%s\n" % ('-' * repeat_num))



print("****************4.完整的for循环语句for-else*****************")
"""
# for 元素 in 集合:
#     ......
# else:
#     for块内没有break退出循环时，会执行的代码
#     ......
"""
for item in num_list:
    if item == 7:
       break
    print(item, end=' ')
else:
    print('\nfor循环遍历没有通过break退出循环时，才会执行，否则不执行')
print()

############for-else的应用场景####################
#定义字典
stu1_dict = {'name': 'zhangsan',
        'id': '0001'}

stu2_dict = {'name': 'xiaoming',
        'id': '0002'}

print('字典1：', stu1_dict)
print('字典2：', stu2_dict)

#多个字典放在一个列表中
stu_list = [stu1_dict, stu2_dict]
print('列表：', stu_list)

#遍历列表
find_name = 'wangwu'
for stu_dict in stu_list:
    if stu_dict['name'] == find_name:
        print('找到了: %s' % find_name)
        break
    print(stu_dict)
else: #搜索字典列表，没有搜索到后，给出一个统一的提示
    print('没有找到: %s' % find_name)
print()

print("%s\n" % ('-' * repeat_num))

