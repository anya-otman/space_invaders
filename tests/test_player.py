import unittest
from game.player import Player
from math import pi


class PlayerTestCase(unittest.TestCase):
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
        player.shoot_laser(pi/2)

        count_of_lasers = len(player.lasers)
        expected_count_of_lasers = 1
        self.assertEqual(expected_count_of_lasers, count_of_lasers)


if __name__ == '__main__':
    unittest.main()
