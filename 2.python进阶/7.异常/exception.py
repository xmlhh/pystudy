#! /usr/bin/python3
#-*- coding:utf-8 -*-
"""
#文件名称：exception.py
#编写人员：LHH
#项 目 组：系统组
#创建日期：2020/07/08
#功能描述：异常
#修改描述：
#备注：
"""

repeat_num = 45
"""
异常：
1.异常的概念： 程序运行时停止执行并提示错误信息， 称之为抛出异常
2.捕获异常： 
3.异常的传递：
4.自定义异常：
"""

print("****************1.简单的捕获异常*****************")
"""
开发中，如果对某些代码的执行不能确定是否正确， 用try()来捕获异常
简单的语法格式：
try:
    执行的代码块    
except:
    异常处理
"""
def except_a():

    is_ok = True
    while True:
        #简单的捕获异常并处理
        try:
            num = int(input('请输入数字： '))
            is_ok = True
        except:
            print('您的输入有误，请重新输入数字！')
            is_ok = False

        if not is_ok:
            continue
        else:
            break

except_a()

print("%s" % ('-' * (repeat_num - 15)))



print("****************2.根据错误类型捕获异常和未知错误*****************")
"""
针对不同类型的异常，做出不同的响应， 这个时候就需要捕获错误类型
语法：
try
    pass
except 错误类型1：
    pass
except (错误类型2, 错误类型3)：
    pass
except Exception as result:
    print('未知错误 %s' % result)
"""
def except_b():

    is_ok = True
    while True:
        #捕获错误类型异常
        try:
            num = int(input('请输入数字： '))
            res = 10 / num
            print('运算结果：%d' % res)
            is_ok = True

        # #输入数字以外的其他字符，出现的异常
        # except ValueError:
        #     print("ValueError: invalid literal for int() with base 10: '%s'" % num)
        #     is_ok = False
        #
        # #输入0，除0异常
        # except ZeroDivisionError:
        #     print('ZeroDivisionError: division by zero！')
        #     is_ok = False

        #未知错误异常处理，可以是上面两个错误类型或其他任何错误
        except Exception as rest:
            print('未知错误：%s' % rest)
            is_ok = False

        if not is_ok:
            continue
        else:
            break

except_b()

print("%s" % ('-' * (repeat_num - 15)))




print("****************3.捕获异常完整语法*****************")
"""
捕获异常的完整语法：
try:
    pass
except 错误类型1:
    pass
except 错误类型2:
    pass
except (错误类型3, 错误类型4):
    pass
except Exception as res:
    #未知错误执行的代码
    pass
else: 
    #没有任何异常时，才会执行的代码
    pass
finally:
    #无论是否有异常，都会执行的代码
    pass
"""
def except_c():

    is_ok = True
    while True:
        #捕获错误类型异常
        try:
            num = int(input('请输入数字： '))
            res = 10 / num
            print('运算结果：%d' % res)
            is_ok = True

        # #输入数字以外的其他字符，出现的异常
        # except ValueError:
        #     print("ValueError: invalid literal for int() with base 10: '%s'" % num)
        #     is_ok = False
        #
        #输入0，除0异常
        except ZeroDivisionError:
            print('ZeroDivisionError: division by zero！')
            is_ok = False

        #未知错误异常处理，可以是上面两个错误类型或其他任何错误
        except Exception as rest:
            print('未知错误：%s' % rest)
            is_ok = False

        # 没有任何异常时，才会执行的代码
        else:
           print('没有任何异常')

        # 无论是否有异常，都会执行的代码
        finally:
            print('任何情况都会执行')

        if not is_ok:
            continue
        else:
            break

except_c()

print("%s" % ('-' * (repeat_num - 15)))



print("****************4.异常的传递性*****************")
"""
异常的传递：当函数/方法出现异常时，会将异常传递给函数/方法的调用方，如果传递到主程序，仍然没有处理异常，程序才会被终止
技巧：为了保证代码的整洁性、且不需要大量使用异常捕获，只需在主函数中增加异常捕获，因为主函数调用了其他函数，只要其他函数出现异常，就会传递到主函数的捕获异常中
"""
def func1():
    num = int(input('请输入数字：'))
    return num

def func2():
    return func1()

def func():
    is_ok = True
    while True:
        try:
            print(func2())
            is_ok = True
        except Exception as res:
            print('未知错误：%s' % res)
            is_ok = False

        if not is_ok:
            continue
        else:
            break
#调用
func()

print("%s" % ('-' * (repeat_num - 15)))



print("****************5.主动抛出异常*****************")
"""
主动抛出异常：
1.创建python提供的Exception异常类的对象
2.使用raise关键字抛出异常对象

开发中根据应用程序的业务需求，主动抛出异常
示例：提示用户输入密码，密码长度至少8位及以上，否则抛出异常
"""
def passwd():

    pwd = input('请输入密码：')

    if len(pwd) >= 8:
        print('您输入的密码为：%s' % pwd)
    else:
        print('主动抛出异常：')
        ext = Exception('密码长度至少8位')
        raise ext
try:
    passwd()
except Exception as res:
    print(res)


print("%s\n" % ('-' * repeat_num))