'''
*****************
Date: 2020-04-13
Author: Allen
*****************
'''

'''
my = int(input('请输入出拳：'))

com = 1

if (my == 1 and com == 2) or (my == 2 and com == 3)\
    or (my == 3 and com == 1):
    print('用户胜利，my=%d,com=%d'%(my,com))
elif my == com:
    print('平局，决战到天亮')
else:
    print('电脑胜利，my=%d,com=%d' % (my, com))
'''

import random

my = int(input('请输入出拳：'))

com = random.randint(1, 3)
print(com)

if (my == 1 and com == 2) or (my == 2 and com == 3)\
    or (my == 3 and com == 1):
    print('用户胜利，my=%d,com=%d'%(my,com))
elif my == com:
    print('平局，决战到天亮')
else:
    print('电脑胜利，my=%d,com=%d' % (my, com))