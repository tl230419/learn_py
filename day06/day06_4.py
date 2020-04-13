'''
*****************
Date: 2020-04-13
Author: Allen
*****************
'''

f = open('a.txt')
#data = f.read(-1)
#print(data)
data = f.read(5)
print(data)
result = f.readline()
print(result)
result = f.readline(10)
print(result)
result = f.readlines()
print(result)
f.close()

f2 = open('b.txt','a')
f2.write('hello world')
f2.close()

f3 = open('c.txt','a')
l = ['bill','gates','tom']
f3.writelines(l)
f3.close()