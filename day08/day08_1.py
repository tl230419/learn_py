'''
*****************
Date: 2020-04-16
Author: Allen
*****************
'''

import utils

print(utils.name)
result = utils.sum(10, 20)
print(result)
p = utils.Person('张三', 30)

from utils import name, sum

print(name)
result = sum(10, 20)

from utils import *

print(name)
result = sum(10, 20)
p = Person('林青霞', 60)

from hello import name
from hi import name

print(name)

from hello import name as hello_name
from hi import name as hi_name

print(hello_name)
print(hi_name)

from hello import *
from hi import *

print(name)

import hello
import hi

print(hello.name)
print(hi.name)


def sum(m, n):
    return m + n

if __name__ == '__main__':
    a = 10
    b = 20
    result = sum(a, b)
    print("main:", result)

import pkg.hello

print(pkg.hello.name)
pkg.hello.say()
nice = pkg.hello.Nice()

from pkg import hello

print(hello.name)
hello.say()
nice = hello.Nice()

from pkg.hello import name
from pkg.hello import say
from pkg.hello import Nice

print(name)
say()
nice = Nice()

from pkg import *

print(name)
say()
nice = Nice()