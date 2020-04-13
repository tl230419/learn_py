'''
*****************
Date: 2020-04-13
Author: Allen
*****************
'''

d = {'中国':'China', '英国':'England', '美国':'America'}
print(d)

d = {'中国':'China', '英国':'England', '美国':'America', '美国':'USA'}
print(d)

d = {'中国':'China', '英国':'England', '美国':'America'}
#d['法国'] = 'France'
d.setdefault('法国','France')
print(d)

d = {'中国':'China', '英国':'England', '美国':'America', '美国':'USA'}
#del d['法国']
#result = d.pop('法国')
print(d)
d.clear()
print(d)

d = {'中国':'China', '英国':'England', '美国':'America', '美国':'USA'}
d['美国'] = 'USA'
print(d)

d = {'中国':'China', '英国':'England', '美国':'America', '美国':'USA'}
value = d['中国']
print(value)

d = {'中国':'China', '英国':'England', '美国':'America', '美国':'USA'}
for ele in d:
    print(ele, d[ele])

d = {'中国':'China', '英国':'England', '美国':'America', '美国':'USA'}
for key in d.keys():
    print(key)

d = {'中国':'China', '英国':'England', '美国':'America', '美国':'USA'}
for value in d.values():
    print(value)

d = {'中国':'China', '英国':'England', '美国':'America', '美国':'USA'}
for key,value in d.items():
    print(key,value)

d = {'name':'张三', 'phone':'12332', 'age':40, '性别':'男'}
print(d)