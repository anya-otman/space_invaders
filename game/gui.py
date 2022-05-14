import pygame


class Gui:
    def __init__(self, screen, screen_width: int):
        self.screen = screen
        self.screen_width = screen_width
        self.font = pygame.font.SysFont('arial', 36)
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

    def loss_message(self):
        """shows the message about losing in the end of game"""
        loss_surf = self.font.render('You lose', False, (255, 255, 255))
        loss_rect = loss_surf.get_rect(center=(300, 300))
        self.screen.blit(loss_surf, loss_rect)

    def victory_message(self):
        """shows the message about victory in the end of game"""
        victory_surf = self.font.render('You win', False, (255, 255, 255))
        victory_rect = victory_surf.get_rect(center=(300, 300))
        self.screen.blit(victory_surf, victory_rect)

    def draw_state(self, game_controller):
        """
        draws the current state of all game objects
        :param game_controller: instance of GameController class
        """
        if game_controller.running:
            game_controller.player_sprite.sprite.lasers.draw(self.screen)
            game_controller.player_sprite.draw(self.screen)
            self.display_lives(game_controller.player.number_of_lives)
            game_controller.alien_controller.aliens.draw(self.screen)
            game_controller.alien_controller.aliens_lasers.draw(self.screen)
            game_controller.obstacles.blocks.draw(self.screen)
        elif game_controller.player.number_of_lives == 0:
            self.loss_message()
        else:
            self.victory_message()
