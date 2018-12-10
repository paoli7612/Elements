from player.sprite import Sprite
from player.stats import Stats
from player.mover import Mover

import settings as st

class Player(Sprite, Mover):
    def __init__(self, map, pos, name, team):
        self.map = map
        self.code = st.NAMES[name]
        self.name = name
        self.team = team
        self.pos = pos
        self.stats = Stats()
        Sprite.__init__(self)
        Mover.__init__(self)

    def move(self, dx=0, dy=0):
        if self.map.turn == self.team:
            self.mover.move(dx, dy)
