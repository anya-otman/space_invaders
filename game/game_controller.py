import pygame
from game.alien_group import AlienGroup
from game.player import Player
from game.obstacles import Obstacles


class GameController:
    def __init__(self, screen_width: int, screen_height: int, level: int, player_lives: int):
        self.running = True
        self.form_timer = 100
        self.level = level
        self.player = Player((screen_width / 2, screen_height), screen_width, player_lives)
        self.player_sprite = pygame.sprite.GroupSingle(self.player)
        self.obstacles = Obstacles(screen_width)
        self.alien_group = AlienGroup(5, 8, screen_width, screen_height)
        self.set_new_level()

    def collision_check(self):
        """checks laser and player or obstacle collision"""
        if self.player.lasers.sprites():
            self.check_laser_collision_with_game_object(self.player.lasers, self.obstacles.blocks,
                                                        self.alien_group.aliens)
            self.check_laser_collision_with_extra_alien(self.player.lasers, self.alien_group.extra_aliens)
        if self.alien_group.aliens_lasers:
            self.check_laser_collision_with_game_object(self.alien_group.aliens_lasers, self.obstacles.blocks)
            self.check_laser_collision_with_player(self.alien_group.aliens_lasers.sprites(), self.player_sprite)
        self.check_aliens_and_obstacles_collision(self.alien_group.aliens, self.obstacles.blocks)

    def check_laser_collision_with_game_object(self, lasers: list, *args):
        """
        checks laser and game object collision and deletes an object if a collision has occurred
        :param lasers: list of laser's sprites
        :param args: other game object's sprites
        """
        for laser in lasers:
            for arg in args:
                if pygame.sprite.spritecollide(laser, arg, True):
                    if not laser.super_laser:
                        laser.kill()

    def check_laser_collision_with_player(self, alien_lasers: list, player):
        """
        checks alien laser and player collision and decreases count of player lives if a collision has occurred
        :param alien_lasers: list of aliens lasers sprites
        :param player: player sprite
        """
        for laser in alien_lasers:
            if pygame.sprite.spritecollide(laser, player, False):
                laser.kill()
                self.player.number_of_lives -= 1
                if self.player.number_of_lives == 0:
                    self.running = False

    def check_laser_collision_with_extra_alien(self, player_lasers: list, extra_aliens):
        """
        checks player laser and extra alien collision and increases count of player lives if a collision has occurred
        :param player_lasers: list of player laser's sprites
        :param extra_aliens: group of extra alien's sprites
        """
        for laser in player_lasers:
            if pygame.sprite.spritecollide(laser, extra_aliens, True):
                laser.kill()
                if self.player.number_of_lives < 5:
                    self.player.number_of_lives += 1

    def check_aliens_and_obstacles_collision(self, aliens: list, blocks):
        """
        checks aliens and obstacles collision and ends the game if a collision has occurred
        :param aliens: list of aliens
        :param blocks: group of blocks
        """
        if aliens:
            for alien in aliens:
                if pygame.sprite.spritecollide(alien, blocks, False):
                    self.running = False

    def set_new_level(self):
        """sets new level params when the GameController instantiated"""
        if self.level == 2:
            self.alien_group.direction_x = 1
        elif self.level == 3:
            self.alien_group.direction_x = 1
            self.alien_group.direction_y = 1

    def run(self):
        """updates the state of all game objects"""
        if self.running:
            if self.form_timer != 0:
                self.form_timer -= 1
            self.player.update()
            self.alien_group.update()
            self.collision_check()

        if not self.alien_group.aliens:
            self.running = False
