'''
*****************
Date: 2020-04-16
Author: Allen
*****************
'''

class Gun:
    def __init__(self, model, damage):
        '''
        初始化枪支
        :param model: 型号
        :param damage: 伤害
        '''
        self.model = model
        self.damage = damage
        self.bullet_count = 0

    def __str__(self):
        return '型号：{}，伤害：{}，子弹数量：{}'.format(self.model, self.damage, self.bullet_count)

    def add_bulltes(self, count):
        '''
        添加子弹
        :param count:
        :return:
        '''
        self.bullet_count += count
        print('添加子弹成功')

    def shoot(self, enemy):
        '''
        射击敌人
        :param enemy:
        :return:
        '''
        if self.bullet_count == 0:
            print('请填充子弹')
        else:
            self.bullet_count -= 1
            enemy.hurt(self)

class Player:
    def __init__(self, role):
        '''
        初始化玩家
        :param role:
        '''
        self.role = role
        self.hp = 100
        self.gun = None
        self.state = '活着'

    def __str__(self):
        return '角色：{}，状态：{}，血量：{}，枪支：{}'.format(self.role, self.state, self.hp, self.gun)

    def fire(self, enemy):
        '''
        射击敌人
        :param enemy:
        :return:
        '''
        if self.gun:
            if self.gun.bullet_count > 0:
                self.gun.shoot(enemy)
            else:
                self.gun.add_bulltes(5)
        else:
            print('现在还没有枪支')

    def hurt(self, enemy_gun):
        '''
        玩家受到伤害
        :param enemy_gun: 受到哪个枪支的伤害
        :return:
        '''
        self.hp -= enemy_gun.damage
        if self.hp <= 0:
            print('玩家：{}死亡'.format(self.role))
        else:
            print('玩家受伤，当前血量：{}'.format(self.hp))


gun = Gun('ak47', 10)
player1 = Player('警察')
player2 = Player('土匪')

player1.gun = gun

while player2.hp > 0:
    player1.fire(player2)