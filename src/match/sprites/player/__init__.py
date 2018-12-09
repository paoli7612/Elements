from match.sprites.player.sprite import Sprite
import settings as st

class Player(Sprite):
    def __init__(self, map, pos, code):
        Sprite.__init__(self, pos, code)
        self.map = map
        self.code = code
        self.next_pos = pos
