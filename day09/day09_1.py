'''
*****************
Date: 2020-04-16
Author: Allen
*****************
'''

'''

import pygame

pygame.init()

pygame.display.set_mode(size=(800, 800))

while True:
    pass
    
'''

'''
import pygame
from pygame.locals import *
import sys

pygame.init()

window = pygame.display.set_mode(size=(800, 800))
while True:
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == QUIT:
            pygame.display.quit()
            sys.exit()
'''

'''
import pygame
from pygame.locals import *
import sys

pygame.init()

window = pygame.display.set_mode(size=(800, 800))
pygame.display.set_caption('飞机大战')

icon = pygame.image.load('img/app.ico')
pygame.display.set_icon(icon)

while True:
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == QUIT:
            pygame.display.quit()
            sys.exit()
'''

'''
import pygame
from pygame.locals import *
import sys

pygame.init()

window = pygame.display.set_mode(size=(800, 800))
pygame.display.set_caption('飞机大战')

icon = pygame.image.load('img/app.ico')
pygame.display.set_icon(icon)

hero_img = pygame.image.load('img/hero2.png')

while True:
    window.blit(hero_img, (40, 40))
    pygame.display.flip()

    event_list = pygame.event.get()
    for event in event_list:
        if event.type == QUIT:
            pygame.display.quit()
            sys.exit()
'''

'''
import pygame
from pygame.locals import *
import sys

pygame.init()

window = pygame.display.set_mode(size=(800, 800))

while True:
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == QUIT:
            pygame.display.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_a:
                print('向左')
            elif event.key == K_d:
                print('向右')
            elif event.key == K_w:
                print('向前')
            elif event.type == K_s:
                print('向后')
            elif event.key == K_RETURN:
                print('点击了enter键')
'''

'''
import pygame
from pygame.locals import *
import sys

pygame.init()

window = pygame.display.set_mode(size=(800, 800))
font = pygame.font.Font('font/happy.ttf', 50)
font_surface = font.render('游戏开始', True, (255,255,255))

while True:
    window.blit(font_surface, (200, 200))
    pygame.display.flip()

    event_list = pygame.event.get()
    for event in event_list:
        if event.type == QUIT:
            pygame.display.quit()
            sys.exit()
'''

'''
import pygame
from pygame.locals import *
import sys

pygame.init()

window = pygame.display.set_mode(size=(800, 800))
pygame.mixer.music.load('snd/bomb.wav')

while True:
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == QUIT:
            pygame.display.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_RETURN:
                pygame.mixer.music.play(loops=-1)
'''

'''
import pygame
from pygame.locals import *
import sys

pygame.init()

window = pygame.display.set_mode(size=(800, 800))
sn = pygame.mixer.Sound('snd/bomb.wav')

while True:
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == QUIT:
            pygame.display.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_a:
                sn.stop()
            elif event.key == K_RETURN:
                sn.play(loops=-1)
'''

import pygame
from pygame.locals import *
import sys
import time

pygame.init()

window = pygame.display.set_mode(size=(800, 800))
pygame.display.set_caption('飞机大战')

icon = pygame.image.load('img/app.ico')
pygame.display.set_icon(icon)

hero_img = pygame.image.load('img/hero2.png')

hero_x = 200
hero_y = 200

while True:
    start_time = time.time()

    window.fill((0, 0, 0))

    window.blit(hero_img, (hero_x, hero_y))
    pygame.display.flip()

    event_list = pygame.event.get()
    for event in event_list:
        if event.type == QUIT:
            pygame.display.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_a:
                hero_x -= 10
            elif event.key == K_d:
                hero_x += 10
            elif event.key == K_w:
                hero_y -= 10
            elif event.key == K_s:
                hero_y += 10

    time.sleep(0.008)
    end_time = time.time()
    render_time = end_time - start_time
    try:
        fps = int(1 / render_time)
        print(fps)
    except:
        pass