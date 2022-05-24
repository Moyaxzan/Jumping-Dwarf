from sys import exit
import pygame.transform
from Animation import *
from Buttons import *


def Menu(screen):
    pygame.mixer.init()
    music_menu = pygame.mixer.Sound("../audio/leumeunu.wav")
    pygame.mixer.Sound.play(music_menu, loops=1000)
    # Allows to animate the background.
    Anime = Animation()
    clock = pygame.time.Clock()
    stay_in_menu = True

    # Iterates while the player hasn't open the door or leave the game.
    while stay_in_menu:
        # Loads the different needed animations.
        display = pygame.image.load(Anime.launch_gif("sprite_menu","menu_bg",6,.1))
        display = pygame.transform.scale(display, (screen_width, screen_height))
        quit_animation = pygame.image.load(Anime.launch_gif("quit","menu_bg",6,.15))
        # Loads the closed door.
        with open("../assets/menu_bg/closed_door.png") as closed_door:
                    door_display = pygame.image.load(closed_door)
                    door_pos = (screen_width * 0.022, screen_height * 0.491)
                    door_dims = (screen_width * 0.1, screen_height * 0.3)
        # Creates the start and quit buttons.
        start_button = Button.draw(Button(screen, door_pos, door_dims, "red"))
        quit_button = Button.draw(Button(screen, (screen_width*0.3, screen_height*0.825), (300, 100), "blue"))
        clock.tick(30)
        # Loads the opened door.
        if start_button.collidepoint(pygame.mouse.get_pos()):
            with open("../assets/menu_bg/opened_door.png") as opened_door:
                door_display = pygame.image.load(opened_door)
                door_pos = (screen_width * 0.022, screen_height * 0.491)
                door_dims = (screen_width * 0.1, screen_height * 0.3*1.075)
        # Displays door and quit button.
        door_display = pygame.transform.scale(door_display,door_dims)
        quit_animation = pygame.transform.scale(quit_animation,(screen_height*1.7, screen_width*.7))
        screen.blit(display, (0,0))
        screen.blit(door_display,door_pos)
        screen.blit(quit_animation,(-screen_width*.03, -screen_height*.07))
        events = pygame.event.get()
        for ev in events:
            # Checks if the player tried to close the window or clicked on quit button.
            if ev.type == pygame.QUIT or (ev.type == pygame.MOUSEBUTTONDOWN and quit_button.collidepoint(pygame.mouse.get_pos())):
                pygame.quit()
                exit()
            # Checks if the player clicked on the door, and if so starts the game.
            if ev.type == pygame.MOUSEBUTTONDOWN and start_button.collidepoint(pygame.mouse.get_pos()):
                fade_transi(screen,"out",1)
                stay_in_menu = False
                pygame.mixer.fadeout(2000)
                music_game = pygame.mixer.Sound("../audio/leujeu.wav")
                pygame.mixer.Sound.play(music_game, loops=10000000)
        pygame.display.update()
    return stay_in_menu

def ending(screen):
    fade_transi(screen,"in",3)
    while True:
        end = pygame.transform.scale(pygame.image.load(r"../assets/divers/end.png"), (screen_width, screen_height))
        screen.blit(end, (0, 0))
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        pygame.display.update()

def fade_transi(screen,in_out,duration):
    fade = pygame.Surface((screen_width,screen_height)).convert()
    fade.fill((0,0,0))
    if in_out == "in":
        params = (100,1)
    else:
        params = (0,-1)
    for alpha in range(100):
        fade.set_alpha(params[0] - params[1]*alpha)
        screen.blit(fade,(0,0))
        pygame.display.update()
        pygame.time.wait(duration)



# List from which we get the map in map.py.
map_list = [
    "s                      W",
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
    "WWWW    S             W",
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
    "W                   N W",
    "W                  T  W",
    "WO                    W",
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
    "W                P    W",
    "W                     W",
    "W    F                W",
    "DGGGGGGGGGGGGGGGGGGGGGD"]


# Settings for the window to be sized correctly
screen_width = 60 * len(map_list[len(map_list) - 1])
screen_height = 12 * 60