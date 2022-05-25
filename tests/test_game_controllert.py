import unittest
import pygame
from math import pi
from game.game_controller import GameController
from game.alien_group import AlienGroup
from game.laser import Laser
from game.extra_alien import ExtraAlien
from game.bonus import Bonus
from game.bonus_type import BonusType


class GameControllerTestCase(unittest.TestCase):
    pygame.mixer.init()

    def test_collision_check_with_player_laser_and_alien_number_of_aliens_should_decrease(self):
        game_controller = GameController(600, 600, 1, 3)
        player = game_controller.player
        aliens = game_controller.alien_group.aliens

        player.shoot_laser(pi/2.5)
        for i in range(100):
            player.lasers.update()
            game_controller.collision_check()

        count_of_aliens = len(aliens)
        expected_count_of_aliens = len(GameController(600, 600, 1, 3).alien_group.aliens) - 1
        self.assertEqual(expected_count_of_aliens, count_of_aliens)

    def test_collision_check_with_player_laser_and_obstacle_number_of_blocks_should_decrease(self):
        game_controller = GameController(600, 600, 1, 3)
        player = game_controller.player
        obstacles_blocks = game_controller.obstacles.blocks

        player.shoot_laser(3*pi/4)
        for i in range(100):
            player.lasers.update()
            game_controller.collision_check()

        count_of_blocks = len(obstacles_blocks)
        expected_count_of_blocks = len(GameController(600, 600, 1, 3).obstacles.blocks) - 2
        self.assertEqual(expected_count_of_blocks, count_of_blocks)

    def test_collision_check_with_alien_laser_and_obstacle_number_of_blocks_should_decrease(self):
        game_controller = GameController(600, 600, 1, 3)
        alien_group = game_controller.alien_group
        obstacles_blocks = game_controller.obstacles.blocks

        alien = alien_group.aliens.sprites().pop(13)
        laser_sprite = Laser(alien.rect.center, 5, pi / 2, 600)
        alien_group.aliens_lasers.add(laser_sprite)

        for i in range(100):
            alien_group.aliens_lasers.update()
            game_controller.collision_check()

        count_of_blocks = len(obstacles_blocks)
        expected_count_of_blocks = len(GameController(600, 600, 1, 3).obstacles.blocks) - 2
        self.assertEqual(expected_count_of_blocks, count_of_blocks)

    def test_collision_check_with_alien_laser_and_player_number_of_player_lives_should_decrease(self):
        game_controller = GameController(600, 600, 1, 3)
        alien_group = game_controller.alien_group
        player = game_controller.player

        alien = alien_group.aliens.sprites().pop(28)
        laser_sprite = Laser(alien.rect.center, 5, pi / 2, 600)
        alien_group.aliens_lasers.add(laser_sprite)

        for i in range(100):
            alien_group.aliens_lasers.update()
            game_controller.collision_check()

        count_of_player_lives = player.number_of_lives
        expected_count_of_player_lives = GameController(600, 600, 1, 3).player.number_of_lives - 1
        self.assertEqual(expected_count_of_player_lives, count_of_player_lives)

    def test_check_collision_with_player_with_zero_player_lives_game_should_stop(self):
        game_controller = GameController(600, 600, 1, 1)
        alien_group = game_controller.alien_group

        alien = alien_group.aliens.sprites().pop(28)
        laser_sprite = Laser(alien.rect.center, 5, pi / 2, 600)
        alien_group.aliens_lasers.add(laser_sprite)

        for i in range(100):
            alien_group.aliens_lasers.update()
            game_controller.collision_check()

        self.assertFalse(game_controller.running)

    def test_collision_with_player_when_player_is_protected_lives_count_not_changes(self):
        game_controller = GameController(600, 600, 1, 1)
        player = game_controller.player
        alien_group = game_controller.alien_group
        player.is_protected = True

        alien = alien_group.aliens.sprites().pop(28)
        laser_sprite = Laser(alien.rect.center, 5, pi / 2, 600)
        alien_group.aliens_lasers.add(laser_sprite)

        for i in range(100):
            alien_group.aliens_lasers.update()
            game_controller.collision_check()

        expected_count_of_lives = 1
        count_of_lives = player.number_of_lives
        self.assertEqual(expected_count_of_lives, count_of_lives)

    def test_check_laser_collision_with_extra_alien_number_of_player_lives_should_increase(self):
        game_controller = GameController(600, 600, 1, 3)
        player = game_controller.player
        player.lasers.add(Laser((0, 0), 1, pi/2, 600))
        extra_aliens = game_controller.alien_group.extra_aliens
        extra_aliens.add(ExtraAlien(0, 0, 600))
        game_controller.check_laser_collision_with_extra_alien(player.lasers, extra_aliens)

        number_of_player_lives = game_controller.player.number_of_lives
        expected_number_of_player_lives = GameController(600, 600, 1, 3).player.number_of_lives + 1
        self.assertEqual(expected_number_of_player_lives, number_of_player_lives)

    def test_check_laser_collision_with_extra_alien_number_of_extra_aliens_should_decrease(self):
        game_controller = GameController(600, 600, 1, 3)
        player = game_controller.player
        player.lasers.add(Laser((0, 0), 1, pi / 2, 600))
        extra_aliens = game_controller.alien_group.extra_aliens
        extra_aliens.add(ExtraAlien(0, 0, 600))
        game_controller.check_laser_collision_with_extra_alien(player.lasers, extra_aliens)

        number_of_extra_aliens = len(game_controller.alien_group.extra_aliens)
        expected_number_of_extra_aliens = 0
        self.assertEqual(expected_number_of_extra_aliens, number_of_extra_aliens)

    def test_aliens_and_obstacles_collision_game_should_stop(self):
        game_controller = GameController(600, 600, 1, 3)
        alien_group = game_controller.alien_group
        alien_group.direction_y = 1
        for i in range(300):
            alien_group.move_down()
        obstacles = game_controller.obstacles.blocks
        game_controller.check_aliens_and_obstacles_collision(alien_group.aliens, obstacles)

        self.assertFalse(game_controller.running)

    def test_check_firing_acceleration_bonus_collision_with_player_f_bonuses_count_should_decrease(self):
        game_controller = GameController(600, 600, 1, 3)
        aliens_f_bonuses = game_controller.alien_group.aliens_f_bonuses
        bonus = Bonus((300, 600), 1, BonusType.firing_acceleration.value)
        aliens_f_bonuses.add(bonus)
        game_controller.collision_check()

        count_of_aliens_f_bonuses = len(aliens_f_bonuses)
        expected_count_of_aliens_f_bonuses = 0
        self.assertEqual(expected_count_of_aliens_f_bonuses, count_of_aliens_f_bonuses)

    def test_check_firing_acceleration_bonus_collision_with_player_f_timer_should_increase(self):
        game_controller = GameController(600, 600, 1, 3)
        aliens_f_bonuses = game_controller.alien_group.aliens_f_bonuses
        bonus = Bonus((300, 600), 1, BonusType.firing_acceleration.value)
        aliens_f_bonuses.add(bonus)
        game_controller.collision_check()

        f_timer_time = game_controller.player.bonus_f_timer
        previous_f_timer_time = GameController(600, 600, 1, 3).player.bonus_f_timer
        self.assertGreater(f_timer_time, previous_f_timer_time)

    def test_check_firing_acceleration_bonus_collision_with_player_cooldown_should_decrease(self):
        game_controller = GameController(600, 600, 1, 3)
        aliens_f_bonuses = game_controller.alien_group.aliens_f_bonuses
        bonus = Bonus((300, 600), 1, BonusType.firing_acceleration.value)
        aliens_f_bonuses.add(bonus)
        game_controller.collision_check()

        cooldown = game_controller.player.laser_cooldown
        previous_cooldown = GameController(600, 600, 1, 3).player.laser_cooldown
        self.assertLess(cooldown, previous_cooldown)

    def test_check_protection_bonus_collision_with_player_pr_bonuses_count_should_decrease(self):
        game_controller = GameController(600, 600, 1, 3)
        aliens_pr_bonuses = game_controller.alien_group.aliens_pr_bonuses
        bonus = Bonus((300, 600), 1, BonusType.protection.value)
        aliens_pr_bonuses.add(bonus)
        game_controller.collision_check()

        count_of_aliens_pr_bonuses = len(aliens_pr_bonuses)
        expected_count_of_aliens_pr_bonuses = 0
        self.assertEqual(expected_count_of_aliens_pr_bonuses, count_of_aliens_pr_bonuses)

    def test_check_protection_bonus_collision_with_player_pr_timer_should_increase(self):
        game_controller = GameController(600, 600, 1, 3)
        aliens_pr_bonuses = game_controller.alien_group.aliens_pr_bonuses
        bonus = Bonus((300, 600), 1, BonusType.protection.value)
        aliens_pr_bonuses.add(bonus)
        game_controller.collision_check()

        pr_timer_time = game_controller.player.bonus_pr_timer
        previous_pr_timer_time = GameController(600, 600, 1, 3).player.bonus_pr_timer
        self.assertGreater(pr_timer_time, previous_pr_timer_time)

    def test_check_protection_bonus_collision_with_player_is_protected_flag_should_be_true(self):
        game_controller = GameController(600, 600, 1, 3)
        aliens_pr_bonuses = game_controller.alien_group.aliens_pr_bonuses
        bonus = Bonus((300, 600), 1, BonusType.protection.value)
        aliens_pr_bonuses.add(bonus)
        game_controller.collision_check()

        is_protected = game_controller.player.is_protected
        self.assertTrue(is_protected)

    def test_check_bonus_collision_with_obstacle_bonuses_count_should_decrease(self):
        game_controller = GameController(600, 600, 1, 3)
        bonuses = game_controller.alien_group.aliens_pr_bonuses
        bonus = Bonus((40, 480), 1, BonusType.protection.value)
        bonuses.add(bonus)
        game_controller.collision_check()

        count_of_bonuses = len(bonuses)
        expected_count_of_bonuses = 0
        self.assertEqual(expected_count_of_bonuses, count_of_bonuses)

    def test_set_new_level_for_level_2_aliens_direction_x_should_set(self):
        game_controller = GameController(600, 600, 2, 3)

        aliens_direction_x = game_controller.alien_group.direction_x
        expected_aliens_direction_x = 1
        self.assertEqual(expected_aliens_direction_x, aliens_direction_x)

    def test_set_new_level_for_level_3_aliens_direction_x_and_direction_y_should_set(self):
        game_controller = GameController(600, 600, 3, 3)

        aliens_direction_x = game_controller.alien_group.direction_x
        expected_aliens_direction_x = 1
        aliens_direction_y = game_controller.alien_group.direction_y
        expected_aliens_direction_y = 1
        self.assertEqual(expected_aliens_direction_x, aliens_direction_x)
        self.assertEqual(expected_aliens_direction_y, aliens_direction_y)

    def test_run_form_timer_should_change_after_call(self):
        pygame.init()
        game_controller = GameController(600, 600, 1, 3)
        game_controller.run()

        current_timer = game_controller.form_timer
        previous_timer = GameController(600, 600, 1, 3).form_timer
        self.assertLess(current_timer, previous_timer)

    def test_run_with_no_aliens_game_should_stop(self):
        pygame.init()
        game_controller = GameController(600, 600, 1, 3)
        game_controller.alien_group = AlienGroup(0, 0, 600, 600)
        game_controller.run()

        self.assertFalse(game_controller.running)


if __name__ == '__main__':
    unittest.main()
