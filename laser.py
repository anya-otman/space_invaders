import pygame


class Laser(pygame.sprite.Sprite):
    def __init__(self, position, speed, screen_height):
        super().__init__()
        self.color = (255, 255, 255)
        self.image = pygame.Surface((4, 20))
        self.image.fill(self.color)
        self.speed = speed
        self.rect = self.image.get_rect(center=position)
        self.height_y_constraint = screen_height

    def destroy(self):
        if self.rect.y <= 0:
            self.kill()

    def update(self):
        self.rect.y += self.speed
        self.destroy()
