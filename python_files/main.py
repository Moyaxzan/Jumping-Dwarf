import sys
import time

import pygame

from Map import *


if __name__ == '__main__':
    # Pygame init
    pygame.init()
    icon = pygame.image.load(r'../assets/divers/icon.png')
    pygame.display.set_icon(icon)
    pygame.display.set_caption("Jumping Dwarf")
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((screen_width, screen_height))
    world = Map(map_list, screen)
    hold = False
    hold_value = 0
    pressed = False
    held = False
    play_the_game = False

    while True:
        if not play_the_game:
            Menu(screen)
            play_the_game = True
        pygame.event.set_blocked(pygame.MOUSEMOTION)
        worldshift = 0
        pygame.display.update()
        screen.fill("cyan")
        clock.tick(60)
        events = pygame.event.get()
        player = world.player.sprite

        if player.get_y() < 0:
            worldshift = screen_height
            player.set_y(player.get_y() + screen_height)
        elif player.get_y() > screen_height:
            worldshift = -screen_height
            player.set_y(player.get_y() - screen_height)

        for event in events:

            if event.type == pygame.QUIT:
                play_the_game = False
                pygame.quit()
                sys.exit()

            if hold and (player.on_ground(world)):
                hold_value += 1
                held = True
                player.image = pygame.image.load(player.anime.launch_gif("stacking_dwarf", "dwarf", 1, 0))

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
                    player.jump(hold_value)
                hold_value = 0
                pressed = False
                hold = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                play_the_game = False

        world.run(held, worldshift)

        if player.rect.colliderect(world.beer):
            ending(screen)