#! /usr/bin/python3
#-*- coding:utf-8 -*-
"""
#文件名称：oop_base_practice.py
#编写人员：LHH
#项 目 组：系统组
#创建日期：2020/07/03
#功能描述：面向对象基础-练习
#修改描述：
#备注：
"""

repeat_num = 45

print("****************1.封装*****************")
"""
封装是面向对象的一大特点
将属性和方法封装到类中
在类外创建类的对象，使用对象调用类的方法
提示：在对象的方法内部，可以直接访问对象的属性
"""

# 案例
# 士兵有一把枪, 士兵可以开枪，枪能够发射子弹，枪可以装填子弹

class Gun:
    """枪类"""
    def __init__(self, model):
        '''初始化'''
        # 枪的型号
        self.model = model
        # 枪的子弹数量
        self.bullet_sum = 0

    def add_bullet(self, count):
        '''装填子弹'''
        self.bullet_sum += count

    def shoot(self):
        '''发射子弹'''
        # 判断子弹数量
        if self.bullet_sum == 0:
            print('[%s]没有子弹了，请装填子弹！' % self.model)
            return
        # 发射子弹
        self.bullet_sum -= 1
        print('[%s] 突突突... 剩余子弹[%d]' % (self.model, self.bullet_sum))


class Soldier:
    """士兵类"""
    def __init__(self, name):
        # 姓名
        self.name = name
        # 枪
        self.gun = None

    def fire(self):
        '''开枪'''
        # 判断是否有枪
        if self.gun == None:
            print('[%s] 还没有枪...' % self.name)
            return

        # 装填子弹
        self.gun.add_bullet(30)
        # 发射子弹
        self.gun.shoot()

# 创建枪对象
ak = Gun('AK47')
# ak47.add_bullet(30)
# ak47.shoot()

#创建士兵对象
soldier = Soldier('许三多')
soldier.gun = ak
soldier.fire()

print("%s" % ('-' * (repeat_num - 15)))

print("%s\n" % ('-' * repeat_num))


print("****************2.私有属性和私有方法*****************")
"""
定义属性和方法时，在属性名或方法名前增加两个下划线，如：self.__name=18; 就是私有属性
"""

class Person:

    def __init__(self, name):
        self.name = name
        # 私有属性
        self.__age = 18

    def put1(self):
        print('%s的年龄是%d' % (self.name, self.__age))

    # 私有方法
    def __put2(self):
        print('%s的年龄是%d' % (self.name, self.__age))

xiaoming = Person('小明')
xiaoming.put1()
print(xiaoming.name)

# 私有属性和方法不能直接在外部访问，如下：会提示没有该属性或方法
# print(xiaoming.__age)
# xiaoming.__put2()

# 事实上可以这么访问: _类__私有属性名或方法名，但不推荐外部直接访问私有属性和私有方法
print(xiaoming._Person__age)
xiaoming._Person__put2()

print("%s" % ('-' * (repeat_num - 15)))

print("%s\n" % ('-' * repeat_num))

