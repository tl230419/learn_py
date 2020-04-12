'''
*****************
Date: 2020-04-13
Author: Allen
*****************
'''

names_tuple = ('林青霞','张曼玉','胡慧中')
print(names_tuple)

names_tuple = ('林青霞')
print(names_tuple)
names_tuple = ('林青霞',)
print(names_tuple)

t = '林青霞','张曼玉','胡慧中'
print(t)

t = ('林青霞','张曼玉','胡慧中')
name1,name2,name3 = t
print(name1)
print(name2)
print(name3)

a = 10
b = 20
tmp = a
a = b
b = tmp
print(a, b)

a = 10
b = 20
a,b = b,a
print(a, b)

l = [10, 20, 30]
print(l)
t = tuple(l)
print(t)
