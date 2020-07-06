#! /usr/bin/python3
#-*- coding:utf-8 -*-
"""
#文件名称：multiple_inherit.py
#编写人员：LHH
#项 目 组：系统组
#创建日期：2020/07/04
#功能描述：单继承、方法重写、私有属性和方法、多继承
#修改描述：
#备注：
"""

repeat_num = 45

print("****************1.单继承*****************")
"""
继承的概念：子类（又名派生类）继承父类（又名基类），又叫子类从父类派生，子类拥有父类的所有属性和方法
继承的语法：
    class B(A):
        pass

A类是B类的父类（基类），B类是A类的子类（派生类）

"""
class Person:

    def eat(self):
        print('吃饭')

    def sleep(self):
        print('睡觉')

    def play_doug(self):
        print('打豆豆')

class EmployeeA(Person):

    def work(self):
        print('上班')

    def get_salary(self):
        print('领薪水')

class EmployeeB(EmployeeA):

    def deduct_salary(self):
        print('被扣薪水')

class Freelancer(Person):

    def play(self):
        print('玩耍')

xiaoming = Person()
print('小明的所有方法：')
xiaoming.eat()
xiaoming.sleep()
xiaoming.play_doug()
print("%s" % ('-' * (repeat_num - 15)))

zhangsan = EmployeeA()
print('张三的所有方法：')
zhangsan.eat()
zhangsan.sleep()
zhangsan.play_doug()
zhangsan.work()
zhangsan.get_salary()
print("%s" % ('-' * (repeat_num - 15)))

lisi = EmployeeB()
print('李四的所有方法：')
lisi.eat()
lisi.sleep()
lisi.play_doug()
lisi.work()
lisi.get_salary()
lisi.deduct_salary()
print("%s" % ('-' * (repeat_num - 15)))

wangwu = Freelancer()
print('王五的所有方法：')
wangwu.eat()
wangwu.sleep()
wangwu.play_doug()
wangwu.play()

#上面的关系：
#Person<---EmployeeA<---EmployeeB
"""
EmployeeB继承EmployeeA, EmployeeA继承Person
EmployeeB是EmployeeA的子类（派生类），EmployeeA是EmployeeB的父类（基类）
EmployeeA是Person的子类（派生类），Person是EmployeeA的父类（基类）
EmployeeB拥有EmployeeA和Person的属性和方法
"""
#Person<---Freelancer, Freelancer继承Person

print("%s\n" % ('-' * repeat_num))



print("****************2.方法重写*****************")
"""
如果父类的方法，无法满足子类的需求时，可以对父类的方法进行重写，在子类中重写父类的方法
重写父类方法有两种：
    1.覆盖父类的方法：
        子类的方法与父类的方法同名，重写后，只会调用子类的方法，而不会调用父类的同名方法
    2.对父类方法进行扩展:
        子类中重写父类的方法，
        在需要的位置使用super.父类方法，来调用父类方法的执行，
        其他位置针对子类的需求，编写子类特有的代码实现
"""

class FreedoomA(Person):

    def sleep(self):
        print('睡午觉')

xiaoliu = FreedoomA()
print('小六的sleep方法：')
xiaoliu.sleep()
print("%s" % ('-' * (repeat_num - 15)))

class FreedoomB(Person):

    def sleep(self):
        print('睡午觉')
        #调用父类的同名方法
        super().sleep()
        print('晚安')

xiaoqi = FreedoomB()
print('小七的sleep方法：')
xiaoqi.sleep()

print("%s\n" % ('-' * repeat_num))





print("****************3.私有属性和方法*****************")
"""
继承后，子类对象不能在自己内部直接访问父类的私有属性和方法，
可以通过父类的公有方法间接访问父类的私有属性和方法
"""
class Staff:

    def __init__(self):
        #私有属性
        self.__id = 1002
        self.__name = '小杨'
        #公有属性
        self.sex = 'female'
        self.age = 19

    #私有方法
    def __test(self):
        print('1.父类的私有方法内部访问所有属性： %d, %s, %s, %d' % (self.__id, self.__name, self.sex, self.age))
    #公有方法
    def test(self):
        #内部调用私有方法
        self.__test()
        print('2.父类的公有方法内部访问所有属性： %d, %s, %s, %d' % (self.__id, self.__name, self.sex, self.age))


class Employee(Staff):

    def demo(self):
        #外部不能访问Staff的__id和__name私有属性
        #print('外部访问私有属性： %d, %s' % (self.__id, self.__name))
        print('外部访问父类的公有属性：%s, %d' % (self.sex, self.age))
        print('外部访问父类的公有方法：')
        self.test()


xiaozhang = Employee()
# xiaozhang.id = 1003
# xiaozhang.name ='小张'
xiaozhang.demo()

print("%s\n" % ('-' * repeat_num))



print("****************4.多继承*****************")
"""
多继承：子类可以继承多个父类，且拥有所有父类的属性和方法
语法：
    class 子类(父类1, 父类2, ...):
        pass
"""
class StaffZ:

    def eat(self):
        print('吃饭')

    def work(self):
        print('上班')

class StaffX:

    def sleep(self):
        print('睡觉')

    def work(self):
        print('下班')

class Developer(StaffZ, StaffX):
    pass

xm = Developer()
print('Developer对象访问StaffZ的方法: ', end='')
xm.eat()
print('Developer对象访问StaffX的方法: ',end='')
xm.sleep()

#多继承使用注意事项
#上述两个父类中存在同名方法或属性，子类对象在调用时，会调用哪一个呢？
#提示：开发中尽量避免这种情况，如果父类之间存在同名或方法，应尽量避免使用多继承
print('Developer对象访问StaffZ和StaffX的同名方法: ', end='')
xm.work()
print('只会调用最前面继承的父类的方法')

print("%s" % ('-' * (repeat_num - 15)))


'''
MRO方法搜索顺序
python提供了内置属性__mro__ 可以查看类的方法搜索顺序，
主要用于在多继承时，判断方法或属性的调用路径 print(class.__mro__)
如果找到方法，直接执行，不再搜索；如果当前类没有找到，继续在下一个类中找到；如果都没有找到方法，最后程序会报错
'''
print(Developer.__mro__)
print("%s" % ('-' * (repeat_num - 15)))


'''
新式类和旧式类
object是python提供的所有对象的基类，提供了内置属性和方法，可以dir函数查看
新式类：默认以object为基类，python3.x
旧式类：默认不以object为基类，python2.x
定义中，如果没有父类，建议统一继承object基类
class 类名(object):
    pass
'''
print(dir(object))

class A:
    pass

class B(object):
    pass

a = A()
b = B()

print('dir(a): ', dir(a))
print('dir(b): ', dir(b))


print("%s\n" % ('-' * repeat_num))
