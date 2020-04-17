'''
*****************
Date: 2020-04-17
Author: Allen
*****************
'''

import pygame
from pygame.locals import *
import sys
import random

# 屏幕刷新率（在这里相当于贪吃蛇的速度）
FPS = 5
# 屏幕宽度
WINDOW_WIDTH = 640
# 屏幕高度
WINDOW_HEIGHT = 480
# 小方格的大小
CELL_SIZE = 20

# 定义常用颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARKGREEN = (0, 155, 0)
DARKGRAY = (40, 40, 40)
BGCOLOR = BLACK

LEFT = 1
RIGHT = 2
UP = 3
DOWN = 4
HEAD = 0

CELL_WIDTH = int(WINDOW_WIDTH / CELL_SIZE)
CELL_HEIGHT = int(WINDOW_HEIGHT / CELL_SIZE)

def main():
    # 定义全局变量
    global FPSCLOCK, DISPLAYSURF, BASICFONT
    pygame.init()
    # 获得pygame时钟
    FPSCLOCK = pygame.time.Clock()
    # 设置屏幕宽高
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    # 设置基本字体
    BASICFONT = pygame.font.Font('resources/ARBERKLEY.ttf', 18)
    pygame.display.set_caption('Snake')
    # 显示游戏开始画面
    show_start_screen()

    while True:
        # 这里一直循环于游戏运行时和显示游戏结束画面之间，运行游戏里有一个循环，显示游戏结束画面也有一个循环，两个循环都有相应的return，这样就可以达到切换这两个模块的效果

        # 运行游戏
        run_game()

        # 显示游戏结束画面
        show_game_over_screen()

# 退出游戏
def terminate():
    pygame.quit()
    sys.exit()

# 检测按键事件
def check_for_key_press():
    if len(pygame.event.get(QUIT)) > 0:
        terminate()

    key_up_events = pygame.event.get(KEYUP)
    if len(key_up_events) == 0:
        return None
    if key_up_events[0].key == K_ESCAPE:
        terminate()
    return key_up_events[0].key

# 提示按键消息
def draw_press_key_msg():
    press_key_surf = BASICFONT.render('Press a key to play.', True, RED)
    press_key_rect = press_key_surf.get_rect()
    press_key_rect.topleft = (WINDOW_WIDTH - 200, WINDOW_HEIGHT - 30)
    DISPLAYSURF.blit(press_key_surf, press_key_rect)

# 显示游戏开始画面
def show_start_screen():
    DISPLAYSURF.fill(BGCOLOR)
    title_font = pygame.font.Font('resources/ARBERKLEY.ttf', 100)
    title_surf = title_font.render('Snake!', True, GREEN)
    title_rect = title_surf.get_rect()
    title_rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
    DISPLAYSURF.blit(title_surf, title_rect)
    # 下方提示文字
    draw_press_key_msg()

    pygame.display.update()
    # 检查按键
    while True:
        if check_for_key_press():
            pygame.event.get()
            return

