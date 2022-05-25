import pygame
from game.alien_group import AlienGroup
from game.player import Player
from game.obstacles import Obstacles


class GameController:
    def __init__(self, screen_width: int, screen_height: int, level: int, player_lives: int):
        self.running = True
        self.is_victory_sound_play = False
        self.form_timer = 100
        self.level = level
        self.lives_at_beginning = player_lives
        self.player = Player((screen_width / 2, screen_height), screen_width, player_lives)
        self.player_sprite = pygame.sprite.GroupSingle(self.player)
        self.obstacles = Obstacles(screen_width)
        self.alien_group = AlienGroup(5, 8, screen_width, screen_height)
        self.explosion_sound = pygame.mixer.Sound("../music/explosion.wav")
        self.bonus_sound = pygame.mixer.Sound("../music/bonus.mp3")
        self.loss_sound = pygame.mixer.Sound("../music/loss.mp3")
        self.victory_sound = pygame.mixer.Sound("../music/victory.mp3")
        self.music = pygame.mixer.Sound("../music/music.mp3")
        self.music.play(loops=-1)
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
        if self.alien_group.aliens_f_bonuses:
            self.check_firing_acceleration_bonus_collision_with_player(self.alien_group.aliens_f_bonuses.sprites(),
                                                                       self.player_sprite)
            self.check_bonus_collision_with_obstacle(self.alien_group.aliens_f_bonuses.sprites(), self.obstacles.blocks)
        if self.alien_group.aliens_pr_bonuses:
            self.check_protection_bonus_collision_with_player(self.alien_group.aliens_pr_bonuses.sprites(),
                                                              self.player_sprite)
            self.check_bonus_collision_with_obstacle(self.alien_group.aliens_pr_bonuses.sprites(),
                                                     self.obstacles.blocks)

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
                        self.explosion_sound.play()

    def check_laser_collision_with_player(self, alien_lasers: list, player):
        """
        checks alien laser and player collision and decreases count of player lives if a collision has occurred
        :param alien_lasers: list of aliens lasers sprites
        :param player: player sprite
        """
        for laser in alien_lasers:
            if pygame.sprite.spritecollide(laser, player, False):
                laser.kill()
                if not self.player.is_protected:
                    self.player.number_of_lives -= 1
                    self.explosion_sound.play()
                if self.player.number_of_lives == 0:
                    self.running = False
                    self.music.stop()
                    self.loss_sound.play()

    def check_laser_collision_with_extra_alien(self, player_lasers: list, extra_aliens):
        """
        checks player laser and extra alien collision and increases count of player lives if a collision has occurred
        :param player_lasers: list of player laser's sprites
        :param extra_aliens: group of extra alien's sprites
        """
        for laser in player_lasers:
            if pygame.sprite.spritecollide(laser, extra_aliens, True):
                laser.kill()
                self.explosion_sound.play()
                if self.player.number_of_lives < 5:
                    self.player.number_of_lives += 1
                    self.bonus_sound.play()

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
                    self.music.stop()
                    self.loss_sound.play()

    def check_firing_acceleration_bonus_collision_with_player(self, bonuses: list, player):
        """
        checks firing acceleration bonus and player collision and decreases player's laser cooldown
        :param bonuses: list of bonuses
        :param player: player sprite
        """
        for bonus in bonuses:
            if pygame.sprite.spritecollide(bonus, player, False):
                bonus.kill()
                self.bonus_sound.play()
                self.player.bonus_f_timer = 800
                self.player.bonus_pr_timer = 0
                self.player.laser_cooldown = 300

    def check_protection_bonus_collision_with_player(self, bonuses: list, player):
        """
        checks protection bonus and player collision and protects the player from alien lasers
        :param bonuses: list of bonuses
        :param player: player sprite
        """
        for bonus in bonuses:
            if pygame.sprite.spritecollide(bonus, player, False):
                bonus.kill()
                self.bonus_sound.play()
                self.player.bonus_pr_timer = 500
                self.player.bonus_f_timer = 0
                self.player.is_protected = True

    def check_bonus_collision_with_obstacle(self, bonuses: list, blocks):
        """
        checks bonus and obstacle collision and deletes a bonus if a collision has occurred
        :param bonuses: list of bonuses
        :param blocks: group of blocks
        """
        for bonus in bonuses:
            if pygame.sprite.spritecollide(bonus, blocks, False):
                bonus.kill()
                self.explosion_sound.play()

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
            self.music.stop()
            if not self.is_victory_sound_play:
                self.victory_sound.play()
                self.is_victory_sound_play = True
