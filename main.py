import pygame, sys
from settings import *
from tiles import Tile
from map import *


# Pygame init
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
map = Map(map_list, screen)
test_tile = pygame.sprite.Group(Tile((100,100),200))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        screen.fill("gray")
        map.run()
        pygame.display.update()
        clock.tick(60)
