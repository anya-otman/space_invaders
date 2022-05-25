import pygame
import pygame.sprite
from math import pi
from game.alien import Alien
from game.extra_alien import ExtraAlien
from game.laser import Laser
from game.bonus import Bonus
from game.bonus_type import BonusType
from random import choice


class AlienGroup:
    def __init__(self, rows: int, cols: int, screen_width: int, screen_height: int):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.aliens = pygame.sprite.Group()
        self.aliens_lasers = pygame.sprite.Group()
        self.aliens_f_bonuses = pygame.sprite.Group()
        self.aliens_pr_bonuses = pygame.sprite.Group()
        self.create(rows, cols)
        self.direction_x = 0
        self.direction_y = 0
        self.extra_aliens = pygame.sprite.Group()
        self.extra_alien_timer = 1000
        self.super_laser_timer = 8
        self.bonus_f_timer = 28
        self.bonus_pr_timer = 35

    def create(self, rows: int, cols: int, x_distance=60, y_distance=48, x_offset=90, y_offset=100):
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
                self.direction_x = -1
                self.move_down()
            elif alien.rect.left <= 0:
                self.direction_x = 1
                self.move_down()

    def move_down(self):
        """
        moves alien's group y coordinate every time it's called
        """
        if self.aliens:
            for alien in self.aliens.sprites():
                alien.rect.y += self.direction_y

    def shoot(self):
        """selects a random shooting enemy"""
        if self.aliens.sprites():
            random_alien = choice(self.aliens.sprites())
            self.super_laser_timer -= 1
            if self.super_laser_timer == 0:
                laser_sprite = Laser(random_alien.rect.center, 5, pi / 2, self.screen_width, True)
                self.aliens_lasers.add(laser_sprite)
                self.super_laser_timer = 8
            else:
                laser_sprite = Laser(random_alien.rect.center, 5, pi / 2, self.screen_width)
                self.aliens_lasers.add(laser_sprite)

    def give_bonus(self):
        """selects a random enemy that shoots bonuses"""
        if self.aliens.sprites():
            random_alien = choice(self.aliens.sprites())
            self.bonus_f_timer -= 1
            self.bonus_pr_timer -= 1
            if self.bonus_f_timer == 0:
                bonus_sprite = Bonus(random_alien.rect.center, 5, BonusType.firing_acceleration.value)
                self.aliens_f_bonuses.add(bonus_sprite)
                self.bonus_f_timer = 28
            elif self.bonus_pr_timer == 0:
                bonus_sprite = Bonus(random_alien.rect.center, 5, BonusType.protection.value)
                self.aliens_pr_bonuses.add(bonus_sprite)
                self.bonus_pr_timer = 41

    def check_extra_alien_timer(self):
        """updates extra alien timer and creates new extra alien if timer time is out"""
        self.extra_alien_timer -= 1
        if self.extra_alien_timer <= 0:
            self.extra_aliens.add(ExtraAlien(-10, 40, self.screen_width))
            self.extra_alien_timer = 1000

    def update(self):
        """updates the state of aliens"""
        self.aliens_lasers.update()
        self.aliens_f_bonuses.update()
        self.aliens_pr_bonuses.update()
        self.check_position()
        self.check_extra_alien_timer()
        for alien in self.aliens:
            alien.update(self.direction_x)
        for extra_alien in self.extra_aliens:
            extra_alien.update()
