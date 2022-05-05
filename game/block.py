import pygame


class Block(pygame.sprite.Sprite):
    def __init__(self, block_size: int, x: int, y: int):
        super().__init__()
        self.image = pygame.Surface((block_size, block_size))
        self.image.fill((19, 94, 242))
        self.rect = self.image.get_rect(topleft=(x, y))
