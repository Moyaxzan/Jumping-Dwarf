from sys import exit
import pygame.transform
from Animation import *


def Homepage(screen):
    pygame.mixer.init()
    pygame.mixer.stop()
    music_menu = pygame.mixer.Sound("../audio/homepage.wav")
    pygame.mixer.Sound.play(music_menu, loops=1000)
    # Allows to animate the background.
    Anime = Animation()
    clock = pygame.time.Clock()
    stay_in_menu = True
    stay_in_settings = False

    # Iterates while the player hasn't open the door or leave the game.
    while stay_in_menu:
        # Loads the different needed animations.
        display = pygame.image.load(Anime.launch_gif("sprite_menu","menu_bg",6,.1))
        display = pygame.transform.scale(display, (screen_width, screen_height))
        quit_animation = pygame.image.load(Anime.launch_gif("quit","menu_bg",6,.15))
        cog_button = pygame.draw.rect(screen,"purple", ((screen_width-120,10),(50,50)))
        cog = pygame.transform.scale(pygame.image.load("../assets/settings/settings_icone.png"), (50,50))
        # Loads the closed door.
        with open("../assets/menu_bg/closed_door.png") as closed_door:
                    door_display = pygame.image.load(closed_door)
                    door_pos = (screen_width * 0.022, screen_height * 0.491)
                    door_dims = (screen_width * 0.1, screen_height * 0.3)
        # Creates the start and quit buttons.
        start_button = pygame.draw.rect(screen, "red", (door_pos, door_dims))
        quit_button = pygame.draw.rect(screen, "blue", ((screen_width*0.3, screen_height*0.825), (300, 100)))
        clock.tick(30)
        # Loads the opened door.
        if not stay_in_settings and start_button.collidepoint(pygame.mouse.get_pos()):
            with open("../assets/menu_bg/opened_door.png") as opened_door:
                door_display = pygame.image.load(opened_door)
                door_pos = (screen_width * 0.022, screen_height * 0.491)
                door_dims = (screen_width * 0.1, screen_height * 0.3*1.075)
        # Displays door and quit button.
        door_display = pygame.transform.scale(door_display,door_dims)
        quit_animation = pygame.transform.scale(quit_animation,(screen_height*1.7, screen_width*.7))
        screen.blit(display, (0,0))
        screen.blit(cog, (screen_width-120,10))
        screen.blit(door_display,door_pos)
        screen.blit(quit_animation,(-screen_width*.03, -screen_height*.07))
        events = pygame.event.get()
        for ev in events:
            # Checks if the player tried to close the window or clicked on quit button.
            if ev.type == pygame.QUIT or (not stay_in_settings and ev.type == pygame.MOUSEBUTTONDOWN and quit_button.collidepoint(pygame.mouse.get_pos())):
                pygame.quit()
                exit()
            # Checks if the player clicked on the door, and if so, starts the game.
            if not stay_in_settings:
                if ev.type == pygame.MOUSEBUTTONDOWN and start_button.collidepoint(pygame.mouse.get_pos()):
                    fade_transi(screen,"out",1)
                    stay_in_menu = False
                    pygame.mixer.fadeout(2000)
                    music_game = pygame.mixer.Sound("../audio/leujeu.wav")
                    pygame.mixer.Sound.play(music_game, loops=10000000)
                if (ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE) or (ev.type == pygame.MOUSEBUTTONDOWN and cog_button.collidepoint(pygame.mouse.get_pos())):
                    stay_in_settings = True
        if stay_in_settings:
            stay_in_settings, stay_in_menu = settings(screen, stay_in_settings, stay_in_menu)
        pygame.display.update()

    return stay_in_menu

# Displays the ending screen
def ending(screen):
    pygame.mixer.stop()
    end_music = pygame.mixer.Sound("../audio/end.wav")
    pygame.mixer.Sound.play(end_music)
    fade_transi(screen, "in", 3)
    while True:
        end = pygame.transform.scale(pygame.image.load(r"../assets/divers/ending_screen.png"), (screen_width, screen_height))
        screen.blit(end, (0, 0))
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        pygame.display.update()

# Displays and allows the user to modify basic settings
def settings(screen, stay_in_settings, go_to_menu):
    settings_bg = pygame.draw.rect(screen, "green", ((screen_width*.135, screen_height*.135),(screen_width*.75,screen_height*.75)))
    return_home_button = pygame.draw.rect(screen,"white", ((screen_width*.48, screen_height*.7), (screen_width*.07,screen_height*.127)))
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            stay_in_settings = False
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and return_home_button.collidepoint(pygame.mouse.get_pos()):
            stay_in_settings = False
            go_to_menu = True
    pygame.display.update()
    return stay_in_settings,go_to_menu

# Creates a fading transition from/to black screen
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
    "s            o      Oo W",
    "      C       oOOoO    W",
    "          oO           W",
    "                       W",
    "                     B W",
    "W                      W",
    "W                  GGGW",
    "W                     W",
    "W                     W",
    "W         P           W",
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
    "Ww                    W",
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
    "W            F        W",
    "W          GGG        W",
    "W                     W",
    "W                     W",
    "W                     W",
    "W   GGGGG             W",
    "W                     W",
    "W                     W",
    "W                     W",
    "W    F          R     W",
    "DGGGGGGGGGGGGGGGGGGGGGD"]


# Settings for the window to be sized correctly
screen_width = 60 * len(map_list[len(map_list) - 1])
screen_height = 12 * 60