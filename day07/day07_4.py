'''
*****************
Date: 2020-04-15
Author: Allen
*****************
'''

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.__PI = 3.1415926

    def perimeter(self):
        return 2 * self.__PI * self.radius

    def __say_hello(self):
        print('hello')

circle = Circle(10)
print(circle.perimeter())