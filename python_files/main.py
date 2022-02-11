import sys
from settings import *
from map import *


# Pygame init
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
world = Map(map_list, screen)
# test_tile = pygame.sprite.Group(Tile((40, 40), 40))

while True:
    pygame.display.update()
    screen.fill("black")
    clock.tick(60)
    world.run()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



