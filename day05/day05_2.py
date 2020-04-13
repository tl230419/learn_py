'''
*****************
Date: 2020-04-13
Author: Allen
*****************
'''

str1 = 'hello'
print(str1)
str2 = "hello"
print(str2)

str = 'hello'
ele = str[2]
print(ele)

str = 'hello'
for ele in str:
    print(ele)

while True:
    name = input('请输入用户名：')
    if not (len(name) >= 6 and len(name) <= 20):
        print('用户名必须6到20位')
        continue

    ele = name[0]
    if not ele.isalpha():
        print('用户名第一个必须为字母')
        continue

    print('用户名合法')
    break

while True:
    pwd = input('请输入密码：')
    if len(pwd) < 6:
        print('密码长度至少为6位')
        continue

    if pwd.isdecimal():
        print('密码不能为纯数字')
        continue

    if ' ' in pwd:
        print('密码不能有空格')
        continue

    print('密码合法')
    break