'''
*****************
Date: 2020-04-13
Author: Allen
*****************
'''

'''
row = 1
while row < 10:
    col = 1
    while col <= row:
        #print('*', end='')
        print('%d * %d = %d'%(col, row, col*row), end='\t')
        col += 1
    print()
    row += 1
'''

row = 9
while row > 0:
    col = 1
    while col <= row:
        # print('*', end='')
        print('%d * %d = %d' % (col, row, col * row), end='\t')
        col += 1
    print()
    row -= 1