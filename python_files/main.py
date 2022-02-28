import sys

import pygame

from settings import *
from map import *


# Pygame init
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
world = Map(map_list, screen)
# test_tile = pygame.sprite.Group(Tile((40, 40), 40))

while True:
    pygame.display.update()
    screen.fill("black")
    clock.tick(60)
    world.run()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        world.player_group.update("x", -5)
    if keys[pygame.K_RIGHT]:
        world.player_group.update("x", 5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



