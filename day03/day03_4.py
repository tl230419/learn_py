'''
*****************
Date: 2020-04-13
Author: Allen
*****************
'''

'''
import utils

print(utils.age)
print(utils.name)

utils.func()
'''

#from utils import func, age, name
from utils import *
print(name)
print(age)
func()

#while True:
def show_menu():
    print('*' * 50)
    print('欢迎使用[名片管理系统]V1.0')
    print()
    print('1.新建名片')
    print('2.显示名片')
    print('3.查询名片')
    print()
    print('0.退出系统')
    print('*' * 50)
    #break

card_list = [] # 名片数据列表  [姓名,电话,qq,email]

def create_card():
    '''
    创建新名片
    :return:
    '''
    print('您选择的功能是： 1')
    print('功能： 新建名片')
    name = input('请输入姓名：')
    phone = input('请输入电话：')
    qq = input('请输入QQ：')
    email = input('请输入邮箱：')
    card = [name,phone,qq,email]
    card_list.append(card)

def show_all():
    '''
    显示所有名片
    :return:
    '''
    print('您选择的功能是： 2')
    print('功能： 显示全部')
    print('姓名\t电话\tQQ\t邮箱')
    print('-' * 50)
    for card in card_list:
        print('%s\t%s\t%s\t%s'%(tuple(card)))
    print('-' * 50)

def search_card():
    '''
    查询名片
    :return:
    '''
    print('您选择的功能是： 3')
    print('功能： 查询名片')
    name = input('请输入查询的姓名：')
    for card in card_list:
        if card[0] == name:
            handle_card(card)
            break
    else:
        print('没有找到对应的用户')

def handle_card(card):
    '''
    处理名片
    :param card:
    :return:
    '''
    while True:
        type = int(input('请输入对名片的操作: 1.修改/ 2.删除/ 0.返回上一级:'))
        if type == 1:
            modify_card(card)
            break
        elif type == 2:
            delete_card(card)
            break
        elif type == 0:
            break
        else:
            print('输入错误，请重新输入')

def modify_card(card):
    '''
    修改名片
    :param card:
    :return:
    '''
    name = input('请输入姓名：')
    phone = input('请输入电话：')
    qq = input('请输入QQ：')
    email = input('请输入邮箱：')
    card[0] = name
    card[1] = phone
    card[2] = qq
    card[3] = email

def delete_card(card):
    '''
    删除名片
    :param card:
    :return:
    '''
    card_list.remove(card)

while True:
    ...
    show_menu()
    type = int(input('请输入执行的操作：'))
    if type == 1:
        # 新建名片
        create_card()
    elif type == 2:
        # 显示全部
        show_all()
    elif type == 3:
        # 搜索名片
        search_card()
    elif type == 0:
        break