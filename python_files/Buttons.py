import pygame


# Allows to create buttons for menu.
class Button:
    def __init__(self, screen, position, dimension, color):
        self.screen = screen
        self.color = color
        self.position = position
        self.dimension = dimension

    def draw(self):
        return pygame.draw.rect(self.screen, self.color, (self.position, self.dimension), 0)
