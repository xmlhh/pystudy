#! /usr/bin/python3
#-*- coding:utf-8 -*-
"""
#文件名称：func_param_and_return_advanced.py
#编写人员：LHH
#项 目 组：研发四部Team3
#创建日期：2020/02/05
#功能描述：函数的参数和返回值进阶（前提：学完4.高级变量类型）
#修改描述：
#备注：
"""

repeat_num = 45

print("****************1.函数的返回值（知识点：元祖交换数据）*****************")
def func1():
    num = 2
    ret = num * 6
    return ret

def func2():
    wendu = 36.3
    shidu = 77.5
    return wendu, shidu


res1 = func1()
res2 = func2()
wendu, shidu = func2()

print('返回一个值：\t%d' % res1)
print('返回元祖：\t', res2)
print('返回多个值：\t%.1f, %.1f' % (wendu, shidu))
print("%s\n" % ('-' * repeat_num))


# 面试题1：交换两个变量a和b的值
print("面试题1：交换两个变量a和b的值")
a = 6
b = 9
print('a = %d, b = %d' % (a, b))
print("%s" % ('-' * (repeat_num - 15)))

#方法一：使用第三个变量
print("方法一：使用第三个变量c")
c = a
a = b
b = c
print('a = %d, b = %d' % (a, b))
print("%s" % ('-' * (repeat_num - 15)))

#方法二：不使用第三变量
print("方法二：不使用第三变量")
a = a + b
b = a - b
a = a - b
print('a = %d, b = %d' % (a, b))
print("%s" % ('-' * (repeat_num - 15)))

#方法三：python转有，利用元祖
print("方法三：python转有，利用元祖")
a, b = (b, a)
print('a = %d, b = %d' % (a, b))

#最终元祖写法
a, b = b, a
print('a = %d, b = %d' % (a, b))
print("%s\n" % ('-' * repeat_num))



print("****************2.函数的参数*****************")
"""
1）函数内部 赋值修改 不可变类型参数或可变类型参数，都不会修改到函数外部变量（实参）
2）如果函数传递的参数是可变类型，
    在函数内部，使用 内置方法 修改数据内容，会影响到函数外部变量（实参）
    在函数内部，使用 赋值 修改数据内容，不会影响到函数外部变量（实参）
"""

print('2.1 函数内部参数改变外部值')

g_list = [1, 2, 3]

def demo1(num_list):
    num_list = [6, 8, 2]
    print('函数内部1：\t', num_list)
    return None

def demo2(num_list):
    num_list.append(9)
    print('函数内部2：\t', num_list)
    return None

# 调用输出
print('原函数外部：\t', g_list)
demo1(g_list)
print('函数外部1：\t', g_list)
demo2(g_list)
print('函数外部2：\t', g_list)

print("%s" % ('-' * (repeat_num - 15)))


# 面试题2：+=
print('面试题2：+=')
"""
在python中，列表变量调用+=，本质上是在执行列表变量的extend()方法，
不会修改变量的引用，就会影响外部的值"""

g_num = 9

def demo3(num, num_list):
    num += num
    print('函数内部3：\t ', num)

    num_list += num_list
    # num_list.extend(num_list)
    print('函数内部3：\t ', num_list)
    return None

# 调用输出
print('原函数外部：\t ', g_num, g_list)
demo3(g_num, g_list)
print('函数外部3：\t ', g_num, g_list)

print("%s" % ('-' * (repeat_num - 15)))



print('2.2 函数的缺省参数')
"""
1）缺省参数：在函数定义时，参数赋值默认值；
2）缺省参数，必须在参数列表最后
"""
def params1(name, isSuccess=False):
    if isSuccess:
        print('%s######' % name)
    else:
        print('%s******' % name)
    return None

def params2(name, title='', isSuccess=False):
    if isSuccess:
        print('[%s] %s######' % (title, name))
    else:
        print('[%s] %s******' % (title, name))
    return None

params1('单个缺省参数调用')
params1('单个缺省参数调用', True)
params2('多个缺省参数调用', '哈哈', True)
params2('多个缺省参数调用', True)
params2('多个缺省参数调用', isSuccess=True)

print("%s" % ('-' * (repeat_num - 15)))



print('2.3 函数的多值参数')
"""
多值参数：（python特有，其他语言没有）
    如果一个函数处理的参数个数是不确定的，就需要用多值参数
    python中有两种多值参数：
        参数名前面一个 * 可以接收元祖
        参数名前面两个 * 可以接收字典
    一般命名时，习惯使用以下两个名字：
        *args    -->存放 元祖 参数，前面*
        **kwargs -->存放 字典 参数，前面**
"""
def multivalue_params(num, *args, **kwargs):
    print('数字型参数：\t %d' % num)
    print('元祖参数：\t', args)
    print('字典参数：\t', kwargs)
    return None

multivalue_params(1, 2, name="小明", age=19, gender=True)

print("%s" % ('-' * (repeat_num - 15)))


#案例1：数字累积
# def multi_num(args):
def multi_num(*args):
    sum_ret = 0
    multi_ret = 1

    for num in args:
        sum_ret += num
        multi_ret *= num

    return sum_ret, multi_ret

# ret = multi_num((1, 2, 3, 4, 5))
ret = multi_num(1, 2, 3, 4, 5)
print('数字累加：\t %d\n数字累积：\t %d' % ret)
print("%s" % ('-' * (repeat_num - 15)))

#案例2：元祖和字典的拆包
"""
在调用带多值参数的函数时，如果希望：
    将一个元祖变量，直接传递给args
    将一个字典变量，直接传递给kwargs
拆包的方式是：
    调用函数传递参数：元祖变量前加*
    调用函数传递参数：字典变量前加**
拆包语法：简化元祖变量/字典变量的传递
"""
def tuple_dict_unpack(*args, **kwargs):
    print('元祖：\t\t', args)
    print('字典：\t\t', kwargs)
    return None

# 不拆包传递
print("不拆包传递(1, 2, 3, name='小美', age=18)")
tuple_dict_unpack(1, 2, 3, name='小美', age=18)
print('')

# 拆包传递
print("拆包传递(1, 2, 3), {'name': '小美', 'age': 18}")
tuple = (1, 2, 3)
dict = {'name': '小美', 'age': 18}
tuple_dict_unpack(*tuple, **dict)
print('')

# 错误传递方式，元祖和字典内容都传给了元祖，字典为空
print("错误传递方式，元祖和字典内容都传给了元祖")
tuple_dict_unpack(tuple, dict)

print("%s" % ('-' * (repeat_num - 15)))




print('2.4 函数的递归')
"""
函数的递归：在函数内部，调用自己
python默认递归数是996，解决方法：
    import sys
    sys.setrecursionlimit(递归数最大3930)
注意：递归数太大容易内存溢出
"""
# 数字累加
# import sys
# sys.setrecursionlimit(3930)
def recursive_func(num):
    num += 1
    print(num, end=' ')

    # if num == 3926:
    if num == 100:
        return None

    recursive_func(num)
    return None

recursive_func(0)

print("%s\n" % ('-' * repeat_num))
