#! /usr/bin/python3
#-*- coding:utf-8 -*-
"""
#文件名称：oop_base_practice.py
#编写人员：LHH
#项 目 组：系统组
#创建日期：2020/07/06
#功能描述：类的继承(派生)、类的私有属性和方法、多继承
#修改描述：
#备注：
"""

repeat_num = 45

print("****************1.类的继承(派生)*****************")
"""
继承（派生）：子类继承父类，拥有父类的所有属性和方法
语法：
class B(A):
    pass
"""

class Person:

    def eat(self):
        print('吃饭')

    def sleep(self):
        print('睡觉')

    def play_doung(self):
        print('打豆豆')

class Employee(Person):

    def word(self):
        print('上班')

    def salary(self):
        print('拿薪水')

#Employee类对象调用Person的方法
xiaoming = Employee()
xiaoming.eat()
xiaoming.sleep()
xiaoming.play_doung()
xiaoming.word()
xiaoming.salary()

print("%s" % ('-' * (repeat_num - 15)))

print("%s\n" % ('-' * repeat_num))



print("****************1.类的私有属性和方法*****************")
"""
类的私有属性和方法是受保护的，子类是不能直接访问的，可通过父类的公有方法来间接访问
"""
class Staff:

    def __init__(self):
        #私有属性
        self.__id = 1001
        self.__name = '小辛'
        # 公有属性
        self.id = 1002
        self.name = '小杨'

    def word(self):
        print('上班')

    def salary(self):
        print('拿薪水')

    # 私有方法
    def __test(self):
        print('私有方法内部访问私有属性：%s %s' % (self.__id, self.__name))

    # 公有方法
    def test(self):
        print('公有方法内部访问私有属性：%s %s' % (self.__id, self.__name))


class EmployeeA(Staff):

    def demo(self):
        print('外部访问公有方法：', end= '')
        self.test()

mm = Staff()
#外部不能访问私有方法
# mm.__test()

nn = EmployeeA()
nn.demo()
print('外部访问公有属性: %s %s' % (nn.id, nn.name))

print("%s" % ('-' * (repeat_num - 15)))

print("%s\n" % ('-' * repeat_num))




print("****************3.多继承*****************")
"""

"""

print("%s" % ('-' * (repeat_num - 15)))

print("%s\n" % ('-' * repeat_num))
