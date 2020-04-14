'''
*****************
Date: 2020-04-13
Author: Allen
*****************
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(self.name)

p = Person('张三', 30)
p.say_hello()

class Person:
    def __init__(self):
        print('执行了init方法')

p1 = Person()
p2 = Person()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        '''
        以字符串输出对象，把对象变成我们能够读懂的形式输出出来
        :return:
        '''
        return 'name:{}, age:{}'.format(self.name, self.age)

p1 = Person('张三', 30)
p2 = Person('李四', 40)
print(p1)
print(p2)