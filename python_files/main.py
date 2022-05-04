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
direction = "None"

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
            hold_value += 10
            held = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                hold = True
                pressed = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                hold = False
                held = False
        if ((not hold and pressed) or (hold_value > 110)) and (player.direction.y == player.gravity or
                                                              player.direction.y == 0):
            for event2 in events:
                if event2.type == pygame.KEYDOWN:
                    print(event2.key == pygame.K_LEFT, "ooOOooOoOoOOoo")
                    if event2.key == pygame.K_LEFT or event2.key == pygame.K_q:
                        direction = "left"
                        print("left")
                    if event2.key == pygame.K_RIGHT or event2.key == pygame.K_d:
                        direction = "right"
                        print("right")
                    else:
                        direction = "None"
            player.jump1(hold_value, direction)
            hold_value = 0
            pressed = False
            hold = False
    world.run(held)






