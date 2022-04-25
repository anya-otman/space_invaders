import pygame
from laser import Laser


class Player(pygame.sprite.Sprite):
    def __init__(self, position, constraint):
        super().__init__()
        self.image = pygame.image.load("images/player.png")
        self.rect = pygame.Surface((60, 30)).get_rect(midbottom=position)
        self.max_x_constraint = constraint
        self.ready = True
        self.laser_time = 0
        self.laser_cooldown = 600  # shoot every 600 milliseconds

        self.lasers = pygame.sprite.Group()

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.move_right()

        if keys[pygame.K_LEFT]:
            self.move_left()

        if keys[pygame.K_SPACE] and self.ready:
            self.shoot_laser()
            self.ready = False
            self.laser_time = pygame.time.get_ticks()

    def move_right(self):
        if self.rect.right >= self.max_x_constraint:
            self.rect.right = self.max_x_constraint
        else:
            self.rect.x += 1

    def move_left(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        else:
            self.rect.x -= 1

    def recharge(self):
        if not self.ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_time >= self.laser_cooldown:
                self.ready = True

    def shoot_laser(self):
        self.lasers.add(Laser(self.rect.center, -1, self.rect.bottom))

    def update(self):
        self.get_input()
        self.recharge()
        self.lasers.update()
