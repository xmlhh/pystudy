#! /usr/bin/python3
#-*- coding:utf-8 -*-
"""
#文件名称：class__property_method.py
#编写人员：LHH
#项 目 组：系统组
#创建日期：2020/07/06
#功能描述：类属性、类方法、静态方法
#修改描述：
#备注：
"""

repeat_num = 45

print("****************1.类属性*****************")
"""
类属性：
类中定义的属性，保存类相关的特征，类属性不会用于记录具体对象的特征
"""
class Fruit(object):

    #定义类属性，记录创建Fruit对象的数量
    count = 0

    def __init__(self, name):
        self.name = name
        #类属性值累加
        Fruit.count += 1

    def func(self):
        print('水果名称：%s' % self.name)


apple = Fruit('苹果')
banana = Fruit('香蕉')
watermelon = Fruit('西瓜')
pineapple = Fruit('菠萝')

apple.func()
print('Fruit.count 统计水果的种类数量：%d' % Fruit.count)
#尽量使用；类.属性，而不要使用 对象.属性的方式访问类属性
apple.count = 33
print('apple.count 统计水果的种类数量：%d' % apple.count)
#对象.属性的方式 并没有改变类属性的值
print('Fruit.count 统计水果的种类数量：%d' % Fruit.count)

print("%s" % ('-' * (repeat_num - 15)))



print("****************2.类方法*****************")
"""
类方法：针对类对象定义的方法

类方法需要用@classmethod来修饰；
类方法的第一个参数是cls，和实例方法的第一个参数self类似；
由哪个类调用的方法，方法内的cls就是哪一个类的引用；
通过 类名.类方法 来调用，调用时，不需要传递cls参数；
在方法内部，可以用cls.xx 访问类的属性，也可以通过cls.xx() 调用其他的方法

语法：
@classmethod
def 类方法名(cls):
    pass
    
"""
class Vegetable(object):

    count = 0

    def __init__(self, name):
        self.name = name
        Vegetable.count += 1

    def func(self):
        print('蔬菜的名称：%s' % self.name)

    # 定义类方法
    @classmethod
    def show_count(cls):
        print('类方法内部, 蔬菜种类的数量：%d' % cls.count)

cabbage = Vegetable('白菜')
# Vegetable.show_count()
radish = Vegetable('萝卜')
Vegetable.show_count()


print("%s" % ('-' * (repeat_num - 15)))



print("****************3.静态方法*****************")
"""
静态方法：当一个方法不需要访问实例属性和方法，也不需要访问类属性和方法，就可以封装成静态方法，
静态方法用@staticmethod来修饰
通过 类名.静态方法 来调用
语法：
@staticmethod
def 静态方法名():
    pass
"""
class Cat(object):

    @staticmethod
    def run():
        print('猫在吃鱼...')

    def __init__(self, name):
        self.name = name

    def func(self):
        print('蔬菜的名称：%s' % self.name)

Cat.run()

print("%s" % ('-' * (repeat_num - 15)))



print("****************4.实例方法、类方法、静态方法的区别*****************")
class Diff(object):
    def func(self, num):
        print('executing func(%s, %s)' % (self, num))

    @classmethod
    def class_func(cls, num):
        print('executing class_func(%s, %s)' % (cls, num))

    @staticmethod
    def static_func(num):
        print('executing static_func(%s)' % num)


df = Diff()

# 实例方法
df.func(6)
# print(df.func)
print("%s" % ('-' * (repeat_num - 15)))

# 类方法
df.class_func(6)
Diff.class_func(6)
# print(df.class_func)
print("%s" % ('-' * (repeat_num - 15)))

# 静态方法
df.static_func(6)
Diff.static_func('hi')
# print(df.static_func)
print("%s" % ('-' * (repeat_num - 15)))



print("****************5.案例*****************")
"""
游戏：
1.设计一个Game类
2.属性：
    定义一个类属性记录游戏历史最高分 history_score
    定义一个实例属性记录游戏玩家的姓名 name
3.方法：
    静态方法： 游戏帮助信息 game_help()
    类方法： 显示历史最高分 show_history_score()
    实例方法： 开始游戏 start_game()
"""
class Game(object):

    history_score = 0

    def __init__(self, name):
        self.name = name
        Game.history_score += 1024

    @staticmethod
    def game_help():
        print('显示游戏帮助信息')

    @classmethod
    def show_history_score(cls):
        print('历史最高分： %d' % cls.history_score)

    def start_game(self):
        print('%s 准备开始游戏' % self.name)

#调用
Game.game_help()
Game.show_history_score()
player = Game('olhho')
player.start_game()


print("%s\n" % ('-' * repeat_num))