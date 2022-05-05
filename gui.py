import sys

import pygame


class Gui:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont('arial', 36)

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

        alien_controller.aliens.draw(self.screen)
        alien_controller.aliens_lasers.draw(self.screen)

        obstacles.blocks.draw(self.screen)
