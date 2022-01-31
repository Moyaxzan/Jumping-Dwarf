import pygame

map_list =[
    "X                       X",
    "X                       X",
    "X                       X",
    "X                       X",
    "X                       X",
    "X                       X",
    "X                       X",
    "X                       X",
    "X                       X",
    "X                       X",
    "X                       X",
    "X                       X",
    "X                       X",
    "X                       X",
    "X              XXX      X",
    "X                       X",
    "X        XXX            X",
    "XXXXXX                  X",
    "XXXXXX      P           X",
    "XXXXXXXXXXXXXXXXXXXXXXXXX"]

tile_size = 40
screen_width = tile_size * len(map_list[1])
screen_height = len(map_list) * tile_size
