def say_hello():
    print('hello world')

say_hello()

def say_hello2():
    '''
    这是给林青霞打招呼的方法
    :return:
    '''
    print('hello 林青霞')

say_hello2()

def sum(a, b):
    '''
    这个函数是求两个数据的和
    :param a: 第一个数据
    :param b: 第二个数据
    :return:
    '''
    result = a + b
    print(result)

sum(10, 20)

def my_max(a, b):
    if a > b:
        return a
    else:
        return b

max_value = my_max(10 ,20)
print(max_value)

def cacl(a, b):
    '''
    求a+b以及a-b的结果
    :param a:
    :param b:
    :return:
    '''
    sum = a + b
    result = a - b
    return sum, result

sum, result = cacl(10 ,20)
print(sum, result)

def say_hello():
    print('hello')

import random
def get_temp():
    return random.randint(0, 100)

def say_hello(name):
    print('hello %s'%name)

def sum(a, b):
    return a + b

def fun1():
    b = 20
    print('hello%d'%b)

m = 10
n = 20

def func():
    print(m)

m = 10

def func():
    global m
    m = 30
    print('函数内部m=%d'%m)

func()