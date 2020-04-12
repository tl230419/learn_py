for ele in range(100, 1000):
    hun = ele // 100
    ten = ele % 100 // 10
    single = ele % 10
    if (hun ** 3 + ten ** 3 + single ** 3 == ele):
        print(ele)

print('number:')
for hun in range(1, 5):
    for ten in range(1, 5):
        for single in range(1, 5):
            if (hun != ten) and (ten != single) and (hun != single):
                num = hun * 100 + ten * 10 + single
                print(num)

str = 'hello world'
for ele in str:
    print(ele)
else:
    print('执行了else语句')

for ele in str:
    if ele == 'l':
        continue
    print(ele)
else:
    print('执行了else语句')

for ele in str:
    if ele == 'l':
        break
    print(ele)
else:
    print('执行了else语句')

str = 'hhew2383dW_fkfE'
container = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_'
for ele in str:
    if ele in container:
        pass
    else:
        print('密码不合法')
        break
else:
    print('密码合法')