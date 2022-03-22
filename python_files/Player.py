import pygame.math

from tiles import *
from math import cos, tan


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        scale_x = 1280.0 / 1600
        scale_y = 720.0 / 900

        with open(r'C:\Users\Kiran\Downloads\Nain_face-Recovered_650mss.png') as nain:
            self.sprite = []

            surface = self.sprite.append(pygame.image.load(nain))




            self.current_sprite = 0
            self.image = self.sprite[self.current_sprite]
            self.rect = self.image.get_rect(topleft=pos)


            self.direction = pygame.math.Vector2(0, 0)
            self.speed = 8
            self.gravity = 0.5
            self.hold = 0
            self.jump_speed = -10

    def get_input(self, held):
        keys = pygame.key.get_pressed()
        if not held and (keys[pygame.K_LEFT] or keys[pygame.K_q]):
            self.direction.x = -1
        elif not held and (keys[pygame.K_RIGHT] or keys[pygame.K_d]):
            self.direction.x = 1
        else:
            self.direction.x = 0

    def jump1(self, hold_value, direction):
        print(direction)
        self.direction.y = -6 - hold_value / 10

    def apply_gravity(self):
        self.direction.y += self.gravity

    def update(self, shift_y, shift_x, held):
        self.get_input(held)
        if shift_y != 0 or shift_x != 0:
            self.rect.y += shift_y
            self.rect.x += shift_x
        self.apply_gravity()

    def jump(self, hold, x, height):
        angle = hold * 120
        g = 9.81
        y = -(g / 2 * vect * cos(angle)**2) * x**2 + tan(angle) * x + height