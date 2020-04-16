'''
*****************
Date: 2020-04-16
Author: Allen
*****************
'''

class WashMachine:
    def __init__(self, brand, capacity):
        '''
        初始化
        :param brand: 品牌
        :param capacity: 容量
        '''
        self.brand = brand
        self.capacity = capacity
        self.has_closed = False
        self.__mode = 0
        self.motor_speed = 0

    def open_door(self):
        self.has_closed = False
        print('打开洗衣机门')

    def close_door(self):
        self.has_closed = True
        print('关闭洗衣机门')

    def set_mode(self, mode):
        '''
        调节模式
        :param mode:
        :return:
        '''
        if mode != 1 and mode != 2:
            print('设置模式错误')
        else:
            self.__mode = mode

    def __set_motor_speed(self, speed):
        '''
        设置马达的转速
        :param speed: 1000：轻柔模式， 2000：狂揉模式
        :return:
        '''
        self.motor_speed = speed

    def wash(self):
        if not self.has_closed:
            print('请关闭洗衣机，哔哔哔...')
        elif self.__mode == 0:
            print('请设置模式')
        else:
            print('放水...')
            print('放满了')
            if self.__mode == 1:
                print('轻柔模式，洗内衣')
                self.__set_motor_speed(1000)
                print('马达转速：{}'.format(self.motor_speed))
                print('开始洗...')
            elif self.__mode == 2:
                print('狂揉模式，洗外套')
                self.__set_motor_speed(2000)
                print('马达转速：{}'.format(self.motor_speed))
                print('开始洗...')

            print('洗完了')


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print('hello')


class Student(Person):
    def __init__(self, name, age, id):
        super(Student, self).__init__(name, age)
        self.id = id

stu = Student('小明', 15, '123')
print(stu.name, stu.age, stu.id)
stu.say_hello()

class Mother:
    def cook(self):
        print('做饭')

class Father:
    def make_money(self):
        print('赚钱')

class Son(Mother, Father):
    pass

son = Son()
son.cook()
son.make_money()

class Human:
    def eat(self):
        print('人类吃饭')

class ZhHuman(Human):
    def eat(self):
        print('中国人使用筷子吃饭')

class UsHuman(Human):
    def eat(self):
        print('美国人使用刀叉吃饭')

class AfricaHuman(Human):
    def eat(self):
        print('非洲人直接用手吃恩希玛')


def tranlate(human):
    '''
    接收一个具备吃饭功能的Human对象
    :param human: Human对象
    :return:
    '''
    human.eat()
human = Human()
zh_human = ZhHuman()
us_human = UsHuman()
africa_human = AfricaHuman()

tranlate(human)
tranlate(zh_human)
tranlate(us_human)
tranlate(africa_human)

class Dog:
    def eat(self):
        print('狗吃骨头')

def tranlate(human):
    '''
    接收一个具备吃饭功能的Human对象
    :param human: Human对象
    :return:
    '''
    human.eat()

dog = Dog()
tranlate(dog)