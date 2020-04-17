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

FPS = 5
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
CELL_SIZE = 20

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

CELL_WIDTH = 20
CELL_HEIGHT = 20

apple = {}

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    BASICFONT = pygame.font.Font('resources/ARBERKLEY.ttf', 18)
    pygame.display.set_caption('Snake')
    show_start_screen()

    while True:
        run_game()

        show_game_over_screen()

def terminate():
    pygame.quit()
    sys.exit()

def check_for_key_press():
    if len(pygame.event.get(QUIT)) > 0:
        terminate()

    key_up_events = pygame.event.get(KEYUP)
    if len(key_up_events) == 0:
        return None
    if key_up_events[0].key == K_ESCAPE:
        terminate()
    return key_up_events[0].key

def draw_press_key_msg():
    press_key_surf = BASICFONT.render('Press a key to play.', True, RED)
    press_key_rect = press_key_surf.get_rect()
    press_key_rect.topleft = (WINDOW_WIDTH - 200, WINDOW_HEIGHT - 30)
    DISPLAYSURF.blit(press_key_surf, press_key_rect)

def show_start_screen():
    DISPLAYSURF.fill(BGCOLOR)
    title_font = pygame.font.Font('resources/ARBERKLEY.ttf', 100)
    title_surf = title_font.render('Snake!', True, GREEN)
    title_rect = title_surf.get_rect()
    title_rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
    DISPLAYSURF.blit(title_surf, title_rect)
    draw_press_key_msg()

    pygame.display.update()
    while True:
        if check_for_key_press():
            pygame.event.get()
            return

def run_game():
    direction = RIGHT

    while True:
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

        start_x = random.randint(5, CELL_WIDTH - 6)
        start_y = random.randint(5, CELL_HEIGHT - 6)

        worm_coords = [{'x': start_x, 'y': start_y},
                       {'x': start_x - 1, 'y': start_y},
                       {'x': start_x - 2, 'y': start_y}]

        if direction == UP:
            new_head = {'x': worm_coords[HEAD]['x'], 'y': worm_coords[HEAD]['y'] - 1}
        elif direction == DOWN:
            new_head = {'x': worm_coords[HEAD]['x'], 'y': worm_coords[HEAD]['y'] + 1}
        elif direction == LEFT:
            new_head = {'x': worm_coords[HEAD]['x'] - 1, 'y': worm_coords[HEAD]['y']}
        elif direction == RIGHT:
            new_head = {'x': worm_coords[HEAD]['x'] + 1, 'y': worm_coords[HEAD]['y']}

        worm_coords.insert(0, new_head)

        del worm_coords[-1]

        DISPLAYSURF.fill(BGCOLOR)

        draw_grid()

        pygame.display.update()

        FPSCLOCK.tick(FPS)

        draw_score(len(worm_coords) - 3)

        if worm_coords[HEAD]['x'] == -1 or worm_coords[HEAD]['x'] == CELL_WIDTH  or worm_coords[HEAD]['x'] == -1 or worm_coords[HEAD]['x'] == CELL_HEIGHT:
            return

        for worm_body in worm_coords[1:]:
            if worm_body['x'] == worm_coords[HEAD]['x'] or worm_body['y'] == worm_coords[HEAD]['y']:
                return

        while True:
            draw_worm(worm_coords)

            draw_apple()

            if worm_coords[HEAD]['x'] == apple['x'] and worm_coords[HEAD]['y'] == apple['y']:
                apple = get_random_location()
            else:
                del worm_coords[-1]

def draw_worm(worm_coords):
    for coord in worm_coords:
        x = coord['x'] * CELL_SIZE
        y = coord['y'] * CELL_SIZE
        worm_segment_rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(DISPLAYSURF, DARKGREEN, worm_segment_rect)
        worm_inner_segment_rect = pygame.Rect(x + 4, y + 4, CELL_SIZE - 8, CELL_SIZE - 8)
        pygame.draw.rect(DISPLAYSURF, GREEN, worm_inner_segment_rect)

def get_random_location():
    return {'x': random.randint(0, CELL_WIDTH - 1), 'y': random.randint(0, CELL_HEIGHT - 1)}

def draw_score(score):
    score_surf = BASICFONT.render('Score: %s'%(score), True, WHITE)
    score_rect = score_surf.get_rect()
    score_rect.topleft = (WINDOW_WIDTH - 120, 10)
    DISPLAYSURF.blit(score_surf, score_rect)

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

def draw_apple():
    x = apple['x'] * CELL_SIZE
    y = apple['y'] * CELL_SIZE
    apple_rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(DISPLAYSURF, RED, apple_rect)

if __name__ == '__main__':
    main()