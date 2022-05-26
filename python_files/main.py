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
    go_to_menu = True
    in_settings = False


    while True:
        # Forces the player to go through the menu when he starts the program.
        if go_to_menu:
            Homepage(screen)
            go_to_menu = False
            fade_transi(screen, "in", 3)
        worldshift = 0
        pygame.display.update()
        cog_button = pygame.draw.rect(screen,"purple", ((screen_width-120,10),(50,50)))
        screen.fill("cyan")
        cog = pygame.transform.scale(pygame.image.load("../assets/settings/settings_icone.png"), (50,50))
        screen.blit(cog, (screen_width-120,10))
        clock.tick(60)
        events = pygame.event.get()
        player = world.player.sprite

        # Allows the camera to move along the player.
        if player.get_y() < 0:
            worldshift = screen_height
            player.set_y(player.get_y() + screen_height)
        elif player.get_y() > screen_height:
            worldshift = -screen_height
            player.set_y(player.get_y() - screen_height)

        # Prevents mouse movements to be counted as events.
        pygame.event.set_blocked(pygame.MOUSEMOTION)
        for event in events:

            # Quits the game.
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Checks if the player is on ground when he tries to jump, and if so load the right animation.
            if hold and (player.on_ground(world)):
                hold_value += 1
                held = True
                player.image = pygame.image.load(player.anime.launch_gif("stacking_dwarf", "dwarf", 1, 0))

            if event.type == pygame.KEYDOWN:
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
                    player.jump(hold_value, in_settings)
                hold_value = 0
                pressed = False
                hold = False
            # If the player presses escape or clicks the cog, he opens the settings screen.
            if player.on_ground(world) and ((event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or (event.type == pygame.MOUSEBUTTONDOWN and cog_button.collidepoint(pygame.mouse.get_pos()))):
                in_settings = True
                hold, held, hold_value = False, False, 0

        # Launches the ending screen when the top is reached.
        if player.rect.colliderect(world.beer):
            fade_transi(screen, "out", 3)
            ending(screen)
        # Makes the world run, called at each frame.
        world.run(held, worldshift, in_settings)

        if in_settings:
            player.direction.x = 0
            player.direction.y = 0
            in_settings, go_to_menu = settings(screen, in_settings, go_to_menu)