import pygame
import math
from math import pi


class Laser(pygame.sprite.Sprite):
    def __init__(self, position: tuple[int, int], speed: int, angle: float, screen_width: int):
        super().__init__()
        self.color = (255, 255, 255)
        self.image = pygame.Surface((7, 10))
        self.image.fill(self.color)
        self.speed = speed
        self.angle = angle
        self.rect = self.image.get_rect(center=position)
        self.width_x_constraint = screen_width

    def destroy(self):
        """deletes laser if it's out of the screen"""
        if self.rect.y <= 0:
            self.kill()

    def change_direction(self):
        """changes the direction of the laser movement if it collides with the edge of the screen"""
        if self.rect.x >= self.width_x_constraint:
            self.rect.x = self.width_x_constraint
            self.angle -= pi/2
        if self.rect.x <= 0:
            self.rect.x = 0
            self.angle += pi / 2

    def update(self):
        """updates the state of the laser"""
        self.rect.y += self.speed * math.sin(self.angle)
        self.rect.x += self.speed * math.cos(self.angle)
        self.change_direction()
        self.destroy()
