import pygame
from Animation import *

class Scenery(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.pos = pos
        self.animation = Animation()
        with open(r'../assets/beer/beer1.png') as beer:
            self.image = pygame.image.load(beer)
            self.rect = self.image.get_rect(topleft=self.pos)

    def display(self, name, path, nb_frames, velocity):
        self.image = pygame.image.load(self.animation.launch_gif(name, path, nb_frames, velocity))

    def update(self, direction, shift):
        if direction == "y":
            self.rect.y += shift
        elif direction == "x":
            self.rect.x += shift
