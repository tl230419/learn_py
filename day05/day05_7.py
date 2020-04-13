'''
*****************
Date: 2020-04-13
Author: Allen
*****************
'''

while True:
    str = input('请输入字符串')
    if len(str) >= 31:
        print('不能超过31位，请重新输入')
        continue
    break
print('输入正确')
print('您输入的字符串：%s'%str)
print('长度：%d'%len(str))
new_str = str[::-1]
print(new_str)
result_dict = {}
for ele in str:
    if ele not in result_dict:
        result_dict[ele] = 1
    else:
        result_dict[ele] += 1
print('字符统计结果：{}'.format(result_dict))