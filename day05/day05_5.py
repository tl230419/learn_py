'''
*****************
Date: 2020-04-13
Author: Allen
*****************
'''

str = 'hello'
print(len(str))

l = [1,2,3]
del l[0]
print(l)

str = 'hello'
result = 'h' in str
print(result)
result = 'h' not in str
print(result)

str1 = 'hello'
str2 = 'world'
str = str1 + str2
print(str)

l1 = [1,2,3]
l2 = [4,5,6]
l = l1 + l2
print(l)

t1 = (1,2,3)
t2 = (4,5,6)
t = t1 + t2
print(t)

str = 'hello'
print(str * 3)

l = [1,2,3]
print(l * 3)