'''
*****************
Date: 2020-04-13
Author: Allen
*****************
'''

l = [ele for ele in range(1, 10001)]
print(l)

t = (ele for ele in range(1, 100))
print(t)

s = {ele for ele in range(1, 101)}
print(s)

d = {key:value for key,value in zip(range(1,10),range(21,30))}
print(d)

l = [ele for ele in range(1, 101)]
print(l)
new_l = [l[ele:ele+3] for ele in range(0,len(l)) if ele %3 == 0]
print(new_l)