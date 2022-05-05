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
held = False


# test_tile = pygame.sprite.Group(Tile((40, 40), 40))

while True:
    pygame.display.update()
    screen.fill("purple")
    clock.tick(60)
    events = pygame.event.get()
    for event in events:
        player = world.player.sprite
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if hold and (player.direction.y == player.gravity or player.direction.y == 0):
            hold_value += 1
            held = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                hold = True
                pressed = True
        elif event.type == pygame.KEYUP or hold_value > 11:
            if hold_value > 11:
                hold = False
                held = False
            elif event.key == pygame.K_SPACE:
                hold = False
                held = False
        if not hold and pressed and (player.direction.y == player.gravity or player.direction.y == 0):
            if player.on_ground(world):
                player.jump1(hold_value)
            hold_value = 0
            pressed = False
            hold = False
    world.run(held, world)






