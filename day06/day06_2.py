'''
*****************
Date: 2020-04-13
Author: Allen
*****************
'''

def sum(*args):
    pass
sum(10,20,30)
sum(10,20,30,40)

def sum(name,*args):
    result = 0
    for ele in args:
        result += ele
    return result

r = sum(10,20,30,40)
print(r)

def func(**kwargs):
    pass

func(name='张三',age=30,score=70)

def func(a,**kwargs):
    name = kwargs['name']
    age = kwargs['age']
    print(name,age)

func(name='张三',age=30,a=10,score=70)

def func(*args):
    print(args)

t = (10,20,30)
func(*t)

def func(**kwargs):
    print(kwargs)

d = {'name':'张三','age':40}
func(**d)