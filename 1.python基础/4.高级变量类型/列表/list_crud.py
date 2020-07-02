#! /usr/bin/python3
#-*- coding:utf-8 -*-
"""
#文件名称：list_crud.py
#编写人员：LHH
#项目组：系统组
#创建日期：2020/07/02
#功能描述：列表的基本操作：增删改查crud和循环遍历
#修改描述：
#备注：
"""

"""
#数据类型：数字型和非数字型
#数字型：  整型、浮点型、布尔型、复数型
#非数字型：字符串、列表、元祖、字典
"""

repeat_num = 45

print("****************1.列表的基础操作*****************")

"""
# 列表[]：
#   格式：name_list = ['name1', 'name2', 'name2', ...]
#   索引（下标）从0开始
# python可以在列表中存储不同类型的数据
# 开发中尽量存储同类型的数据
"""

#定义列表
name_list = ['张三', '李四', '王五']
name_id = ['001', '002', '003']

#列表的增删改查
if __name__=="__main__":
    print('原型：\t', name_list)        #输出列表全部内容
    print('取值：\t', name_list[2])     # 取值（索引取值）
    print('取索引：\t', name_list.index('王五'))

    '''增加'''
    #末尾追加
    name_list.append('赵六')
    print('末尾追加：\t\t', name_list)
    #索引0位置插入
    name_list.insert(0, '痳七')
    print('在0的位置插入：\t', name_list)
    #在列表name_list追加列表name_id
    name_list.extend(name_id)
    print('追加列表：\t\t', name_list)

    #修改指定索引的内容
    name_list[3] = '王小二'
    print('修改索引3的内容：\t', name_list)

    '''删除'''
    #删除末尾的内容
    name_list.pop()
    print('末尾删除：\t\t', name_list)
    # 删除指定索引的内容
    name_list.pop(0)
    print('删除0位置的内容：\t', name_list)
    #删除指定数据
    name_list.remove('001')
    print('删除内容001：\t\t', name_list)
    #del关键字本质上是将一个变量从内存中删除
    #删除关键字del
    del name_list[4]
    print('del删除关键字：\t', name_list)

    #列表的长度
    lenght = len(name_list)
    print('长度：\t', lenght)

    #'张三'在列表中出现的次数
    times = name_list.count('张三')
    print('统计在列表中出现的次数：\t', times)

    '''排序'''
    #升序
    name_list.sort()
    print('升序：\t', name_list)
    #降序
    name_list.sort(reverse=True)
    print('降序：\t', name_list)
    #逆序（反转）
    name_list.reverse()
    print('反转：\t', name_list)

print("%s\n" % ('-' * repeat_num))


print("****************2.列表的for循环遍历*****************")

"""
# 循环遍历格式：
#     for 变量 in 列表:
#         print(变量)
"""

name_list = ['张三', '李四', '王五']
id_list = ['001', '002', '003']

#列表的循环遍历
if __name__=="__main__":
    print(id_list)
    print(name_list)

    for id in id_list:
        print('%s ' % id, end='')
    print('')

    for name in name_list:
        print('%s ' % name, end='')
    print('')

print("%s\n" % ('-' * repeat_num))

