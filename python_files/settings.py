from sys import exit
from Buttons import *


def Menu(screen):
    with open("../assets/bg/menu.gif") as bg:
        display = pygame.image.load(bg)
        display = pygame.transform.scale(display, (screen_width, screen_height))
    clock = pygame.time.Clock()
    stay_in_menu = True
    while stay_in_menu:
        pygame.display.update()
        clock.tick(30)

        start_button = Button.draw(Button(screen, (screen_width*0.363, screen_height*0.523), (400, 100), "red"))
        quit_button = Button.draw(Button(screen, (screen_width*0.376, screen_height*0.657), (300, 100), "blue"))
        screen.blit(display, (0, 0))

        events = pygame.event.get()
        for ev in events:
            if ev.type == pygame.QUIT or (ev.type == pygame.MOUSEBUTTONDOWN and quit_button.collidepoint(pygame.mouse.get_pos())):
                pygame.quit()
                exit()
            if ev.type == pygame.MOUSEBUTTONDOWN and start_button.collidepoint(pygame.mouse.get_pos()):
                stay_in_menu = False
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