import pygame.math

from tiles import *
from math import cos, tan


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        scale_x = 1280.0 / 1600
        scale_y = 720.0 / 900

        with open(r'../assets/dwarf/static dwarf.gif') as nain:
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

    def get_input(self, held, world):
        keys = pygame.key.get_pressed()
        ground = self.on_ground(world)
        if not held and (keys[pygame.K_LEFT] or keys[pygame.K_q]) and ground:
            self.direction.x = -1
        elif not held and (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and ground:
            self.direction.x = 1
        else:
            self.direction.x = 0

    def jump1(self, hold_value, direction):
        self.direction.y = -6 - hold_value / 10

    def apply_gravity(self):
        self.direction.y += self.gravity

    def update(self, shift_y, shift_x, held, world):
        self.get_input(held, world)
        if shift_y != 0 or shift_x != 0:
            self.rect.y += shift_y
            self.rect.x += shift_x
        self.apply_gravity()

    def on_ground(self, world):
        for tile in world.tiles_group:
            if tile.rect.collidepoint(self.rect.centerx, self.rect.bottom):
                return True
        return False

    def jump(self, hold, x, height):
        angle = hold * 120
        g = 9.81
        y = -(g / 2 * vect * cos(angle)**2) * x**2 + tan(angle) * x + height
