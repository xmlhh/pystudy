#! /usr/bin/python3
#-*- coding:utf-8 -*-
"""
#文件名称：oop_base.py
#编写人员：LHH
#项 目 组：系统组
#创建日期：2020/07/03
#功能描述：面向对象基础(面向过程->面向对象)
#修改描述：
#备注：
"""

repeat_num = 45

print("****************1.类与对象*****************")
"""
类是模板，对象是根据模板创建出来的，比如：建房子，先设计图纸（类），再建房子（对象）
类的命名：大驼峰命名法 如：PythonLearn
    1）每个单词的首字母大写
    2）单词与单词之间没有下划线
面向对象基础语法：
    1）dir内置函数，使用dir(对象)，可以查看对象的属性/方法
    提示：__方法名__ 这种格式的方法是python的内置属性/方法
"""

#示例
# 创建类
class employee:
    """员工类"""

    def work(self):
        print('员工上班')

    def salary(self):
        print('员工拿薪水')

# 创建类的对象
staff = employee()

# 对象调用类的方法
staff.work()
staff.salary()

#创建类的多个对象，每个对象都有该类的属性和方法
staff1 = employee()
staff2 = employee()
staff3 = employee()

# 在类的外部给对象增加属性(不推荐使用)
staff.name = '小明'
staff.sex = '男'
staff.age = 20

print(staff.name, staff.sex, staff.age)

print("%s" % ('-' * (repeat_num - 15)))

# 利用self在类的方法中输出对象的属性
class employee2:
    """员工类"""

    def work(self):
        print(self.name)
        print('%s上班' % self.name)

    def salary(self):
        print('%s拿薪水' % self.name)

staff4 = employee2()
staff4.name = '小美'  # 不推荐使用，存在隐患，赋值和调用顺序会打乱
staff4.work()
staff4.salary()

print("%s\n" % ('-' * repeat_num))



print("****************2.初始化方法（类内）*****************")
"""
创建类的对象时，会自动调用类内置的初始化方法 __init__(self)
类内的所有方法，都可以使用初始化的所有属性
提示：在对象的方法内部，可以直接访问对象的属性
"""
class employee3:
    """员工类"""
    def __init__(self):
        print('__init__初始化方法')

        # 属性初始化
        self.name = '小羽'

    def work(self):
        print('%s上班' % self.name)

    def salary(self):
        print('%s拿薪水' % self.name)

# 创建对象时，会自动调用类内置的初始化方法
em3 = employee3()
print(em3)
print(em3.name)
em3.work()
em3.salary()
print("%s" % ('-' * (repeat_num - 15)))

class employee4:
    """员工类"""
    def __init__(self, name):
        print('__init__初始化方法优化')

        # 属性初始化
        self.name = name

    def work(self):
        print('%s上班' % self.name)

    def salary(self):
        print('%s拿薪水' % self.name)

# 创建对象时，会自动调用类内置的初始化方法，并传递属性的值
em4 = employee4('小张')
print(em4)
print(em4.name)
em4.work()
em4.salary()
print("%s" % ('-' * (repeat_num - 15)))

"""
类的对象销毁时，会自动调用类内置的销毁方法 __del__(self)
"""
class employee5:
    """员工类"""
    def __init__(self, name):
        print('__init__初始化方法优化')

        # 属性初始化
        self.name = name

    def work(self):
        print('%s上班' % self.name)

    def salary(self):
        print('%s拿薪水' % self.name)

# 创建对象时，会自动调用类内置的初始化方法，并传递属性的值
em5 = employee5('小张')
print(em5)
print(em5.name)
em5.work()
em5.salary()
# 销毁对象，会自动调用类内置销毁方法 __del__(self)
del em5
print("%s" % ('-' * (repeat_num - 15)))

# print输出对象变量时，不希望输出对象内存地址，而希望输出自定义的内容
# 使用类内置方法 __str__(self)
class employee6:
    """员工类"""
    def __init__(self, name):
        print('__init__初始化方法优化')

        # 属性初始化
        self.name = name

    def work(self):
        print('%s上班' % self.name)

    def salary(self):
        print('%s拿薪水' % self.name)

    def __str__(self):
        return '您好，我是%s' % self.name

# 创建对象时，会自动调用类内置的初始化方法，并传递属性的值
em6 = employee6('小李')
print(em6)
print(em6.name)
em6.work()
em6.salary()
# 销毁对象，会自动调用类内置销毁方法 __del__(self)
del em6
print("%s" % ('-' * (repeat_num - 15)))

print("%s\n" % ('-' * repeat_num))

