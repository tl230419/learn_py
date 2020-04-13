'''
*****************
Date: 2020-04-13
Author: Allen
*****************
'''

import random

while_balls = ['白','白','白','白']
red_balls = ['红','红','红']
blue_balls = ['蓝','蓝','蓝']

boxes = [[],[],[]]
for box in boxes:
    box.append(while_balls.pop(while_balls.index('白')))

print(boxes)

l = while_balls + red_balls + blue_balls
while_balls.clear()
red_balls.clear()
blue_balls.clear()

for ball in l:
    index = random.randint(0, 2)
    box = boxes[index]
    box.append(ball)

print(boxes)