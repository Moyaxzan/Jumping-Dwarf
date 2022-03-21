import sys

import pygame

from settings import *
from map import *


# Pygame init
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
world = Map(map_list, screen)
hold = False
hold_value = 0
pressed = False
# test_tile = pygame.sprite.Group(Tile((40, 40), 40))

while True:
    pygame.display.update()
    screen.fill("purple")
    clock.tick(60)
    world.run()
    for event in pygame.event.get():
        player = world.player.sprite
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if hold and (player.direction.y == player.gravity or player.direction.y == 0):
            hold_value += 6
            print(hold_value)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                hold = True
                pressed = True
        elif event.type == pygame.KEYUP:
            hold = False
        if ((not hold and pressed) or (hold_value > 95)) and (player.direction.y == player.gravity or player.direction.y == 0):
            player.jump1(hold_value)
            hold_value = 0
            pressed = False
            hold = False






