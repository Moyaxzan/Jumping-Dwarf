import pygame.math
from Animation import *
from Tiles import *
from random import randint

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        with open(r'../assets/dwarf/static_dwarf1.png') as nain:
            self.image = pygame.image.load(nain)
            self.rect = self.image.get_rect(topleft=pos)
        # Player variables.
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 8
        self.gravity = 0.5
        self.hold = 0
        self.jump_speed = -10
        # Allows the player to have several animations.
        self.anime = Animation()

    # Receives player's inputs for movements.
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

    # Makes the play jump, the longer he holds space the higher because of "hold_value" variable.
    def jump(self, hold_value, in_settings):
        if not in_settings:
            rand = randint(1, 5)
            sound_jump = pygame.mixer.Sound("../audio/saut" + str(rand) + ".wav")
            pygame.mixer.Sound.play(sound_jump)
            self.direction.y = -6 - hold_value

    # Apply gravity, called in each frame by update().
    def apply_gravity(self):
        if self.direction.y < 25:
            self.direction.y += self.gravity

    # Apply every changes needed to the player, called in each frame by the map.
    def update(self, shift_y, shift_x, held, world, in_settings):
        if not in_settings:
            self.get_input(held, world)
            if shift_y != 0 or shift_x != 0:
                self.rect.y += shift_y
                self.rect.x += shift_x
            self.apply_gravity()

    # Returns True if the player is on ground.
    def on_ground(self, world):
        for tile in world.tiles_group:
            if tile.rect.collidepoint(self.rect.centerx - 33, self.rect.bottom) or tile.rect.collidepoint(self.rect.centerx + 33, self.rect.bottom):
                return True
        return False

    # Returns player y position.
    def get_y(self):
        return self.rect.centery

    # Returns player x position.
    def get_x(self):
        return self.rect.centerx

    # Sets position y position.
    def set_y(self, y):
        self.rect.centery = y
