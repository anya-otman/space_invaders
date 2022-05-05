import pygame.sprite
import pygame
from math import pi
from game.alien import Alien
from laser import Laser
from random import choice


class AlienController:
    def __init__(self, x, y, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.aliens = pygame.sprite.Group()
        self.aliens_lasers = pygame.sprite.Group()
        self.create(x, y)
        self.direction = 1

    def create(self, rows, cols, x_distance=60, y_distance=48, x_offset=70, y_offset=100):
        for row_index in range(rows):
            for col_index in range(cols):
                x = col_index * x_distance + x_offset
                y = row_index * y_distance + y_offset
                alien = Alien(x, y)
                self.aliens.add(alien)

    def check_position(self):
        for alien in self.aliens.sprites():
            if alien.rect.right >= self.screen_width:
                self.direction = -1
            elif alien.rect.left <= 0:
                self.direction = 1

    def shoot(self):
        if self.aliens.sprites():
            random_alien = choice(self.aliens.sprites())
            laser_sprite = Laser(random_alien.rect.center, 5, pi/2, self.screen_width)
            self.aliens_lasers.add(laser_sprite)

    def update(self):
        self.aliens_lasers.update()
        self.check_position()
        for alien in self.aliens:
            alien.update(self.direction)