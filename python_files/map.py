import pygame
from tiles import Tile
from settings import *
from Player import Player


class Map:
    def __init__(self, level_data, surface):
        self.tiles_group = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()
        self.display_surface = surface
        self.world_shift = 1
        self.setup_level(level_data)

    def setup_level(self, layout):
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                if cell == "X":
                    x = col_index * tile_size
                    y = row_index * tile_size
                    tile = Tile((x, y), tile_size)
                    self.tiles_group.add(tile)
                if cell == "P":
                    x = col_index * tile_size
                    y = row_index * tile_size
                    player = Player((x, y-tile_size))
                    self.player_group.add(player)
        self.tiles_group.update("y", -tile_size * len(map_list) + screen_height)
        self.player_group.update("y", -tile_size * len(map_list) + screen_height)

    def run(self):
        self.player_group.draw(self.display_surface)
        self.tiles_group.draw(self.display_surface)
