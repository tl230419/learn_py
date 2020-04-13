'''
*****************
Date: 2020-04-13
Author: Allen
*****************
'''

s = {'张三','李四','王五'}
print(s)

s = {'张三','李四','王五','张三'}
print(s)

s = {'张三','李四','王五'}
for ele in s:
    print(ele)

s = {'张三','李四','王五'}
s.add('赵六')
print(s)

s = {'张三','李四','王五'}
s.remove('张三')
print(s)

s = {'张三','李四','王五'}
s.pop()
print(s)

s = {'张三','李四','王五'}
s.discard('林青霞')
print(s)