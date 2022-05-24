import sys
from Map import *


if __name__ == '__main__':
    # Pygame init
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    icon = pygame.image.load(r'../assets/divers/icon.png')
    pygame.display.set_icon(icon)
    pygame.display.set_caption("Jumping Dwarf")
    clock = pygame.time.Clock()

    # Map initiation
    world = Map(map_list, screen)
    hold = False
    hold_value = 0
    pressed = False
    held = False
    play_the_game = False


    while True:
        # Force the player to go into menu when he starts the program.
        if not play_the_game:
            Menu(screen)
            play_the_game = True
        worldshift = 0
        pygame.display.update()
        screen.fill("cyan")
        clock.tick(60)
        events = pygame.event.get()
        player = world.player.sprite

        # Allow the camera to move along the player.
        if player.get_y() < 0:
            worldshift = screen_height
            player.set_y(player.get_y() + screen_height)
        elif player.get_y() > screen_height:
            worldshift = -screen_height
            player.set_y(player.get_y() - screen_height)

        # Prevents mouse movements to be counted as events.
        pygame.event.set_blocked(pygame.MOUSEMOTION)
        for event in events:

            # Quit the game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Check if the player is on ground when he tries to jump, and if so load the right animation.
            if hold and (player.on_ground(world)):
                hold_value += 1
                held = True
                player.image = pygame.image.load(player.anime.launch_gif("stacking_dwarf", "dwarf", 1, 0))

            if event.type == pygame.KEYDOWN:
                #
                if event.key == pygame.K_SPACE:
                    hold = True
                    pressed = True

            # Checks if the player is still holding space OR if he pressed it for too long,
            # which will make him jump afterwards.
            elif event.type == pygame.KEYUP or hold_value > 11:
                if hold_value > 11:
                    hold = False
                    held = False
                elif event.key == pygame.K_SPACE:
                    hold = False
                    held = False

            # Makes the player jump.
            if not hold and pressed and (player.direction.y == player.gravity or player.direction.y == 0):
                # Checks if the player is on ground.
                if player.on_ground(world):
                    player.jump1(hold_value)
                hold_value = 0
                pressed = False
                hold = False
            # If the player press escape, he returns into menu.
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                play_the_game = False

        # Makes the world run, called at each frame.
        world.run(held, worldshift)

        if player.rect.colliderect(world.beer):
            ending(screen)