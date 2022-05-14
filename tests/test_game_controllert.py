import unittest
import pygame
from math import pi
from game.game_controller import GameController
from game.alien_group import AlienGroup
from game.laser import Laser


class GameControllerTestCase(unittest.TestCase):
    def test_collision_check_with_player_laser_and_alien(self):
        game_controller = GameController(600, 600)
        player = game_controller.player
        aliens = game_controller.alien_group.aliens

        player.shoot_laser(pi/2)
        for i in range(100):
            player.lasers.update()
            game_controller.collision_check()

        count_of_aliens = len(aliens)
        expected_count_of_aliens = len(GameController(600, 600).alien_group.aliens) - 1
        self.assertEqual(expected_count_of_aliens, count_of_aliens)

    def test_collision_check_with_player_laser_and_obstacle(self):
        game_controller = GameController(600, 600)
        player = game_controller.player
        obstacles_blocks = game_controller.obstacles.blocks

        player.shoot_laser(3*pi/4)
        for i in range(100):
            player.lasers.update()
            game_controller.collision_check()

        count_of_blocks = len(obstacles_blocks)
        expected_count_of_blocks = len(GameController(600, 600).obstacles.blocks) - 2
        self.assertEqual(expected_count_of_blocks, count_of_blocks)

    def test_collision_check_with_alien_laser_and_obstacle(self):
        game_controller = GameController(600, 600)
        alien_group = game_controller.alien_group
        obstacles_blocks = game_controller.obstacles.blocks

        alien = alien_group.aliens.sprites().pop(2)
        laser_sprite = Laser(alien.rect.center, 5, pi / 2, 600)
        alien_group.aliens_lasers.add(laser_sprite)

        for i in range(100):
            alien_group.aliens_lasers.update()
            game_controller.collision_check()

        count_of_blocks = len(obstacles_blocks)
        expected_count_of_blocks = len(GameController(600, 600).obstacles.blocks) - 1
        self.assertEqual(expected_count_of_blocks, count_of_blocks)

    def test_collision_check_with_alien_laser_and_player(self):
        game_controller = GameController(600, 600)
        alien_group = game_controller.alien_group
        player = game_controller.player

        alien = alien_group.aliens.sprites().pop(28)
        laser_sprite = Laser(alien.rect.center, 5, pi / 2, 600)
        alien_group.aliens_lasers.add(laser_sprite)

        for i in range(100):
            alien_group.aliens_lasers.update()
            game_controller.collision_check()

        count_of_player_lives = player.number_of_lives
        expected_count_of_player_lives = GameController(600, 600).player.number_of_lives - 1
        self.assertEqual(expected_count_of_player_lives, count_of_player_lives)

    def test_check_collision_with_player_with_zero_player_lives_game_should_stop(self):
        game_controller = GameController(600, 600)
        player = game_controller.player
        alien_group = game_controller.alien_group
        player.number_of_lives = 1

        alien = alien_group.aliens.sprites().pop(28)
        laser_sprite = Laser(alien.rect.center, 5, pi / 2, 600)
        alien_group.aliens_lasers.add(laser_sprite)

        for i in range(100):
            alien_group.aliens_lasers.update()
            game_controller.collision_check()

        self.assertFalse(game_controller.running)

    def test_run_with_no_aliens_game_should_stop(self):
        pygame.init()
        game_controller = GameController(600, 600)
        game_controller.alien_group = AlienGroup(0, 0, 600, 600)

        game_controller.run()

        self.assertFalse(game_controller.running)


if __name__ == '__main__':
    unittest.main()
