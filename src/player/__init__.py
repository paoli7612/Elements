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
        Mover.__init__(self)
        Sprite.__init__(self)
