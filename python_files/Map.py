from Tiles import Tile
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
                if cell == "G":
                    x = col_index * 60
                    y = row_index * 60
                    tile = Tile((x, y), "grass")
                    self.tiles_group.add(tile)
                if cell == "D":
                    x = col_index * 60
                    y = row_index * 60
                    tile = Tile((x, y), "dirt")
                    self.tiles_group.add(tile)
                if cell == "W":
                    x = col_index * 60
                    y = row_index * 60
                    tile = Tile((x, y), "wall")
                    self.tiles_group.add(tile)
                if cell == "P":
                    x = col_index * 60
                    y = row_index * 60
                    player_sprite = Player((x, y - 60))
                    self.player.add(player_sprite)
        self.tiles_group.update("y", -60 * len(map_list) + screen_height)
        self.player.update(-60 * len(map_list) + screen_height, 0, False, self)

    def movement_collide(self):
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
        player.rect.y += player.direction.y
        for sprite in self.tiles_group.sprites():
            if sprite.rect.colliderect(player):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                if player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0.75


    def run(self, held, world, world_shift):
        world.tiles_group.update("y", world_shift)
        self.player.update(0, 0, held, world)
        self.movement_collide()
        self.player.draw(self.display_surface)
        self.tiles_group.draw(self.display_surface)
