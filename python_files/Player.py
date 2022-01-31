import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        """self.image = pygame.Surface.scroll(dx=0, dy=0)"""
        self.image.fill("red")
        self.rect = self.image.get_rect(topleft=pos)
