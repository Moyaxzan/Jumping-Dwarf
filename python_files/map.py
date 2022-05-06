import pygame
from tiles import Tile
from settings import *
from Player import Player


class Map:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.world_shift = 0
        self.setup_level(level_data)

    def setup_level(self, layout):
        self.tiles_group = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
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
                    player_sprite = Player((x, y-tile_size))
                    self.player.add(player_sprite)
        self.tiles_group.update("y", -tile_size * len(map_list) + screen_height)
        self.player.update(-tile_size * len(map_list) + screen_height, 0, False, self)

    def horizontal_movement(self, world, player):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
        for sprite in self.tiles_group.sprites():
            if sprite.rect.colliderect(player):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.direction.x = -(player.direction.x) * 0.5
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.direction.x = -(player.direction.x) * 0.5

    def vertical_movement(self):
        player = self.player.sprite
        player.rect.y += player.direction.y
        for sprite in self.tiles_group.sprites():
            if sprite.rect.colliderect(player):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                if player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0.75

    def run(self, held, world, world_shift, player):
        world.tiles_group.update("y", world_shift)
        self.player.update(0, 0, held, world)
        self.horizontal_movement(world, player)
        self.vertical_movement()
        self.player.draw(self.display_surface)
        self.tiles_group.draw(self.display_surface)
