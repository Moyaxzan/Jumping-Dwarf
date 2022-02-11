import pygame
from tiles import Tile
from settings import tile_size
from Player import Player


class Map:
    def __init__(self, level_data, surface):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = -1

    def setup_level(self, layout):
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                if cell == "X":
                    x = col_index * tile_size
                    y = row_index * tile_size
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)
                if cell == "P":
                    x = col_index * tile_size
                    y = row_index * tile_size
                    player = Player((x, y))
                    self.tiles.add(player)

    def run(self):
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
