import unittest
from game.alien import Alien


class AlienTestCase(unittest.TestCase):
    def test_update_with_positive_direction(self):
        alien = Alien(0, 0)
        alien.update(1)

        alien_x = alien.rect.x
        expected_alien_x = Alien(1, 0).rect.x
        self.assertEqual(expected_alien_x, alien_x)

    def test_update_with_negative_direction(self):
        alien = Alien(0, 0)
        alien.update(-1)

        alien_x = alien.rect.x
        expected_alien_x = Alien(-1, 0).rect.x
        self.assertEqual(expected_alien_x, alien_x)

    def test_update_with_several_directions(self):
        alien = Alien(0, 0)
        alien.update(-1)
        alien.update(-2)
        alien.update(5)

        alien_x = alien.rect.x
        expected_alien_x = Alien(2, 0).rect.x
        self.assertEqual(expected_alien_x, alien_x)


if __name__ == '__main__':
    unittest.main()
