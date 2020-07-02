#! /usr/bin/python3
#-*- coding:utf-8 -*-
"""
#文件名称：dictionary_base.py
#编写人员：LHH
#项目组：系统组
#创建日期：2020/07/02
#功能描述：字典的定义与基本操作
#修改描述：
#备注：
"""

repeat_num = 45

print("****************1.字典的定义*****************")
"""
# 列表是有序的对象集合，输出是有序的
# 字典是无序的对象集合，输出是无序的
# 字典：
#     字典使用键值对(key-value)存储数据，多个键值对之间用逗号，分隔；
#     key是索引；
#     value是数据；
#     键和值之间用冒号:分隔；
#     键必须唯一；
#     键只能使用字符串、数字或元祖，
#     值可以是任何数据类型
# 字典格式：
# dict = {'key1': 'value1', 'key2': value2, 'key3': value3}
"""

stu1_dict = {'name': '张三',
        'sex': 'male',
        'gender': True,
        'age': 19,
        'height': 1.75,
        'weight': 62}
print(stu1_dict)

print("%s\n" % ('-' * repeat_num))


print("****************2.字典的基本操作*****************")

#查找
name = stu1_dict['name']
#id = stu1_dict['id']
print('名字：%s' % name)
#增加
stu1_dict['id'] = '0001'
#修改
stu1_dict['sex'] = 'female'
stu1_dict['age'] = 20
print('修改后：', stu1_dict)
#删除
stu1_dict.pop('id')
#stu1_dict.pop('name')
print('删除后：', stu1_dict)

print('字典的长度：', len(stu1_dict))

#合并字典
#注意：如果被合并的字典中包含已经存在的键值对，则会覆盖原有的键值对
tmp_dict = {'id': '0002'}
print('合并前：', stu1_dict)
stu1_dict.update(tmp_dict)
print('合并后：', stu1_dict)

#清空字典
# stu1_dict.clear()
# print(stu1_dict)

print("%s\n" % ('-' * repeat_num))


print("****************3.字典的循环遍历*****************")
#遍历字典
#变量k是每一次循环中，获取的键值对的key
stu2_dict = {'name': 'xiaoming',
        'sex': 'male',
        'gender': True,
        'id': '0001',
        'age': 18,
        'height': 1.80,
        'weight': 65}

# 遍历字典
for k in stu2_dict:
    v = stu2_dict[k]
    print('%s:\t\t\t%s' % (k, v))


key_list = []
var_list = []
# 遍历字典列表，键和值分别保存到列表中
for key, var in stu2_dict.items():
    key_list.append(key)
    var_list.append(var)
print('所有键：', key_list)
print('所有值：', var_list)

print("%s\n" % ('-' * repeat_num))


print("****************4.字典-列表组合的应用场景*****************")
#多个字典放在一个列表中，再遍历
stu_list = [stu1_dict, stu2_dict]

for stu_dict in stu_list:
    print(stu_dict)

print("%s\n" % ('-' * repeat_num))
