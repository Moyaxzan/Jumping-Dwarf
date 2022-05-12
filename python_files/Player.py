import pygame.math
from math import cos, tan
from Animation import *
from Tiles import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        with open(r'../assets/dwarf/static_dwarf1.png') as nain:
            self.image = pygame.image.load(nain)
            self.rect = self.image.get_rect(topleft=pos)

        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 8
        self.gravity = 0.5
        self.hold = 0
        self.jump_speed = -10
        self.anime = Animation()

    def get_input(self, held, world):
        keys = pygame.key.get_pressed()
        ground = self.on_ground(world)
        if not held and (keys[pygame.K_LEFT] or keys[pygame.K_q]) and ground:
            self.direction.x = -1
            self.image = pygame.image.load(self.anime.launch_gif("running_left", "dwarf", 2, .1))
        elif not held and (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and ground:
            self.direction.x = 1
            self.image = pygame.image.load(self.anime.launch_gif("running_right", "dwarf", 2, .1))

        elif ground:
            self.direction.x = 0
            if not held:
                self.image = pygame.image.load(self.anime.launch_gif("static_dwarf", "dwarf", 2, .03))
        elif not ground and self.direction.y > 18:
            self.image = pygame.image.load(self.anime.launch_gif("falling_dwarf", "dwarf", 2, .1))


    def jump1(self, hold_value):
        self.direction.y = -6 - hold_value

    def apply_gravity(self):
        if self.direction.y < 25:
            self.direction.y += self.gravity

    def update(self, shift_y, shift_x, held, world):
        self.get_input(held, world)
        if shift_y != 0 or shift_x != 0:
            self.rect.y += shift_y
            self.rect.x += shift_x
        self.apply_gravity()

    def on_ground(self, world):
        for tile in world.tiles_group:
            if tile.rect.collidepoint(self.rect.centerx - 33, self.rect.bottom) or tile.rect.collidepoint(self.rect.centerx + 33, self.rect.bottom):
                return True
        return False

    def jump(self, hold, x, height):
        angle = hold * 120
        g = 9.81
        y = -(g / 2 * vect * cos(angle)**2) * x**2 + tan(angle) * x + height

    def get_y(self):
        return self.rect.centery

    def get_x(self):
        return self.rect.centerx

    def set_y(self, y):
        self.rect.centery = y
