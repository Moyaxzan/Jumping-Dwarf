import sys

import pygame

from settings import *
from map import *


# Pygame init
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
world = Map(map_list, screen)
hold = 0
# test_tile = pygame.sprite.Group(Tile((40, 40), 40))

while True:
    pygame.display.update()
    screen.fill("purple")
    clock.tick(60)
    world.run()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        while event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and hold < 120:
                print(hold)
                hold += 1
            else:
                break
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                player = world.player.sprite
                print(hold)
                player.direction.y = -10 - hold/2
                hold = 0





