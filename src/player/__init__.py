from player.sprite import Sprite
from player.stats import Stats
from player.mover import Mover

import settings as st

class Player(Sprite, Mover):
    TOT_TEAM = 0
    TEAMS = set()
    def __init__(self, map, pos, id, team):
        self.map = map
        self.id = id
        self.code = st.PLAYER_COORDS[id]
        self.name = st.PLAYER_NAMES[id]
        self.team = team
        Player.TEAMS.add(team)
        self.pos = pos
        self.stats = Stats()
        Mover.__init__(self)
        Sprite.__init__(self)
