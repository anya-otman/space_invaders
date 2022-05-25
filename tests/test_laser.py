import unittest
import pygame
import math
from game.laser import Laser
from game.player import Player
from math import pi


class LaserTestCase(unittest.TestCase):
    def test_update_with_straight_trajectory(self):
        angle = pi/2
        player = Player((600 / 2, 600), 600, 3)
        laser = Laser(player.rect.center, -5, angle, 600)
        laser.update()

        my_laser = Laser(player.rect.center, -5, angle, 600)
        my_laser.rect.x += -5*math.cos(angle)
        my_laser.rect.y += -5*math.sin(angle)

        laser_coordinates = (laser.rect.x, laser.rect.y)
        expected_laser_coordinates = (my_laser.rect.x, my_laser.rect.y)
        self.assertEqual(expected_laser_coordinates, laser_coordinates)

    def test_update_with_angular_trajectory_positive_angle(self):
        angle = pi / 4
        player = Player((600 / 2, 600), 600, 3)
        laser = Laser(player.rect.center, -5, angle, 600)
        laser.update()

        my_laser = Laser(player.rect.center, -5, angle, 600)
        my_laser.rect.x += -5 * math.cos(angle)
        my_laser.rect.y += -5 * math.sin(angle)

        laser_coordinates = (laser.rect.x, laser.rect.y)
        expected_laser_coordinates = (my_laser.rect.x, my_laser.rect.y)
        self.assertEqual(expected_laser_coordinates, laser_coordinates)

    def test_update_with_angular_trajectory_negative_angle(self):
        angle = -pi / 4
        player = Player((600 / 2, 600), 600, 3)
        laser = Laser(player.rect.center, -5, angle, 600)
        laser.update()

        my_laser = Laser(player.rect.center, -5, angle, 600)
        my_laser.rect.x += -5 * math.cos(angle)
        my_laser.rect.y += -5 * math.sin(angle)

        laser_coordinates = (laser.rect.x, laser.rect.y)
        expected_laser_coordinates = (my_laser.rect.x, my_laser.rect.y)
        self.assertEqual(expected_laser_coordinates, laser_coordinates)

    def test_change_direction_after_several_calls_update_sharp_corner(self):
        angle = pi / 4
        player = Player((600 / 2, 600), 600, 3)
        laser = Laser(player.rect.center, -5, angle, 600)

        for i in range(200):
            laser.update()

        laser_angle = laser.angle
        expected_laser_angle = angle + pi / 2
        self.assertEqual(expected_laser_angle, laser_angle)

    def test_change_direction_after_several_calls_update_obtuse_corner(self):
        angle = 3*pi/4
        player = Player((600 / 2, 600), 600, 3)
        laser = Laser(player.rect.center, -5, angle, 600)

        for i in range(200):
            laser.update()

        laser_angle = laser.angle
        expected_laser_angle = angle - pi / 2
        self.assertEqual(expected_laser_angle, laser_angle)

    def test_destroy_movement_in_a_negative_direction(self):
        laser = Laser((0, 0), -5, pi/2, 600)
        lasers = pygame.sprite.Group()
        lasers.add(laser)
        self.assertEqual(len(lasers.sprites()), 1)
        laser.update()
        self.assertEqual(len(lasers.sprites()), 0)

    def test_destroy_movement_in_a_positive_direction(self):
        laser = Laser((600, 0), 5, pi / 2, 600)
        lasers = pygame.sprite.Group()
        lasers.add(laser)
        self.assertEqual(len(lasers.sprites()), 1)
        laser.update()
        self.assertEqual(len(lasers.sprites()), 0)


if __name__ == '__main__':
    unittest.main()
