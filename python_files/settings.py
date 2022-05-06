from sys import exit
from Buttons import *

map_list =[
    "X                     X",
    "X                     X",
    "X                     X",
    "X                     X",
    "X      XXXXXXXXXXXXX  X",
    "X                     X",
    "X                     X",
    "XX                    X",
    "X    XX               X",
    "X                     X",
    "X                     X",
    "X                     X",
    "X          XX         X",
    "X                     X",
    "X                     X",
    "X   X                 X",
    "X                     X",
    "X                     X",
    "X       XX            X",
    "X                     X",
    "X                     X",
    "X                     X",
    "XXXXXX          P     X",
    "XXXXXX                X",
    "XXXXXXXXXXXXXXXXXXXXXXX"]

tile_size = 60
screen_width = tile_size * len(map_list[1])
screen_height = 12 * tile_size

def Menu(screen):
    with open("../assets/bg/menu.gif") as bg:
        display = pygame.image.load(bg)
        display = pygame.transform.scale(display, (screen_width,screen_height))
    clock = pygame.time.Clock()
    stay_in_menu = True
    while stay_in_menu:
        pygame.display.update()
        clock.tick(30)

        start_button = Button.draw(Button(screen, (screen_width*0.363, screen_height*0.523), (400,100), "red"))
        quit_button  = Button.draw(Button(screen, (screen_width*0.376, screen_height*0.657), (300,100), "blue"))
        screen.blit(display, (0, 0))

        events = pygame.event.get()
        for ev in events:
            if ev.type == pygame.QUIT or (ev.type == pygame.MOUSEBUTTONDOWN and quit_button.collidepoint(pygame.mouse.get_pos())):
                pygame.quit()
                exit()
            if ev.type == pygame.MOUSEBUTTONDOWN and start_button.collidepoint(pygame.mouse.get_pos()):
                stay_in_menu = False
    return stay_in_menu
