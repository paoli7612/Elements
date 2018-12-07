from player.sprite import Sprite
from player.moving import Moving
import settings as st

class Player(Sprite, Moving):
    def __init__(self, map, pos, code):
        Sprite.__init__(self, pos, code)
        Moving.__init__(self, 3)
        self.map = map
        self.code = code
