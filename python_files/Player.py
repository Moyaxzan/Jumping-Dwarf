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
        self.speed = 8
        self.gravity = 0.5
        self.jump_speed = -10

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_q]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE]:
            self.jump1()

    def jump1(self):
        self.direction.y = self.jump_speed

    def apply_gravity(self):
        self.direction.y += self.gravity



    def update(self, shift_y, shift_x):
        self.get_input()
        if shift_y == 0 and shift_x == 0:
            pass
        else:
            self.rect.y += shift_y
            self.rect.x += shift_x
        self.apply_gravity()

    def jump(self, hold, x, height):
        angle = hold * 120
        g = 9.81
        y = -(g / 2 * vect * cos(angle)**2) * x**2 + tan(angle) * x + height
