'''
*****************
Date: 2020-04-13
Author: Allen
*****************
'''

print('hello1')
print('hello2')
print('hello3')
print('hello4')
print('hello5')

age = int(input('请输入你的年纪：'))
if age >= 18:
    print('允许进网吧嗨皮')
else:
    print('回家写作业')

holiday_name = input('请输入节日名称')
if holiday_name == '情人节':
    print('买玫瑰/看电影')
elif holiday_name == '平安夜':
    print('买苹果/吃大餐')
elif holiday_name == '生日':
    print('买蛋糕')
else:
    print('每天都是节日，每天一个红包')

has_ticket = input("请输入是否有车票(0 没有 1 有)：")
has_ticket = int(has_ticket)
knife_length = input('请输入刀的长度：')
knife_length = int(knife_length)

if bool(has_ticket):
    if knife_length > 20:
        print("不能进站")
    else:
        print("可以进站")
else:
    print("不能进站")