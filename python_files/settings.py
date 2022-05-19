from sys import exit
import pygame.transform
from Animation import *
from Buttons import *


def Menu(screen):
    Anime = Animation()
    clock = pygame.time.Clock()
    stay_in_menu = True

    while stay_in_menu:
        display = pygame.image.load(Anime.launch_gif("sprite_menu","menu_bg",6,.25))
        display = pygame.transform.scale(display, (screen_width, screen_height))
        with open("../assets/menu_bg/closed_door.png") as closed_door:
                    door_display = pygame.image.load(closed_door)
                    door_pos = (screen_width * 0.022,screen_height * 0.491)
                    door_dims = (screen_width * 0.1, screen_height * 0.3)
        start_button = Button.draw(Button(screen, door_pos, door_dims, "red"))
        screen.blit(display, (0, 0))
        quit_button = Button.draw(Button(screen, (screen_width*0.3, screen_height*0.825), (300, 100), "blue"))
        clock.tick(30)
        if start_button.collidepoint(pygame.mouse.get_pos()):
            with open("../assets/menu_bg/opened_door.png") as opened_door:
                door_display = pygame.image.load(opened_door)
                door_pos = (screen_width * 0.022, screen_height * 0.491)
                door_dims = (screen_width * 0.1, screen_height * 0.3*1.075)
        events = pygame.event.get()
        for ev in events:
            if ev.type == pygame.QUIT or (ev.type == pygame.MOUSEBUTTONDOWN and quit_button.collidepoint(pygame.mouse.get_pos())):
                pygame.quit()
                exit()
            if ev.type == pygame.MOUSEBUTTONDOWN and start_button.collidepoint(pygame.mouse.get_pos()):
                stay_in_menu = False
        door_display = pygame.transform.scale(door_display,door_dims)
        screen.blit(door_display,door_pos)
        pygame.display.update()
    return stay_in_menu


map_list = [
    "                       W",
    "                       W",
    "                       W",
    "                       W",
    "                       W",
    "W                   B  W",
    "W                  GGGW",
    "W                     W",
    "W                     W",
    "W                     W",
    "W        GG           W",
    "W        DD           W",
    "W                     W",
    "W                     W",
    "W   GG                W",
    "W                     W",
    "W                     W",
    "W                     W",
    "W                     W",
    "WGG       F           W",
    "W        GGGG         W",
    "W                     W",
    "W                GG   W",
    "W                     W",
    "W                     W",
    "W          GG         W",
    "W                     W",
    "W      F              W",
    "W    GGG              W",
    "W                     W",
    "W                     W",
    "W        F  F  FF     W",
    "W      GGGGGGGGGGG    W",
    "W                     W",
    "WWW                   W",
    "WWW                   W",
    "W                     W",
    "W    GG               W",
    "W                     W",
    "W                     W",
    "W                     W",
    "W          GG         W",
    "W                     W",
    "W                     W",
    "W  GG                 W",
    "W                     W",
    "W                     W",
    "W                     W",
    "W                     W",
    "W     GGG             W",
    "W                     W",
    "W                     W",
    "WWW                   W",
    "WWW                   W",
    "WWWW                  W",
    "WWWW    S      P      W",
    "WWWW   GG             W",
    "W             GG      W",
    "W                     W",
    "W                     W",
    "W                     W",
    "W                 GG  W",
    "W                     W",
    "W                     W",
    "W                     W",
    "W                   WWW",
    "W                WWWWWW",
    "WWWW             WWWWWW",
    "W                     W",
    "W                     W",
    "W        GG           W",
    "W                     W",
    "W                     W",
    "W F                   W",
    "WGGGGG                W",
    "WDDDD             GG  W",
    "WDDD                  W",
    "WDD                   W",
    "W                     W",
    "W        GGGG         W",
    "W                     W",
    "W                     W",
    "W                 G   W",
    "W                     W",
    "W                     W",
    "W                     W",
    "W                     W",
    "W                 GGGGW",
    "W                     W",
    "W                     W",
    "W                     W",
    "W          GGGG       W",
    "W                     W",
    "W F                   W",
    "WGGGGG                W",
    "WDDDDD                W",
    "W                     W",
    "W            F        W",
    "W          GGG        W",
    "W                     W",
    "W                     W",
    "W                     W",
    "W   GGGGG             W",
    "W                     W",
    "W                     W",
    "W    F                W",
    "DGGGGGGGGGGGGGGGGGGGGGD"]


screen_width = 60 * len(map_list[len(map_list) - 1])
screen_height = 12 * 60