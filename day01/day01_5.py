'''
*****************
Date: 2020-04-13
Author: Allen
*****************
'''

name = '张三'
print(10)
print(name)
print(10, name)

age = input('请输入年纪')
print(age)

t = type(age)
print(t)

a = int(input('请输入第一个数'))
b = int(input('请输入第二个数'))
print(a+b)

price = float(input('请输入苹果单价：'))
weight = float(input('请输入苹果重量：'))
money = price * weight
print('付款金额：%.2f'%money)

name = input('请输入姓名：')
com = input('请输入公司名：')
title = input('请输入职务：')
telephone = input('请输入电话：')
email = input('请输入邮箱：')

print('*'*50)
print('公司名称：%s'%com)
print()
print('%s(%s)'%(name,title))
print()
print('电话：%s'%telephone)
print('邮箱：%s'%email)
print('*'*50)