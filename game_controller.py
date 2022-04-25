from player import Player
from obstacles import Obstacles


class GameController:
    def __init__(self, screen_width, screen_height):
        self.running = True
        self.player = Player((screen_width / 2, screen_height), screen_width)
        self.obstacles = Obstacles(screen_width)

    def run(self):
        if self.running:
            self.player.update()

