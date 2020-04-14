'''
*****************
Date: 2020-04-13
Author: Allen
*****************
'''

class MobilePhone:
    def __init__(self, name):
        self.name = name
        self.battery = 5

    def __str__(self):
        return 'name:{}, battery:{}'.format(self.name, self.battery)

    def play_game(self):
        '''
        打游戏
        :return:
        '''
        if self.battery >= 10:
            print('打游戏')
            self.battery -= 10
        else:
            print('不能打游戏')

    def listen_music(self):
        '''
        听歌
        :return:
        '''
        if self.battery >= 5:
            print('听歌')
            self.battery -= 5
        else:
            print('不能听歌')

    def call(self):
        '''
        打电话
        :return:
        '''
        if self.battery >= 4:
            print('打电话')
            self.battery -= 4
        else:
            print('不能打电话')

    def receive_call(self):
        '''
        接电话
        :return:
        '''
        if self.battery >= 3:
            print('接电话')
            self.battery -= 3
        else:
            print('不能接电话')

    def charge(self):
        '''
        充电
        :return:
        '''
        print('充电')
        self.battery += 10

phone = MobilePhone('苹果')

phone.play_game()
phone.listen_music()
phone.charge()
print(phone)