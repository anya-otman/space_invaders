import pygame


class ExtraAlien(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, screen_width: int):
        super().__init__()
        self.image = pygame.image.load('../images/extra.png')
        self.rect = pygame.Surface((40, 32)).get_rect(center=(x, y))
        self.speed = 2
        self.screen_width = screen_width

    def destroy(self):
        """deletes extra_alien if it's out of the screen"""
        if self.rect.x >= self.screen_width + 50:
            self.kill()

    def update(self):
        """changes the x coordinate of the alien every time it's called"""
        self.rect.x += self.speed
        self.destroy()
