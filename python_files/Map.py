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
        # Create several groups to put every different tiles in them.
        self.player = pygame.sprite.GroupSingle()
        self.beer_group = pygame.sprite.GroupSingle()
        self.tiles_group = pygame.sprite.Group()
        self.flower_group = pygame.sprite.Group()
        self.sword_group = pygame.sprite.Group()
        self.tourist_group = pygame.sprite.Group()
        self.nani_group = pygame.sprite.Group()
        self.wazo_group = pygame.sprite.Group()
        self.sun_group = pygame.sprite.Group()
        self.oiseaux1_group = pygame.sprite.Group()
        self.oiseaux2_group = pygame.sprite.Group()
        self.stone_group = pygame.sprite.Group()
        self.cloud1_group = pygame.sprite.Group()
        self.cloud2_group = pygame.sprite.Group()
        self.cloud3_group = pygame.sprite.Group()
        self.cloud4_group = pygame.sprite.Group()
        self.cloud5_group = pygame.sprite.Group()
        self.cloud6_group = pygame.sprite.Group()

        # Iterates through the list in settings.py, then add to the different groups the right tile depending
        # on what letters are found . (i.e. G for grass, D for dirt)
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * 60
                y = row_index * 60
                if cell == "G":
                    tile = Tile((x, y), "grass")
                    self.tiles_group.add(tile)
                if cell == "D":
                    tile = Tile((x, y), "dirt")
                    self.tiles_group.add(tile)
                if cell == "W":
                    tile = Tile((x, y), "wall")
                    self.tiles_group.add(tile)
                if cell == "P":
                    player_sprite = Player((x, y - 60))
                    self.player.add(player_sprite)
                if cell == "B":
                    self.beer = Scenery((x, y))
                    self.beer_group.add(self.beer)
                if cell == "F":
                    self.flower = Scenery((x, y))
                    self.flower_group.add(self.flower)
                if cell == "T":
                    self.tourist = Scenery((x, y))
                    self.tourist_group.add(self.tourist)
                if cell == "N":
                    self.nani = Scenery((x, y))
                    self.nani_group.add(self.nani)
                if cell == "w":
                    self.wazo = Scenery((x, y-53.5))
                    self.wazo_group.add(self.wazo)
                if cell == "S":
                    self.sword = Scenery((x, y))
                    self.sword_group.add(self.sword)
                if cell == "s":
                    self.sun = Scenery((x,y))
                    self.sun_group.add(self.sun)
                if cell == "O":
                    self.oiseau = Scenery((x,y))
                    self.oiseaux1_group.add(self.oiseau)
                if cell == "o":
                    self.oiseau = Scenery((x,y))
                    self.oiseaux2_group.add(self.oiseau)
                if cell == "R":
                    self.stone = Scenery((x,y))
                    self.stone_group.add(self.stone)
                if cell == "1":
                    self.cloud1 = Scenery((x,y))
                    self.cloud1_group.add(self.cloud1)
                if cell == "2":
                    self.cloud2 = Scenery((x,y))
                    self.cloud2_group.add(self.cloud2)
                if cell == "3":
                    self.cloud3 = Scenery((x,y))
                    self.cloud3_group.add(self.cloud3)
                if cell == "4":
                    self.cloud4 = Scenery((x, y))
                    self.cloud4_group.add(self.cloud4)
                if cell == "5":
                    self.cloud5 = Scenery((x,y))
                    self.cloud5_group.add(self.cloud5)
                if cell == "6":
                    self.cloud6 = Scenery((x,y))
                    self.cloud6_group.add(self.cloud6)

        # Draw every groups where they need to be.
        self.tiles_group.update("y", -60 * len(map_list) + screen_height)
        self.beer_group.update("y", -60 * len(map_list) + screen_height)
        self.sword_group.update("y", -60 * len(map_list) + screen_height)
        self.flower_group.update("y", -60 * len(map_list) + screen_height)
        self.wazo_group.update("y", -60 * len(map_list) + screen_height)
        self.oiseaux1_group.update("y", -60 * len(map_list) + screen_height)
        self.oiseaux2_group.update("y", -60 * len(map_list) + screen_height)
        self.stone_group.update("y", -60 * len(map_list) + screen_height)
        self.sun_group.update("y", -60 * len(map_list) + screen_height - 50)
        self.cloud1_group.update("y", -60 * len(map_list) + screen_height - 50)
        self.cloud2_group.update("y", -60 * len(map_list) + screen_height - 50)
        self.cloud3_group.update("y", -60 * len(map_list) + screen_height - 50)
        self.cloud4_group.update("y", -60 * len(map_list) + screen_height - 45)
        self.cloud5_group.update("y", -60 * len(map_list) + screen_height - 50)
        self.cloud6_group.update("y", -60 * len(map_list) + screen_height - 50)
        self.tourist_group.update("x", -20)
        self.tourist_group.update("y", -60 * len(map_list) + screen_height + 30)
        self.nani_group.update("y", -60 * len(map_list) + screen_height + 35)
        self.nani_group.update("x", -20)
        self.player.update(-60 * len(map_list) + screen_height, 0, False, self, False)

    # Handle collision with player.
    def movement_collide(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
        for sprite in self.tiles_group.sprites():
            if sprite.rect.colliderect(player):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.direction.x = -player.direction.x * 0.5
                    if not player.on_ground(self):

                        self.player.sprite.image = \
                            pygame.image.load(self.player.sprite.anime.launch_gif("running_right", "dwarf", 2, .1))

                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.direction.x = -player.direction.x * 0.5
                    if not player.on_ground(self):

                        self.player.sprite.image = \
                            pygame.image.load(self.player.sprite.anime.launch_gif("running_left", "dwarf", 2, .1))

        player.rect.y += player.direction.y
        for sprite in self.tiles_group.sprites():
            if sprite.rect.colliderect(player):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                if player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0.75

    # Updates every group then draw them on screen, called each frame by main.py.
    def run(self, held, world_shift, in_settings):

        self.tiles_group.update("y", world_shift)
        self.player.update(0, 0, held, self, in_settings)
        self.beer_group.update("y", world_shift)
        self.flower_group.update("y", world_shift)
        self.sword_group.update("y", world_shift)
        self.tourist_group.update("y", world_shift)
        self.nani_group.update("y", world_shift)
        self.wazo_group.update("y", world_shift)
        self.sun_group.update("y", world_shift)
        self.oiseaux1_group.update("y", world_shift)
        self.oiseaux2_group.update("y", world_shift)
        self.stone_group.update("y", world_shift)
        self.cloud1_group.update("y", world_shift)
        self.cloud2_group.update("y", world_shift)
        self.cloud3_group.update("y", world_shift)
        self.cloud4_group.update("y", world_shift)
        self.cloud5_group.update("y", world_shift)
        self.cloud6_group.update("y", world_shift)

        self.beer.display("beer", "beer", 20, 0.8)
        self.sword.display("sword", "sword", 3, 0.08)
        self.tourist.display("tourist", "tourist", 8, 0.06)
        self.nani.display("nani","nani", 3, 0.1)
        self.wazo.display("wazo","wazo", 4, 0.08)
        self.sun.display("sun","sun", 6, 0.04)
        self.stone.display("rock","divers", 1, 0)

        for each_oiseau1 in self.oiseaux1_group.sprites():
            each_oiseau1.display("oiseaux","oiseaux1", 2, 0.05)
        for each_oiseau2 in self.oiseaux2_group.sprites():
            each_oiseau2.display("oiseaux", "oiseaux2", 2, 0.05)
        for each_flower in self.flower_group.sprites():
            each_flower.display("flower", "flower", 2, 0.02)
        for each_cloud in self.cloud1_group.sprites():
            each_cloud.display("cloud1", "divers", 1, 0)
        for each_cloud in self.cloud2_group.sprites():
            each_cloud.display("cloud2", "divers", 1, 0)
        for each_cloud in self.cloud3_group.sprites():
            each_cloud.display("cloud3", "divers", 1, 0)
        for each_cloud in self.cloud4_group.sprites():
            each_cloud.display("cloud4", "divers", 1, 0)
        for each_cloud in self.cloud5_group.sprites():
            each_cloud.display("cloud5", "divers", 1, 0)
        for each_cloud in self.cloud6_group.sprites():
            each_cloud.display("cloud6", "divers", 1, 0)
        self.movement_collide()

        self.cloud1_group.draw(self.display_surface)
        self.cloud2_group.draw(self.display_surface)
        self.cloud3_group.draw(self.display_surface)
        self.cloud4_group.draw(self.display_surface)
        self.cloud5_group.draw(self.display_surface)
        self.cloud6_group.draw(self.display_surface)
        self.beer_group.draw(self.display_surface)
        self.flower_group.draw(self.display_surface)
        self.sword_group.draw(self.display_surface)
        self.tourist_group.draw(self.display_surface)
        self.nani_group.draw(self.display_surface)
        self.wazo_group.draw(self.display_surface)
        self.sun_group.draw(self.display_surface)
        self.oiseaux1_group.draw(self.display_surface)
        self.oiseaux2_group.draw(self.display_surface)
        self.stone_group.draw(self.display_surface)
        self.tiles_group.draw(self.display_surface)
        self.player.draw(self.display_surface)

