from match.sprites.player.sprite import Sprite
import settings as st

class Wall(Sprite):
    def __init__(self, pos, code):
        self.code = code
        Sprite.__init__(self, pos, code)
