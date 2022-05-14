import pygame
from game.alien_group import AlienGroup
from game.player import Player
from game.obstacles import Obstacles


class GameController:
    def __init__(self, screen_width: int, screen_height: int):
        self.running = True
        self.player = Player((screen_width / 2, screen_height), screen_width)
        self.player_sprite = pygame.sprite.GroupSingle(self.player)
        self.obstacles = Obstacles(screen_width)
        self.alien_group = AlienGroup(5, 8, screen_width, screen_height)

    def collision_check(self):
        """checks laser and player or obstacle collision"""
        if self.player.lasers.sprites():
            self.check_laser_collision_with_game_object(self.player.lasers, self.obstacles.blocks,
                                                        self.alien_group.aliens, self.alien_group.extra_aliens)
        if self.alien_group.aliens_lasers:
            self.check_laser_collision_with_game_object(self.alien_group.aliens_lasers, self.obstacles.blocks)
            self.check_collision_with_player(self.alien_group.aliens_lasers.sprites(), self.player_sprite)

    def check_laser_collision_with_game_object(self, lasers: list, *args):
        """checks collision and deletes an object if a collision has occurred"""
        for laser in lasers:
            for arg in args:
                if pygame.sprite.spritecollide(laser, arg, True):
                    if not laser.super_laser:
                        laser.kill()

    def check_collision_with_player(self, sprites: list, player):
        for laser in sprites:
            if pygame.sprite.spritecollide(laser, player, False):
                laser.kill()
                self.player.number_of_lives -= 1
                if self.player.number_of_lives == 0:
                    self.running = False

    def run(self):
        """updates the state of all game objects"""
        if self.running:
            self.player.update()
            self.alien_group.update()
            self.collision_check()

        if not self.alien_group.aliens:
            self.running = False
