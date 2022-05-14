import pygame
import pygame.sprite
from math import pi
from game.alien import Alien
from game.extra_alien import ExtraAlien
from game.laser import Laser
from random import choice, randint


class AlienGroup:
    def __init__(self, rows: int, cols: int, screen_width: int, screen_height: int):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.aliens = pygame.sprite.Group()
        self.aliens_lasers = pygame.sprite.Group()
        self.create(rows, cols)
        self.direction = 1
        self.extra_aliens = pygame.sprite.Group()
        self.extra_alien_timer = randint(600, 1000)

    def create(self, rows: int, cols: int, x_distance=60, y_distance=48, x_offset=70, y_offset=100):
        """
        creates aliens
        :param rows: number of rows of aliens
        :param cols: number of columns of aliens
        :param x_distance: x distance between robots
        :param y_distance: y distance between robots
        :param x_offset: x offset of the alien group on the screen
        :param y_offset: y offset of the alien group on the screen
        """
        for row_index in range(rows):
            for col_index in range(cols):
                x = col_index * x_distance + x_offset
                y = row_index * y_distance + y_offset
                alien = Alien(x, y)
                self.aliens.add(alien)

    def check_position(self):
        """checks the position of the alien and doesn't allow it to go beyond the screen"""
        for alien in self.aliens.sprites():
            if alien.rect.right >= self.screen_width:
                self.direction = -1
            elif alien.rect.left <= 0:
                self.direction = 1

    def shoot(self):
        """selects a random shooting enemy"""
        if self.aliens.sprites():
            random_alien = choice(self.aliens.sprites())
            rnd_int = randint(0, 8)
            if rnd_int == 5:
                laser_sprite = Laser(random_alien.rect.center, 5, pi / 2, self.screen_width, True)
                self.aliens_lasers.add(laser_sprite)
            else:
                laser_sprite = Laser(random_alien.rect.center, 5, pi / 2, self.screen_width)
                self.aliens_lasers.add(laser_sprite)

    def check_extra_alien_timer(self):
        """updates extra alien timer and create extra alien"""
        self.extra_alien_timer -= 1
        if self.extra_alien_timer <= 0:
            self.extra_aliens.add(ExtraAlien(-10, 40, self.screen_width))
            self.extra_alien_timer = randint(600, 1000)

    def update(self):
        """updates the state of aliens"""
        self.aliens_lasers.update()
        self.check_position()
        self.check_extra_alien_timer()
        for alien in self.aliens:
            alien.update(self.direction)
        for extra_alien in self.extra_aliens:
            extra_alien.update()
