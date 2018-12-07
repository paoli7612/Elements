from player.sprite import Sprite
from player.moving import Moving
import settings as st

class Player(Sprite, Moving):
    def __init__(self, pos, code):
        Sprite.__init__(self, pos, code)
        Moving.__init__(self, 1)
        self.code = code
