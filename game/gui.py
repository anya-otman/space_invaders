import pygame

WHITE = (255, 255, 255)


class Gui:
    def __init__(self, screen, screen_width: int):
        self.screen = screen
        self.screen_width = screen_width
        # self.font = pygame.font.SysFont('arial', 36)
        self.font = pygame.font.Font('../font/Pixeled.ttf', 20)
        self.live_surf = pygame.image.load('../images/life.png').convert_alpha()

    def display_lives(self, number_of_lives: int):
        """
        draws the player's lives on the screen
        :param number_of_lives: current number of player lives
        """
        lives_x_start_pos = self.screen_width - (self.live_surf.get_size()[0] * number_of_lives + 8 * number_of_lives)
        for live in range(number_of_lives):
            x = lives_x_start_pos + (live * (self.live_surf.get_size()[0] + 10))
            self.screen.blit(self.live_surf, (x, 8))

    def print_message(self, message: str, pos):
        """prints a message on the screen
        :param message: message text
        :param pos: position of the text on the screen
        """
        surf = self.font.render(message, False, WHITE)
        rect = surf.get_rect(center=pos)
        self.screen.blit(surf, rect)

    def loss_message(self):
        """shows the message about losing in the end of game"""
        self.print_message('You lose', (300, 250))
        self.print_message('press N to start new game', (300, 300))

    def victory_message(self):
        """shows the message about victory in the end of game"""
        self.print_message('You win', (300, 250))
        self.print_message('press N to start new game', (300, 300))

    def next_level_message(self):
        """shows the message about start a new level"""
        self.print_message('Level completed', (300, 250))
        self.print_message('press N to start next level', (300, 300))

    def level_message(self, level_number):
        """shows the message about number of current level"""
        self.print_message(f'Level {level_number}', (300, 250))  # change level number

    def draw_state(self, game_controller):
        """
        draws the current state of all game objects
        :param game_controller: instance of GameController class
        """
        if game_controller.running:
            if game_controller.form_timer != 0:
                self.level_message(game_controller.level)
            else:
                game_controller.player_sprite.sprite.lasers.draw(self.screen)
                game_controller.player_sprite.draw(self.screen)
                self.display_lives(game_controller.player.number_of_lives)
                game_controller.alien_group.aliens.draw(self.screen)
                game_controller.alien_group.aliens_lasers.draw(self.screen)
                game_controller.alien_group.extra_aliens.draw(self.screen)
                game_controller.obstacles.blocks.draw(self.screen)
        elif game_controller.player.number_of_lives == 0 or game_controller.alien_group.aliens:
            self.loss_message()
        elif game_controller.level == 3:
            self.victory_message()
        else:
            self.next_level_message()
