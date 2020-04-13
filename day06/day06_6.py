'''
*****************
Date: 2020-04-13
Author: Allen
*****************
'''

class Person:
    pass

p1 = Person()

class Person:
    def say_hello(self):
        print('hello')
    def run(self):
        print('run')

p = Person()
p.say_hello()

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p = Person('张三',30)
print(p.name)
print(p.age)