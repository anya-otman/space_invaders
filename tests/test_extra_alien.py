import unittest
import pygame.sprite
from game.extra_alien import ExtraAlien


class ExtraAlienTestCase(unittest.TestCase):
    def test_update_coordinate_x_should_change(self):
        extra_alien = ExtraAlien(0, 0, 600)
        extra_alien.update()

        extra_alien_x = extra_alien.rect.x
        expected_extra_alien_x = ExtraAlien(2, 0, 600).rect.x
        self.assertEqual(expected_extra_alien_x, extra_alien_x)

    def test_destroy_coordinate_x_not_greater_than_screen_width(self):
        extra_alien_list = []
        extra_alien = ExtraAlien(5, 0, 600)
        extra_alien_list.append(extra_alien)
        extra_alien.destroy()

        count_of_extra_aliens = len(extra_alien_list)
        expected_count_of_extra_aliens = 1
        self.assertEqual(expected_count_of_extra_aliens, count_of_extra_aliens)

    def test_destroy_coordinate_x_greater_than_screen_width(self):
        extra_alien_list = pygame.sprite.Group()
        extra_alien = ExtraAlien(650, 0, 600)
        extra_alien_list.add(extra_alien)
        extra_alien.destroy()

        count_of_extra_aliens = len(extra_alien_list)
        expected_count_of_extra_aliens = 0
        self.assertEqual(expected_count_of_extra_aliens, count_of_extra_aliens)


if __name__ == '__main__':
    unittest.main()
