from player.sprite import Sprite

class Player(Sprite):
    def __init__(self, pos, code):
        Sprite.__init__(self, pos)
        self.code = code
