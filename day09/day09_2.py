'''
*****************
Date: 2020-04-16
Author: Allen
*****************
'''

import pygame
from pygame.locals import *
import sys
import random

pygame.init()

window_w = 344
window_h = 476

window = pygame.display.set_mode(size=(window_w, window_h))
pygame.display.set_caption('飞机大战')

icon_surface = pygame.image.load('img/app.ico')
pygame.display.set_icon(icon_surface)

bg_surface = pygame.image.load('img/img_bg_level_1.jpg')
hero_surface = pygame.image.load('img/hero2.png')

class Plane:
    def __init__(self, x, y, window):
        self.x = x
        self.y = y
        self.window = window
        self.surface = pygame.image.load('img/hero2.png')
        self.width = self.surface.get_width()
        self.height = self.surface.get_height()
        self.bullets = []
        self.hp = 100

    def display(self):
        print(len(self.bullets))
        self.window.blit(self.surface, (self.x, self.y))

        for enemy in enemy_list:
            if self.has_collision(enemy):
                enemy.reset()
                self.hp -= 1
                break

        for bullet in self.bullets:
            for enemy in enemy_list:
                if bullet.has_collision(enemy):
                    self.bullets.remove(bullet)
                    enemy.reset()
                    break

        for bullet in self.bullets:
            if bullet.need_destroy():
                print('需要销毁')
                self.bullets.remove(bullet)

        for bullet in self.bullets:
            bullet.display()

    def move_left(self):
        self.x -= 1
        if self.x < 0:
            self.x = 0

    def move_right(self):
        self.x += 1
        if self.x > window_w - self.width:
            self.x = window_w - self.width

    def move_up(self):
        self.y -= 1
        if self.y < 0:
            self.y = 0

    def move_down(self):
        self.y += 1
        if self.y > window_h - self.height:
            self.y = window_h - self.height

    def fire(self):
        bullet = Bullet(self.window, self.x, self.y, self.width)
        self.bullets.append(bullet)

    def has_collision(self, enemy):
        bullet_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        enemy_rect = pygame.Rect(enemy.x, enemy.y, enemy.width, enemy.height )
        return bullet_rect.colliderect(enemy_rect)

class Bullet:
    def __init__(self, window, px, py, pw):
        self.surface = pygame.image.load('img/bullet.png')
        self.width = self.surface.get_width()
        self.height = self.surface.get_height()
        self.window = window
        self.x = px + (pw - self.width) / 2
        self.y = py - self.height / 2

    def display(self):
        self.window.blit(self.surface, (self.x, self.y))
        #self.y -= 2
        if not game_over:
            self.y -= 2

    def need_destroy(self):
        return self.y < -self.height

    def has_collision(self, enemy):
        bullet_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        enemy_rect = pygame.Rect(enemy.x, enemy.y, enemy.width, enemy.height )
        return bullet_rect.colliderect(enemy_rect)

class EnemyPlane:
    def __init__(self, window):
        self.window = window
        self.surface = pygame.image.load('img/img_plane_1.png')
        self.width = self.surface.get_width()
        self.height = self.surface.get_height()
        self.x = 100
        self.y = -self.height + 100

    def display(self):
        self.window.blit(self.surface, (self.x, self.y))
        #self.y += 1
        if self.y > window_h:
            self.reset()

        if not game_over:
            self.y += 1

    def reset(self):
        self.window = window
        self.surface = pygame.image.load('img/img_plane_{}.png'.format(random.randint(1, 7)))
        self.width = self.surface.get_width()
        self.height = self.surface.get_height()
        self.x = random.randint(0, window_w - self.width)
        self.y = -self.height

plane = Plane(window_w / 2 - 100 , 360, window)
enemy = EnemyPlane(window)
enemy_list = []

font = pygame.font.Font('font/happy2.ttf', 50)
font_w = 50
font_h = 50
game_over_surface = font.render('游戏结束', True, (255, 255, 255))

game_over = False

for index in range(0, 3):
    enemy = EnemyPlane(window)
    enemy_list.append(enemy)

while True:
    window.blit(bg_surface, (0, 0))
    #window.blit(hero_surface, (0, 0))
    plane.display()
    #enemy.display()
    for index in enemy_list:
        enemy.display()

    if plane.hp <= 0:
        game_over = True
        window.blit(game_over_surface, ((window_w - font_w) / 2, (window_h - font_h) / 2))

    pygame.display.flip()

    event_list = pygame.event.get()
    for event in event_list:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_a:
                plane.move_left()
            elif event.key == K_d:
                plane.move_right()
            elif event.key == K_w:
                plane.move_up()
            elif event.key == K_s:
                plane.move_down()
            elif event.key == K_RETURN:
                plane.fire()

