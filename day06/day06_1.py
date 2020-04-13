'''
*****************
Date: 2020-04-13
Author: Allen
*****************
'''

def say_hello(name='林青霞'):
    '''
    给女神打招呼
    :param name:
    :return:
    '''
    print('hello %s'%(name))

say_hello()
say_hello('高圆圆')

def say_hello(score,name='林青霞'):
    '''
    给女神大招
    :param score:
    :param name:
    :return:
    '''
    print('hello %s'%(name))

say_hello(60, '高圆圆')

def say_hello(name,age,score):
    print('姓名:%s,年纪:%d,分数:%f'%(name,age,score))

say_hello(name='林青霞',age=60,score=70.5)
say_hello(score=70,age=30,name='高圆圆')

def send_request(path,method='GET'):
    print('请求地址：%s,请求方式:%s'%(path,method))

send_request('http://www.toutiao.com')
send_request('http://toutiao.login.com','POST')