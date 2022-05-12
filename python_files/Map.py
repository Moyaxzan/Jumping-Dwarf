from Tiles import Tile
from settings import *
from Scenery import *
from Player import Player


class Map:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.world_shift = 0
        self.setup_level(level_data)

    def setup_level(self, layout):
        self.tiles_group = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.beer_group = pygame.sprite.GroupSingle()
        self.flower_group = pygame.sprite.Group()
        self.sword_group = pygame.sprite.Group()
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
                if cell == "B":
                    x = col_index * 60
                    y = row_index * 60
                    self.beer = Scenery((x, y))
                    self.beer_group.add(self.beer)
                if cell == "F":
                    x = col_index * 60
                    y = row_index * 60
                    self.flower = Scenery((x, y))
                    self.flower_group.add(self.flower)
                if cell == "S":
                    x = col_index * 60
                    y = row_index * 60
                    self.sword = Scenery((x, y))
                    self.sword_group.add(self.sword)
        self.tiles_group.update("y", -60 * len(map_list) + screen_height)
        self.beer_group.update("y", -60 * len(map_list) + screen_height)
        self.sword_group.update("y", -60 * len(map_list) + screen_height)
        self.flower_group.update("y", -60 * len(map_list) + screen_height)
        self.player.update(-60 * len(map_list) + screen_height, 0, False, self)

    def movement_collide(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
        for sprite in self.tiles_group.sprites():
            if sprite.rect.colliderect(player):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.direction.x = -(player.direction.x) * 0.5
                    if not player.on_ground(self):
                        self.player.sprite.image = pygame.image.load(self.player.sprite.anime.launch_gif("running_right", "dwarf", 2, .1))
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    # Presque stylée sah
                    # player.rect = player.image.get_rect(topleft=player.rect.topleft)
                    player.direction.x = -(player.direction.x) * 0.5
                    if not player.on_ground(self):
                        self.player.sprite.image = pygame.image.load(self.player.sprite.anime.launch_gif("running_left", "dwarf", 2, .1))

        player.rect.y += player.direction.y
        for sprite in self.tiles_group.sprites():
            if sprite.rect.colliderect(player):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                if player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0.75


    def run(self, held, world_shift):
        self.tiles_group.update("y", world_shift)
        self.player.update(0, 0, held, self)
        self.beer_group.update("y", world_shift)
        self.flower_group.update("y", world_shift)
        self.sword_group.update("y", world_shift)
        self.beer.display("beer", "beer", 20, 0.8)
        self.sword.display("sword", "sword", 3, 0.08)
        for i in self.flower_group.sprites():
            i.display("flower", "flower", 2, 0.02)
        self.movement_collide()
        self.beer_group.draw(self.display_surface)
        self.flower_group.draw(self.display_surface)
        self.sword_group.draw(self.display_surface)
        self.tiles_group.draw(self.display_surface)
        self.player.draw(self.display_surface)
