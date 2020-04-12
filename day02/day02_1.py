'''
i = 1
while i <= 10000:
    print('媳妇儿，我错了')
    i += 1
'''

#while True:
#    pass

'''
row = int(input("请输入打印的行数："))
n = row
while n >= 0:
    x = "*" * n
    print(x)
    n -= 1
'''

'''
n = int(input("Enter the number of rows:"))
i = 1
while i <= n:
    print("*" * i)
    i += 1
'''

'''
row = int(input("Enter the number of rows:"))
n = row
while n >= 0:
    x = "*" * n
    y = " " * (row - n)
    print(y + x)
    n -= 1
'''

'''
i = 0
while i < 5:
    if i == 3:
        break
    print(i)
    i += 1
'''

'''
i = 0
while i < 5:
    i += 1
    if i - 1 == 3:
        continue
    print(i - 1)
'''

i = 0
while i < 5:
    j = 0
    while j < 3:
        print(j)
        j += 1
    i += 1
