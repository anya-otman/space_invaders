import pygame
from game.bonus_type import BonusType


class Bonus(pygame.sprite.Sprite):
    def __init__(self, position, speed: int, type: int):
        super().__init__()
        if type == BonusType.protection.value:
            self.image = pygame.image.load("../images/bonus_pr.png")
        elif type == BonusType.firing_acceleration.value:
            self.image = pygame.image.load("../images/bonus_f.png")
        self.rect = pygame.Surface((20, 20)).get_rect(center=position)
        self.speed = speed

    def destroy(self):
        """deletes laser if it's out of the screen"""
        if self.rect.y >= 600:
            self.kill()

    def update(self):
        """updates the state of the laser"""
        self.rect.y += self.speed
        self.destroy()
