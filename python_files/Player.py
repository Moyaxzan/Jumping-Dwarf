import pygame.math

from tiles import *
from math import cos, tan


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((40,40*2))
        self.image.fill("red")
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(0,0)
        self.gravity = 0.01

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.direction.x = -5
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 5
        else:
            self.direction.x = 0

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def update(self, shift_y, shift_x):
        if shift_y == 0 and shift_x == 0:
            self.get_input()
            self.rect.y += self.direction.y
            self.rect.x += self.direction.x
        else:
            self.rect.y += shift_y
            self.rect.x += shift_x
        self.apply_gravity()

    def jump(self, hold, x, height):
        angle = hold * 120
        g = 9.81
        y = -(g / 2 * vect * cos(angle)**2) * x**2 + tan(angle) * x + height
