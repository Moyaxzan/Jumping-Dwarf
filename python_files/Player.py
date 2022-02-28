from tiles import *
from math import cos, tan


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((40,40*2))
        self.image.fill("red")
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, direction, shift):
        if direction == "y":
            self.rect.y += shift
        if direction == "x":
            self.rect.x += shift

    def jump(self, hold, x, height):
        angle = hold * 120
        g = 9.81
        y = -(g / 2 * vect * cos(angle)**2) * x**2 + tan(angle) * x + height
