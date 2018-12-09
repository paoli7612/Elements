from match.sprites.sprite import Sprite
from match.sprites.player.stats import Stats
import settings as st



class Player(Sprite):
    def __init__(self, map, pos, code, team):
        self.map = map
        self.code = code
        self.team = team
        self.speed = 2
        self.stats = Stats()
        Sprite.__init__(self, pos, code)
