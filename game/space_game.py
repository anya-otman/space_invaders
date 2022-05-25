import pygame
import sys
from game_controller import GameController
from gui import Gui


def start():
    """updates game's state and draws it on the screen every 60 milliseconds"""
    pygame.init()
    screen_width = 600
    screen_height = 600
    levels = [1, 2, 3]
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    game_controller = GameController(screen_width, screen_height, level=1, player_lives=3)
    gui = Gui(screen, screen_width)

    ALIENLASER = pygame.USEREVENT + 1
    pygame.time.set_timer(ALIENLASER, 800)

    AlIENBONUS = pygame.USEREVENT + 2
    pygame.time.set_timer(AlIENBONUS, 800)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == ALIENLASER:
                game_controller.alien_group.shoot()
            if event.type == AlIENBONUS:
                game_controller.alien_group.give_bonus()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n and not game_controller.running:
                    game_controller = make_new_game(screen_width, screen_height, game_controller, levels)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game_controller = restart_level(screen_width, screen_height, game_controller)
        screen.fill((30, 30, 30))
        game_controller.run()
        gui.draw_state(game_controller)
        pygame.display.flip()
        clock.tick(60)


def make_new_game(screen_width: int, screen_height: int, game_controller: GameController, levels: list):
    """
    creates and initializes an instance of the GameController class with new params
    :param screen_width: width of the game screen
    :param screen_height: height of the game screen
    :param game_controller: previous instance of GameController class
    :param levels: list that contains the game's level numbers
    :return: GameController
    """
    level = game_controller.level
    lives = game_controller.player.number_of_lives
    if lives != 0:
        if level != len(levels):
            level = levels[level]
        else:
            level = levels[0]
            lives = 3
    else:
        level = levels[0]
        lives = 3
    return GameController(screen_width, screen_height, level, lives)


def restart_level(screen_width: int, screen_height: int, game_controller: GameController):
    """
    creates and initializes an instance of the GameController class with params of current level
    :param screen_width: width of the game screen
    :param screen_height: height of the game screen
    :param game_controller: previous instance of GameController class
    :return: GameController
    """
    game_controller.music.stop()
    level = game_controller.level
    lives = game_controller.lives_at_beginning
    return GameController(screen_width, screen_height, level=level, player_lives=lives)


if __name__ == '__main__':
    start()
