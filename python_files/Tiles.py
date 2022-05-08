import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, type):
        super().__init__()
        if type == "grass":
            with open(r'../assets/tiles/cube_herbe.png') as grass:
                self.image = pygame.image.load(grass)
                self.rect = self.image.get_rect(topleft=pos)
        if type == "dirt":
            with open(r'../assets/tiles/cube_dirt.png') as dirt:
                self.image = pygame.image.load(dirt)
                self.rect = self.image.get_rect(topleft=pos)
        if type == "wall":
            with open(r'../assets/tiles/cube_wall.png') as wall:
                self.image = pygame.image.load(wall)
                self.rect = self.image.get_rect(topleft=pos)


    def update(self, direction, shift):
        if direction == "y":
            self.rect.y += shift
        elif direction == "x":
            self.rect.x += shift
