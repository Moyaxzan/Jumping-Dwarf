import pygame

map_list =[
    "X                     X",
    "X                     X",
    "X                     X",
    "X                     X",
    "X                     X",
    "X                     X",
    "X                     X",
    "X                     X",
    "X                     X",
    "X     XXXX            X",
    "X                     X",
    "X                     X",
    "X                   XXX",
    "X                     X",
    "X                     X",
    "X                     X",
    "X                     X",
    "X           P         X",
    "X          XXX        X",
    "X                     X",
    "X                     X",
    "X                     X",
    "XXXXXX                X",
    "XXXXXX                X",
    "XXXXXXXXXXXXXXXXXXXXXXX"]

tile_size = 60
screen_width = tile_size * len(map_list[1])
screen_height = 12 * tile_size
