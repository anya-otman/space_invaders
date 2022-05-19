import pygame
from game.laser import Laser
from math import pi


class Player(pygame.sprite.Sprite):
    def __init__(self, position, constraint: int, lives: int):
        super().__init__()
        self.image = pygame.image.load("../images/player.png")
        self.rect = pygame.Surface((60, 30)).get_rect(midbottom=position)
        self.max_x_constraint = constraint
        self.number_of_lives = lives
        self.ready_to_shoot = True
        self.laser_time = 0
        self.laser_cooldown = 600  # shoot every 600 milliseconds
        self.lasers = pygame.sprite.Group()

    def get_input(self):
        """gets input from user's keyboard and calls the appropriate method"""
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.move_right()

        if keys[pygame.K_LEFT]:
            self.move_left()

        if keys[pygame.K_SPACE] and self.ready_to_shoot:
            self.shoot_laser(pi/2)
            self.ready_to_shoot = False
            self.laser_time = pygame.time.get_ticks()

        if keys[pygame.K_UP] and self.ready_to_shoot:
            self.shoot_laser(3*pi/4)
            self.ready_to_shoot = False
            self.laser_time = pygame.time.get_ticks()

        if keys[pygame.K_DOWN] and self.ready_to_shoot:
            self.shoot_laser(pi/4)
            self.ready_to_shoot = False
            self.laser_time = pygame.time.get_ticks()

    def move_right(self):
        """shifts the player to the right, checks right side of the player and doesn't allow this to move beyond the
        screen"""
        if self.rect.right >= self.max_x_constraint:
            self.rect.right = self.max_x_constraint
        else:
            self.rect.x += 5

    def move_left(self):
        """shifts the player to the left, checks left side of the player and doesn't allow this to move beyond the
        screen"""
        if self.rect.left <= 0:
            self.rect.left = 0
        else:
            self.rect.x -= 5

    def recharge(self):
        """resets the player's ability to shoot"""
        if not self.ready_to_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_time >= self.laser_cooldown:
                self.ready_to_shoot = True

    def shoot_laser(self, angle: float):
        """
        adds lasers to the container to draw later on the screen
        :param angle: the angle at which the laser will move
        """
        self.lasers.add(Laser(self.rect.center, -5, angle, self.max_x_constraint))

    def update(self):
        """updates the player's state"""
        self.get_input()
        self.recharge()
        self.lasers.update()
