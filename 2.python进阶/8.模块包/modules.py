#! /usr/bin/python3
#-*- coding:utf-8 -*-
"""
#文件名称：modules.py
#编写人员：LHH
#项 目 组：系统组
#创建日期：2020/07/08
#功能描述：模块和包
#修改描述：
#备注：
"""

"""
模块： 每一个以扩展名py结尾的python
模块名也是标识符，要符合标识符的命名规则
在模块中定义的全局变量、函数、类都是提供给外界直接使用的工具
"""

repeat_num = 45

print("****************1.模块的两种导入方式*****************")
"""
1.import 导入：
提示： 在导入模块时， 每个导入应该单独占一行
    import 模块名1
    import 模块名2
使用as指定模块的别名： 方便使用， 防止冲突
    import 模块名 as 模块别名
    模块的别名用大驼峰命名法： 如Method
    这种方式导入后，可以使用模块提供的给工具： 全局变量、函数、类
    访问： 需要通过模块名/别名.工具 访问

2.from ... import 导入
    from 模块名 import 工具名（全局变量、函数、类）
    这种方式导入后的是模块中某一个工具， 
    访问： 可直接使用模块内的工具， 不需要通过模块名/别名访问

"""
import test1
import test2

print(test1.title)
print(test2.title)
test1.say()
test2.say()
dog = test1.Dog()
print(dog)
cat = test2.Cat()
print(cat)

print("%s" % ('-' * (repeat_num - 15)))


import test1 as DogModule
import test2 as CatModule

DogModule.say()
CatModule.say()
dog = DogModule.Dog()
print(dog)
cat = CatModule.Cat()
print(cat)

print("%s" % ('-' * (repeat_num - 15)))


print("\n****************2.导入模块的同名工具和所有工具*****************")
"""
如果导入的两个模块存在同名的函数， 那么最后导入模块的函数， 会覆盖之前导入的函数
"""
from test1 import say
from test2 import say

# say()

#上面的方式只能使用test2模块的say函数
#可以用as改别名，使用别名，如下：

from test1 import say as module1_say
from test2 import say

module1_say()
say()

"""
从模块导入所以工具：
from 模块 import *
#这种方式不推荐使用， 因为函数重名并没有任何提示， 出问题不好排查
"""


print("\n****************3.模块的扩展*****************")
"""
1.模块的搜索顺序：
    优先搜索当前目录， 如果有就直接导入， 不再搜索系统目录； 如果没有再搜索系统目录
    所以在开发中， 文件名不要与系统模块文件重名， 如果重名， 系统模块工具就无法使用， 只能用当前目录的模块
    每个模块都有一个内置方法 __file__ 查看模块的完整路径
"""
import random

print(random.__file__)
# rd = random.randint(0, 100)
# print('0-100之间的随机数： ' % rd)
print("%s\n" % ('-' * repeat_num))

"""
2.__name__ 属性：
    模块内部执行的代码块， 外部不被执行，可以用于模块内部测试执行代码
    如果是被其他文件导入的， __name__ 就是模块
    如果是当前执行的程序， __name__ 是 __main__
例子： 请见test1.py和test2.py
"""

"""
一个完整的py文件代码顺序格式：
#导入模块
#定义全局变量
#定义类
#定义函数

#代码执行的主函数
def main():
    pass
    
#根据 __name__判断是否执行下方代码
if __name__ = "__main__":
    main()
"""

print("%s\n" % ('-' * repeat_num))