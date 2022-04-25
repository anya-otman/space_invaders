import pygame


class Gui:
    def __init__(self, screen):
        self.screen = screen

    def draw_state(self, player, obstacles):
        player_sprite = pygame.sprite.GroupSingle(player)
        player_sprite.sprite.lasers.draw(self.screen)
        player_sprite.draw(self.screen)

        obstacles.blocks.draw(self.screen)
