'''
*****************
Date: 2020-04-15
Author: Allen
*****************
'''

class Item:
    def __init__(self, type, area):
        '''
        创建家具类的初始化方法
        :param type: 家具类型
        :param area: 家具面积
        '''
        self.type = type
        self.area = area

    def __str__(self):
        return '家具类型:{},家具占用面积:{}'.format(self.type, self.area)

class Home:
    def __init__(self, address, area):
        '''
        房子的初始化方法
        :param address: 房子地址
        :param area: 房子面积
        '''
        self.address = address
        self.area = area
        self.free_area = self.area
        self.items = []

    def __str__(self):
        return '房子面积:{}, 占用面积:{},剩余面积:{}'.format(self.address, self.area, self.free_area)

    def add_item(self, item):
        '''
        添加家具到房子中
        :param item: 家具类Item的实例
        :return:
        '''
        if self.free_area >= item.area:
            self.items.append(item)
            self.free_area -= item.area
            print('添加成功')
        else:
            print('面积不足，不能添加家具')


item1 = Item('桌子', 10)
item2 = Item('椅子', 5)

home = Home('深圳湾一号', 300)
print(home)

home.add_item(item1)
home.add_item(item2)
print(home)
print(home.items[0], home.items[1])