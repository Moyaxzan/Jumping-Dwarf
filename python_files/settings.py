import pygame

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
    "X          P          X",
    "X          XX         X",
    "X                     X",
    "X   P                 X",
    "X   X                 X",
    "X                     X",
    "X                     X",
    "X       XX            X",
    "X                     X",
    "X                     X",
    "X                     X",
    "XXXXXX                X",
    "XXXXXX                X",
    "XXXXXXXXXXXXXXXXXXXXXXX"]

tile_size = 60
screen_width = tile_size * len(map_list[1])
screen_height = 12 * tile_size
