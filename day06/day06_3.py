'''
*****************
Date: 2020-04-13
Author: Allen
*****************
'''

def func(n):
    '''
    求n的阶乘
    :param n: 需要求的阶乘
    :return: n的阶乘
    '''
    if n == 1:
        return 1
    else:
        return n * func(n - 1)

r = func(5)
print(r)