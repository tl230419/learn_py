'''
*****************
Date: 2020-04-16
Author: Allen
*****************
'''

name = '张三'

def sum(a, b):
    return a + b

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return 'name:{}, age:{}'.format(self.name, self.age)
