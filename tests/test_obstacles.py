import unittest
from game.obstacles import Obstacles


class ObstaclesTestCase(unittest.TestCase):
    def test_create_multiple_obstacles(self):
        is_blocks_created = False
        obstacles = Obstacles(600)
        blocks = obstacles.blocks
        if blocks.sprites():
            is_blocks_created = True
        self.assertTrue(is_blocks_created)


if __name__ == '__main__':
    unittest.main()
