import unittest
import pygame
from game.bonus import Bonus


class BonusTestCase(unittest.TestCase):
    def test_update(self):
        bonus = Bonus((0, 0), 1, 1)
        bonus.update()

        expected_coordinate_y = Bonus((0, 1), 1, 1).rect.y
        coordinate_y = bonus.rect.y
        self.assertEqual(expected_coordinate_y, coordinate_y)

    def test_destroy_when_bonus_still_on_the_screen(self):
        bonus = Bonus((0, 0), 1, 1)
        bonuses = pygame.sprite.Group()
        bonuses.add(bonus)
        self.assertEqual(len(bonuses.sprites()), 1)
        bonus.update()
        self.assertEqual(len(bonuses.sprites()), 1)

    def test_destroy_when_bonus_out_of_the_screen(self):
        bonus = Bonus((0, 610), 1, 1)
        bonuses = pygame.sprite.Group()
        bonuses.add(bonus)
        self.assertEqual(len(bonuses.sprites()), 1)
        bonus.update()
        self.assertEqual(len(bonuses.sprites()), 0)
