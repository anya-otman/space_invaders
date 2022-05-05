import pygame
import sys
from game_controller import GameController
from gui import Gui

if __name__ == '__main__':
    pygame.init()
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    game_controller = GameController(screen_width, screen_height)
    gui = Gui(screen, screen_width)

    ALIENLASER = pygame.USEREVENT + 1
    pygame.time.set_timer(ALIENLASER, 800)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == ALIENLASER:
                game_controller.alien_controller.alien_shoot()

        screen.fill((30, 30, 30))
        game_controller.run()
        gui.draw_state(game_controller.player, game_controller.obstacles, game_controller.alien_controller)
        pygame.display.flip()
        clock.tick(60)

        if not game_controller.running:
            pygame.quit()
            sys.exit()
