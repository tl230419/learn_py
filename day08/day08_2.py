'''
*****************
Date: 2020-04-16
Author: Allen
*****************
'''

import time

result = time.time()
print(result)

time.sleep(3)
print('end')

import datetime

year = datetime.datetime.now().year
month = datetime.datetime.now().month
day = datetime.datetime.now().day
print(year)
print(month)
print(day)

import math

print(math.pow(10, 2))
print(math.floor(1.8234234234234))
print(math.ceil(1.1234234234234))
print(round(1.6234234234234))
print(math.sin(1.57))

import random

print(random.randint(10, 20))
print(random.random())
print(random.uniform(1.3, 8.5))

l = [10, 20, 30]
print(random.choice(l))
print(random.choices(l))