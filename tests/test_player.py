import unittest
import pygame
from game.player import Player
from math import pi
from unittest.mock import patch, MagicMock


class PlayerTestCase(unittest.TestCase):
    pygame.mixer.init()

    def test_move_left(self):
        player = Player((100, 100), 600, 3)
        player.move_left()

        player_x_coordinate = player.rect.x
        expected_player_x_coordinate = Player((95, 100), 600, 3).rect.x
        self.assertEqual(expected_player_x_coordinate, player_x_coordinate)

    def test_move_right(self):
        player = Player((100, 100), 600, 3)
        player.move_right()

        player_x_coordinate = player.rect.x
        expected_player_x_coordinate = Player((105, 100), 600, 3).rect.x
        self.assertEqual(expected_player_x_coordinate, player_x_coordinate)

    def test_move_left_with_constraint(self):
        player = Player((-1, 0), 600, 3)
        player.move_left()

        player_x_coordinate = player.rect.left
        expected_player_x_coordinate = 0
        self.assertEqual(expected_player_x_coordinate, player_x_coordinate)

    def test_move_right_with_constraint(self):
        player = Player((601, 0), 600, 3)
        player.move_right()

        player_x_coordinate = player.rect.right
        expected_player_x_coordinate = 600
        self.assertEqual(expected_player_x_coordinate, player_x_coordinate)

    def test_shoot_laser(self):
        player = Player((0, 0), 600, 3)
        player.shoot_laser(pi / 2)

        count_of_lasers = len(player.lasers)
        expected_count_of_lasers = 1
        self.assertEqual(expected_count_of_lasers, count_of_lasers)

    def test_check_bonus_timers_should_change_bonus_timers_after_call(self):
        player = Player((0, 0), 600, 3)
        player.bonus_f_timer = 2
        player.bonus_pr_timer = 2
        player.check_bonus_timers()

        bonus_f_timer = player.bonus_f_timer
        expected_bonus_f_timer = 1
        bonus_pr_timer = player.bonus_pr_timer
        expected_bonus_pr_timer = 1
        self.assertEqual(expected_bonus_f_timer, bonus_f_timer)
        self.assertEqual(expected_bonus_pr_timer, bonus_pr_timer)

    def test_check_bonus_timers_when_f_timer_is_out_should_set_normal_value_of_laser_cooldown(self):
        player = Player((0, 0), 600, 3)
        player.laser_cooldown = 300
        player.check_bonus_timers()

        normal_laser_cooldown = 600
        laser_cooldown = player.laser_cooldown
        self.assertEqual(normal_laser_cooldown, laser_cooldown)

    def test_check_bonus_timers_when_pr_timer_is_out_should_set_normal_value_of_is_protected_flag(self):
        player = Player((0, 0), 600, 3)
        player.is_protected = True
        player.check_bonus_timers()

        self.assertFalse(player.is_protected)

    @patch('game.player.pygame', new_callable=MagicMock)
    def test_get_input_key_right_is_pressed_move_right_should_be_called(self, pygame_mock):
        player = MagicMock()
        pygame_mock.key.get_pressed.return_value = {pygame_mock.K_RIGHT: True, pygame_mock.K_LEFT: False,
                                                    pygame_mock.K_SPACE: False, pygame_mock.K_UP: False,
                                                    pygame_mock.K_DOWN: False}
        Player.get_input(player)
        player.move_right.assert_called_once_with()
        # assert not player.ready_to_shoot

    @patch('game.player.pygame', new_callable=MagicMock)
    def test_get_input_key_left_is_pressed_move_left_should_be_called(self, pygame_mock):
        player = MagicMock()
        pygame_mock.key.get_pressed.return_value = {pygame_mock.K_RIGHT: False, pygame_mock.K_LEFT: True,
                                                    pygame_mock.K_SPACE: False, pygame_mock.K_UP: False,
                                                    pygame_mock.K_DOWN: False}
        Player.get_input(player)
        player.move_left.assert_called_once_with()

    @patch('game.player.pygame', new_callable=MagicMock)
    def test_get_input_key_space_is_pressed_ready_to_shoot_becomes_false(self, pygame_mock):
        player = MagicMock()
        player.ready_to_shoot = True
        pygame_mock.key.get_pressed.return_value = {pygame_mock.K_RIGHT: False, pygame_mock.K_LEFT: False,
                                                    pygame_mock.K_SPACE: True, pygame_mock.K_UP: False,
                                                    pygame_mock.K_DOWN: False}
        Player.get_input(player)
        self.assertFalse(player.ready_to_shoot)

    @patch('game.player.pygame', new_callable=MagicMock)
    def test_get_input_key_space_is_pressed_shoot_laser_should_be_called(self, pygame_mock):
        player = MagicMock()
        player.ready_to_shoot = True
        pygame_mock.key.get_pressed.return_value = {pygame_mock.K_RIGHT: False, pygame_mock.K_LEFT: False,
                                                    pygame_mock.K_SPACE: True, pygame_mock.K_UP: False,
                                                    pygame_mock.K_DOWN: False}
        Player.get_input(player)
        player.shoot_laser.assert_called_once_with(pi/2)

    @patch('game.player.pygame', new_callable=MagicMock)
    def test_get_input_key_up_is_pressed_ready_to_shoot_becomes_false(self, pygame_mock):
        player = MagicMock()
        player.ready_to_shoot = True
        pygame_mock.key.get_pressed.return_value = {pygame_mock.K_RIGHT: False, pygame_mock.K_LEFT: False,
                                                    pygame_mock.K_SPACE: False, pygame_mock.K_UP: True,
                                                    pygame_mock.K_DOWN: False}
        Player.get_input(player)
        self.assertFalse(player.ready_to_shoot)

    @patch('game.player.pygame', new_callable=MagicMock)
    def test_get_input_key_up_is_pressed_shoot_laser_should_be_called(self, pygame_mock):
        player = MagicMock()
        player.ready_to_shoot = True
        pygame_mock.key.get_pressed.return_value = {pygame_mock.K_RIGHT: False, pygame_mock.K_LEFT: False,
                                                    pygame_mock.K_SPACE: False, pygame_mock.K_UP: True,
                                                    pygame_mock.K_DOWN: False}
        Player.get_input(player)
        player.shoot_laser.assert_called_once_with(3*pi/4)

    @patch('game.player.pygame', new_callable=MagicMock)
    def test_get_input_key_down_is_pressed_ready_to_shoot_becomes_false(self, pygame_mock):
        player = MagicMock()
        player.ready_to_shoot = True
        pygame_mock.key.get_pressed.return_value = {pygame_mock.K_RIGHT: False, pygame_mock.K_LEFT: False,
                                                    pygame_mock.K_SPACE: False, pygame_mock.K_UP: False,
                                                    pygame_mock.K_DOWN: True}
        Player.get_input(player)
        self.assertFalse(player.ready_to_shoot)

    @patch('game.player.pygame', new_callable=MagicMock)
    def test_get_input_key_down_is_pressed_shoot_laser_should_be_called(self, pygame_mock):
        player = MagicMock()
        player.ready_to_shoot = True
        pygame_mock.key.get_pressed.return_value = {pygame_mock.K_RIGHT: False, pygame_mock.K_LEFT: False,
                                                    pygame_mock.K_SPACE: False, pygame_mock.K_UP: False,
                                                    pygame_mock.K_DOWN: True}
        Player.get_input(player)
        player.shoot_laser.assert_called_once_with(pi / 4)


if __name__ == '__main__':
    unittest.main()
