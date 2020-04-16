'''
*****************
Date: 2020-04-16
Author: Allen
*****************
'''

a = 10
b = 0
#c  = a / b
#print(c)

try:
    result = a / b
    print('没有异常')
except:
    print('出现了异常')

try:
    result = a / b
    print('没有异常')
except Exception as error:
    print('出现了异常', error)

'''
try:
    a = 1 / 0
finally:
    print('hello')
'''

f = open('a.txt', 'w')
f.write('hello')
try:
    a = 10
    b = 0
    re = a / b
except:
    print('出现异常')
finally:
    f.close()
    print('文件已关闭了')

a = 10
b = 0
try:
    result = a / b
    print(result)
except:
    print('出异常')
else:
    print('没有出异常')
finally:
    print('最终执行的代码')

#l = [10, 20, 30]
#print(l[-10])

#d = {'name':'张三', 'age':30}
#print(d['phone'])

#str = 'abc'
#print(int(str))

class Person:
    def __init__(self):
        self.name = '张三'
        self.age = 30

p = Person()
#print(p.id)

class MyException(Exception):
    def __init__(self, msg):
        '''
        异常的提示文字
        :param msg:
        '''
        self.msg = msg

    def __str__(self):
        return self.msg


a = 10
b = 0
try:
    if b == 0:
        raise MyException('出现了0')
    result = a / b
    print(result)
except MyException as error:
    print('捕获异常', error)

try:
    a = 1 / 0
    try:
        int("abc")
    except Exception as error:
        print(error)
except Exception as error:
    print(error)


try:
    a = 1 / 0
    b = [1,2]
    b[2]
except IndexError as error:
    print('IndexError 错误逻辑')
except Exception as error:
    print(error)

import random

def hello():
    try:
        b = [1]
        b[random.randint(0, 1)]

        print("--0")
        return 0
    except Exception as error:
        print("--1")
        return 1
    finally:
        print("--2")
        return 2

hello()