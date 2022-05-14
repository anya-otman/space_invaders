import pygame


class Alien(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        super().__init__()
        self.image = pygame.image.load('../images/alien.png')
        self.rect = pygame.Surface((60, 30)).get_rect(midbottom=(x, y))
        self.speed = 1

    def update(self, direction: int):
        """
        changes the x coordinate of the alien every time it's called
        :param direction: direction of alien's offset
        """
        self.rect.x += direction * self.speed
