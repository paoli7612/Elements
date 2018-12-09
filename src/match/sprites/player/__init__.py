from match.sprites.sprite import Sprite
from match.sprites.player.stats import Stats
from match.sprites.player.mover import Mover
import settings as st


class Player(Sprite):
    def __init__(self, map, pos, code, team):
        self.map = map
        self.code = code
        self.team = team
        self.speed = 2
        self.stats = Stats()
        Sprite.__init__(self, pos, code)
        self.mover = Mover(self)

    def move(self, dx=0, dy=0):
        if self.map.turn == self.team:
            self.mover.move(dx, dy)
