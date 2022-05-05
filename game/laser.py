import pygame
import math
from math import pi


class Laser(pygame.sprite.Sprite):
    def __init__(self, position, speed, angle, screen_width):
        super().__init__()
        self.color = (255, 255, 255)
        self.image = pygame.Surface((7, 10))
        self.image.fill(self.color)
        self.speed = speed
        self.angle = angle
        self.rect = self.image.get_rect(center=position)
        self.width_x_constraint = screen_width

    def destroy(self):
        if self.rect.y <= 0:
            self.kill()

    def change_direction(self):
        if self.rect.x >= self.width_x_constraint:
            self.rect.x = self.width_x_constraint
            self.angle -= pi/2
        if self.rect.x <= 0:
            self.rect.x = 0
            self.angle += pi / 2

    def update(self):
        self.rect.y += self.speed * math.sin(self.angle)
        self.rect.x += self.speed * math.cos(self.angle)
        self.change_direction()
        self.destroy()
