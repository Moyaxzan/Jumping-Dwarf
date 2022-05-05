import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill('yellow')
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, direction, shift):
        if direction == "y":
            self.rect.y += shift
        elif direction == "x":
            self.rect.x += shift
