import pygame
from game.alien_controller import AlienController
from player import Player
from obstacles import Obstacles


class GameController:
    def __init__(self, screen_width, screen_height):
        self.running = True
        self.player = Player((screen_width / 2, screen_height), screen_width)
        self.player_sprite = pygame.sprite.GroupSingle(self.player)
        self.obstacles = Obstacles(screen_width)
        self.alien_controller = AlienController(5, 8, screen_width, screen_height)

    def check_sprite(self, sprites, *args):
        for spr in sprites:
            for arg in args:
                if pygame.sprite.spritecollide(spr, arg, True):
                    spr.kill()

    def collision_check(self):
        if self.player.lasers.sprites():
            self.check_sprite(self.player.lasers.sprites(), self.obstacles.blocks, self.alien_controller.aliens)
        if self.alien_controller.aliens_lasers:
            self.check_sprite(self.alien_controller.aliens_lasers.sprites(), self.obstacles.blocks)
            for laser in self.alien_controller.aliens_lasers.sprites():
                if pygame.sprite.spritecollide(laser, self.player_sprite, False):
                    laser.kill()
                    self.player.number_of_lives -= 1
                    if self.player.number_of_lives == 0:
                        self.running = False

    def run(self):
        if self.running:
            self.player.update()
            self.alien_controller.update()
            self.collision_check()

        if not self.alien_controller.aliens:
            self.running = False
