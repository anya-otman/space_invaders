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
        alien_group.direction_x = 1
        for i in range(100):
            alien_group.update()

        alien_group_direction_x = alien_group.direction_x
        expected_alien_group_direction_x = -1
        self.assertEqual(expected_alien_group_direction_x, alien_group_direction_x)

    def test_chek_position_with_negative_direction(self):
        alien_group = AlienGroup(5, 8, 600, 600)
        alien_group.direction_x = -1
        for i in range(100):
            alien_group.update()

        alien_group_direction_x = alien_group.direction_x
        expected_alien_group_direction_x = 1
        self.assertEqual(expected_alien_group_direction_x, alien_group_direction_x)

    def test_move_down(self):
        alien_group = AlienGroup(5, 8, 600, 600)
        alien_group.direction_y = 1
        alien_group.move_down()

        alien_y = alien_group.aliens.sprites().pop(1).rect.y
        expected_alien_y = AlienGroup(5, 8, 600, 600).aliens.sprites().pop(1).rect.y + 1
        self.assertEqual(expected_alien_y, alien_y)

    def test_check_position_with_move_down_direction_x_and_coordinate_y_should_change(self):
        alien_group = AlienGroup(5, 8, 600, 600)
        alien_group.direction_x = 1
        alien_group.direction_y = 1
        for i in range(100):
            alien_group.update()

        alien_group_direction_x = alien_group.direction_x
        expected_alien_group_direction_x = -1
        alien_y = alien_group.aliens.sprites().pop(1).rect.y
        expected_alien_y = AlienGroup(5, 8, 600, 600).aliens.sprites().pop(1).rect.y + 5
        self.assertEqual(expected_alien_group_direction_x, alien_group_direction_x)
        self.assertEqual(expected_alien_y, alien_y)

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

    def test_check_extra_alien_timer_one_call_no_extra_aliens(self):
        alien_group = AlienGroup(2, 2, 600, 600)
        alien_group.check_extra_alien_timer()

        count_of_extra_aliens = len(alien_group.extra_aliens)
        expected_count_of_extra_aliens = 0
        self.assertEqual(expected_count_of_extra_aliens, count_of_extra_aliens)

    def test_check_extra_alien_timer_several_calls_one_extra_alien(self):
        alien_group = AlienGroup(2, 2, 600, 600)
        for i in range(1000):
            alien_group.check_extra_alien_timer()

        count_of_extra_aliens = len(alien_group.extra_aliens)
        expected_count_of_extra_aliens = 1
        self.assertEqual(expected_count_of_extra_aliens, count_of_extra_aliens)

    def test_give_bonus_after_one_call_all_timers_should_change(self):
        alien_group = AlienGroup(2, 2, 600, 600)
        alien_group.bonus_pr_timer = 2
        alien_group.bonus_f_timer = 2
        alien_group.give_bonus()

        alien_group_bonus_pr_timer = alien_group.bonus_pr_timer
        expected_alien_group_bonus_pr_timer = 1

        alien_group_bonus_f_timer = alien_group.bonus_f_timer
        expected_alien_group_bonus_f_timer = 1
        self.assertEqual(expected_alien_group_bonus_f_timer, alien_group_bonus_f_timer)
        self.assertEqual(expected_alien_group_bonus_pr_timer, alien_group_bonus_pr_timer)

    def test_give_bonus_bonus_pr_timer_is_out_one_pr_bonus_should_appear(self):
        alien_group = AlienGroup(2, 2, 600, 600)
        alien_group.bonus_pr_timer = 1
        alien_group.give_bonus()

        count_of_pr_bonuses = len(alien_group.aliens_pr_bonuses)
        expected_count_of_pr_bonuses = 1
        self.assertEqual(expected_count_of_pr_bonuses, count_of_pr_bonuses)

    def test_give_bonus_bonus_f_timer_is_out_one_f_bonus_should_appear(self):
        alien_group = AlienGroup(2, 2, 600, 600)
        alien_group.bonus_f_timer = 1
        alien_group.give_bonus()

        count_of_f_bonuses = len(alien_group.aliens_f_bonuses)
        expected_count_of_f_bonuses = 1
        self.assertEqual(expected_count_of_f_bonuses, count_of_f_bonuses)


if __name__ == '__main__':
    unittest.main()
