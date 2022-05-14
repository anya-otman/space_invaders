import unittest
from game.alien_group import AlienGroup


class AlienGroupTestCase(unittest.TestCase):
    def test_create_with_positive_number_of_rows_and_columns(self):
        alien_group = AlienGroup(2, 2, 600, 600)

        aliens_count = len(alien_group.aliens)
        expected_aliens_count = 4
        self.assertEqual(expected_aliens_count, aliens_count)

    def test_create_with_zero_number_of_rows_and_columns(self):
        alien_group = AlienGroup(0, 0, 600, 600)

        aliens_count = len(alien_group.aliens)
        expected_aliens_count = 0
        self.assertEqual(expected_aliens_count, aliens_count)

    def test_create_with_negative_number_of_rows_and_columns(self):
        alien_group = AlienGroup(-2, -2, 600, 600)

        aliens_count = len(alien_group.aliens)
        expected_aliens_count = 0
        self.assertEqual(expected_aliens_count, aliens_count)

    def test_create_with_negative_number_of_rows_and_positive_number_of_columns(self):
        alien_group = AlienGroup(-2, 2, 600, 600)

        aliens_count = len(alien_group.aliens)
        expected_aliens_count = 0
        self.assertEqual(expected_aliens_count, aliens_count)

    def test_chek_position_with_positive_direction(self):
        alien_group = AlienGroup(5, 8, 600, 600)
        for i in range(100):
            alien_group.update()

        alien_group_direction = alien_group.direction
        expected_alien_group_direction = -1
        self.assertEqual(expected_alien_group_direction, alien_group_direction)

    def test_chek_position_with_negative_direction(self):
        alien_group = AlienGroup(5, 8, 600, 600)
        alien_group.direction = -1
        for i in range(100):
            alien_group.update()

        alien_group_direction = alien_group.direction
        expected_alien_group_direction = 1
        self.assertEqual(expected_alien_group_direction, alien_group_direction)

    def test_shoot_with_aliens_one_call_one_laser(self):
        alien_group = AlienGroup(2, 2, 600, 600)
        alien_group.shoot()

        count_of_aliens_lasers = len(alien_group.aliens_lasers)
        expected_count_of_aliens_lasers = 1
        self.assertEqual(expected_count_of_aliens_lasers, count_of_aliens_lasers)

    def test_shoot_with_aliens_five_calls_five_lasers(self):
        alien_group = AlienGroup(2, 2, 600, 600)
        for i in range(5):
            alien_group.shoot()

        count_of_aliens_lasers = len(alien_group.aliens_lasers)
        expected_count_of_aliens_lasers = 5
        self.assertEqual(expected_count_of_aliens_lasers, count_of_aliens_lasers)

    def test_shoot_without_aliens_one_call_no_lasers(self):
        alien_group = AlienGroup(0, 0, 600, 600)
        alien_group.shoot()

        count_of_aliens_lasers = len(alien_group.aliens_lasers)
        expected_count_of_aliens_lasers = 0
        self.assertEqual(expected_count_of_aliens_lasers, count_of_aliens_lasers)


if __name__ == '__main__':
    unittest.main()
