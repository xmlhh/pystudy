#! /usr/bin/python3
#-*- coding:utf-8 -*-
"""
#文件名称：BasicGrammar.py
#编写人员：LHH
#项目组：系统组
#创建日期：2020/07/01
#功能描述：Python基础语法
#修改描述：
#备注：
"""


print("Python基础语法：")

print('一. Python四则运算：')
print('     200 + 100 = ', 200 + 100)
print('     200 - 100 = ', 200 - 100)
print('     200 * 100 = ', 200 * 100)
print('     200 / 100 = ', 200 / 100)
print('     200 % 99 = ', 200 % 99)


print("二. 行与缩进")
print(' 1. python最具特色的就是使用缩进来表示代码块，不需要使用大括号 {} \
        缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数。实例如下: ')

if True:
    print("这个条件是True")
else:
    print("这个条件是false")

print(' 2. 缩进不一致，会导致运行错误: ')
if True:
    print ("Answer")
    print ("True")
else:
    print ("Answer")
#  print ("False")

print("三. 多行语句: ")

print(' Python通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠(\)来实现多行语句，例如：')

"""
total = item_one + \
        item_two + \
        item_three
"""


print("四. 数字(Number)类型")
print("""python中数字有四种类型：整数、布尔型、浮点数和复数。
        int (整数), 如 1, 只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
        bool (布尔), 如 True。
        float (浮点数), 如 1.23、3E-2 
        complex (复数), 如 1 + 2j、 1.1 + 2.2j """)

print("五. 字符串(String)")
    #python中单引号和双引号使用完全相同。
    #使用三引号'''或"""可以指定一个多行字符串。
    #转义符 '\'，换行
    #反斜杠可以用来转义，使用r可以让反斜杠不发生转义。。 如 r"this is a line with \n" 则\n会显示，并不是换行。
    #按字面意义级联字符串，如"this " "is " "string"会被自动转换为this is string。
    #字符串可以用 + 运算符连接在一起，用 * 运算符重复。
    #Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
    #Python中的字符串不能改变。
    #Python 没有单独的字符类型，一个字符就是长度为 1 的字符串。
    #字符串的截取的语法格式如下：变量[头下标:尾下标]

    # word = '字符串'
    # sentence = "这是一个句子。"
    # paragraph = """这是一个段落，
    # 可以由多行组成"""


str = 'Runoob'
print('字符串:', str)

print('完整字符串输出：\n', str)                              # 完整字符串输出
print('输出第一个到倒数第二个的所有字符：\n', str[0:-1])         # 输出第一个到倒数第二个的所有字符
print('输出字符串第一个字符：\n', str[0])                      # 输出字符串第一个字符
print('输出从第三个开始到第五个的字符：\n', str[2:5])            # 输出从第三个开始到第五个的字符
print('输出从第三个开始的后的所有字符：\n', str[2:])             # 输出从第三个开始的后的所有字符
print('输出字符串两次：\n', str * 2)                          # 输出字符串两次
print('连接字符串：\n', str + '你好')                         # 连接字符串

print('------------------------------')

print('使用反斜杠(\)+n转义特殊字符：\n', 'hello\nrunoob')                         # 使用反斜杠(\)+n转义特殊字符
print('在字符串前面添加一个 r，表示原始字符串，不会发生转义：\n', r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义


print("六. 空行")
print("""
    函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。类和函数入口之间也用一行空行分隔，以突出函数入口的开始。
    空行与代码缩进不同，空行并不是Python语法的一部分。书写时不插入空行，Python解释器运行也不会出错。但是空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。
    记住：空行也是程序代码的一部分。""")


print('二. Python输入输出：')
print(' 1. 输入(name)：')
name = input()

print(' 2. 输出(name)：')
print('hello', name)

#print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""：
x = "a"
y = "b"
print('换行输出---------')
print(x)
print(y)

print('不换行输出---------')
print(x, end=" ")
print(y, end=" ")
print()


