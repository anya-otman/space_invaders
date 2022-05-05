import pygame


class Gui:
    def __init__(self, screen, screen_width):
        self.screen = screen
        self.screen_width = screen_width
        self.font = pygame.font.SysFont('arial', 36)
        self.live_surf = pygame.image.load('images/life.png').convert_alpha()

    def display_lives(self, number_of_lives):
        lives_x_start_pos = self.screen_width - (self.live_surf.get_size()[0] * number_of_lives + 8 * number_of_lives)
        for live in range(number_of_lives):
            x = lives_x_start_pos + (live * (self.live_surf.get_size()[0] + 10))
            self.screen.blit(self.live_surf, (x, 8))

    def loss_message(self):
        loss_surf = self.font.render('You lose', False, (255, 255, 255))
        loss_rect = loss_surf.get_rect(center=(300, 300))
        self.screen.blit(loss_surf, loss_rect)

    def victory_message(self):
        victory_surf = self.font.render('You win', False, (255, 255, 255))
        victory_rect = victory_surf.get_rect(center=(300, 300))
        self.screen.blit(victory_surf, victory_rect)

    def draw_state(self, player, obstacles, alien_controller):
        player_sprite = pygame.sprite.GroupSingle(player)
        player_sprite.sprite.lasers.draw(self.screen)
        player_sprite.draw(self.screen)
        self.display_lives(player.number_of_lives)
        alien_controller.aliens.draw(self.screen)
        alien_controller.aliens_lasers.draw(self.screen)

        obstacles.blocks.draw(self.screen)