# 游戏运行时
def run_game():
    # 随机初始化设置一个点作为贪吃蛇的起点
    start_x = random.randint(5, CELL_WIDTH - 6)
    start_y = random.randint(5, CELL_HEIGHT - 6)

    # 以这个点为起点，建立一个长度为3格的贪吃蛇（列表）
    worm_coords = [{'x': start_x, 'y': start_y},
                   {'x': start_x - 1, 'y': start_y},
                   {'x': start_x - 2, 'y': start_y}]

    # 初始化一个运动的方向
    direction = RIGHT

    apple = get_random_location()

    # 游戏主循环
    while True:
        # 事件处理
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if (event.key == K_LEFT or event.key == K_a) and (direction != RIGHT):
                    direction = LEFT
                elif (event.key == K_RIGHT or event.key == K_d) and (direction != LEFT):
                    direction = RIGHT
                elif (event.key == K_UP or event.key == K_w) and (direction != DOWN):
                    direction = UP
                elif (event.key == K_DOWN or event.key == K_s) and (direction != UP):
                    direction = DOWN
                elif event.key == K_ESCAPE:
                    terminate()

        # 根据方向，添加一个新的蛇头，以这种方式来移动贪吃蛇
        if direction == UP:
            new_head = {'x': worm_coords[HEAD]['x'], 'y': worm_coords[HEAD]['y'] - 1}
        elif direction == DOWN:
            new_head = {'x': worm_coords[HEAD]['x'], 'y': worm_coords[HEAD]['y'] + 1}
        elif direction == LEFT:
            new_head = {'x': worm_coords[HEAD]['x'] - 1, 'y': worm_coords[HEAD]['y']}
        elif direction == RIGHT:
            new_head = {'x': worm_coords[HEAD]['x'] + 1, 'y': worm_coords[HEAD]['y']}

        # 插入新的蛇头在数组的最前面
        worm_coords.insert(0, new_head)

        # 检查贪吃蛇是否撞到撞到边界，即检查蛇头的坐标
        if worm_coords[HEAD]['x'] == -1 or worm_coords[HEAD]['x'] == CELL_WIDTH  or worm_coords[HEAD]['y'] == -1 or worm_coords[HEAD]['y'] == CELL_HEIGHT:
            # game over
            return

        # 检查贪吃蛇是否撞到自己，即检查蛇头的坐标是否等于蛇身的坐标
        for worm_body in worm_coords[1:]:
            if worm_body['x'] == worm_coords[HEAD]['x'] and worm_body['y'] == worm_coords[HEAD]['y']:
                # game over
                return

        # 检查贪吃蛇是否吃到苹果，若没吃到，则删除尾端，蛇身前进一格
        if worm_coords[HEAD]['x'] == apple['x'] and worm_coords[HEAD]['y'] == apple['y']:
            # 不移除蛇的最后一个尾巴格
            # 重新随机生成一个苹果
            apple = get_random_location()
        else:
            # 移除蛇的最后一个尾巴格
            del worm_coords[-1]

        # 绘制背景
        DISPLAYSURF.fill(BGCOLOR)

        # 绘制所有的方格
        draw_grid()

        # 绘制贪吃蛇
        draw_worm(worm_coords)

        # 绘制苹果
        draw_apple(apple)

        # 绘制分数（分数为贪吃蛇列表当前的长度-3）
        draw_score(len(worm_coords) - 3)

        # 更新屏幕
        pygame.display.update()

        # 设置帧率
        FPSCLOCK.tick(FPS)

# 根据worm_coords列表绘制贪吃蛇
def draw_worm(worm_coords):
    for coord in worm_coords:
        x = coord['x'] * CELL_SIZE
        y = coord['y'] * CELL_SIZE
        worm_segment_rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(DISPLAYSURF, DARKGREEN, worm_segment_rect)
        worm_inner_segment_rect = pygame.Rect(x + 4, y + 4, CELL_SIZE - 8, CELL_SIZE - 8)
        pygame.draw.rect(DISPLAYSURF, GREEN, worm_inner_segment_rect)

# 随机生成一个苹果的坐标位置
def get_random_location():
    return {'x': random.randint(0, CELL_WIDTH - 1), 'y': random.randint(0, CELL_HEIGHT - 1)}

# 显示分数
def draw_score(score):
    score_surf = BASICFONT.render('Score: %s'%(score), True, WHITE)
    score_rect = score_surf.get_rect()
    score_rect.topleft = (WINDOW_WIDTH - 120, 10)
    DISPLAYSURF.blit(score_surf, score_rect)

# 显示游戏结束画面
def show_game_over_screen():
    game_over_font = pygame.font.Font('resources/ARBERKLEY.ttf', 50)
    game_surf = game_over_font.render('Game', True, WHITE)
    over_surf = game_over_font.render('Over', True, WHITE)
    game_rect = game_surf.get_rect()
    over_rect = over_surf.get_rect()
    game_rect.midtop = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 - game_rect.height - 10)
    over_rect.midtop = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)

    DISPLAYSURF.blit(game_surf, game_rect)
    DISPLAYSURF.blit(over_surf, over_rect)
    draw_press_key_msg()
    pygame.display.update()
    pygame.time.wait(500)
    check_for_key_press()

    while True:
        if check_for_key_press():
            pygame.event.get()
            return

def draw_grid():
    for x in range(0, WINDOW_WIDTH, CELL_SIZE):
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (x, 0), (x, WINDOW_HEIGHT))
    for y in range(0, WINDOW_HEIGHT, CELL_SIZE):
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (0, y), (WINDOW_WIDTH, y))

def draw_apple(apple):
    x = apple['x'] * CELL_SIZE
    y = apple['y'] * CELL_SIZE
    apple_rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(DISPLAYSURF, RED, apple_rect)

if __name__ == '__main__':
    main()