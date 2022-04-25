import pygame


class Alien(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('images/alien.png')
        self.rect = pygame.Surface((60, 30)).get_rect(midbottom=(x, y))
        self.speed = 1

    def update(self, direction):
        self.rect.x += direction * self.speed
