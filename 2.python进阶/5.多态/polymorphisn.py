#! /usr/bin/python3
#-*- coding:utf-8 -*-
"""
#文件名称：polymorphisn.py
#编写人员：LHH
#项 目 组：系统组
#创建日期：2020/07/04
#功能描述：多态
#修改描述：
#备注：
"""

repeat_num = 45

print("****************1.多态*****************")
"""
面向对象的三大特性：
封装：将属性和方法封装到一个抽象类中，可选择不公开(私有)和公开(公有)
继承：实现代码的重用，相同代码不需要重复编写
多态：不同的子类对象调用相同的父类方法，产生不同的执行结果，以继承和重写父类方法为前提，多态可以增加代码的灵活度
"""
class Dog(object):

    def __init__(self, name):
        self.name = name

    def play(self):
        print('%s 挠痒痒' % self.name)

class WhiteDog(Dog):

    def play(self):
        print('%s 愉快的玩耍' % self.name)

class Human(object):

    def __init__(self, name):
        self.name = name

    def play_with_dog(self, dog):
        print('%s 出门遛 %s' % (self.name, dog.name))
        #调用paly()方法，通过对象来决定调用哪个类的play()方法
        dog.play()

# xiaobai = Dog('小黑')
xiaobai = WhiteDog('小白')
#使用以上两个类对象的同一个方法，执行结果不一样
zhuren = Human('主人')
zhuren.play_with_dog(xiaobai)

print("%s\n" % ('-' * repeat_num))

