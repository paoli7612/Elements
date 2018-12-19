from player.sprite import Sprite
from player.mover import Mover
from player.loader import Loader

import settings as st
import json, os

class Player(Sprite, Mover, Loader):
    TEAMS = set()
    def __init__(self, map, pos, id, team):
        self.map = map
        self.pos = pos
        self.id = id
        self.team = team
        Player.TEAMS.add(team)

        Loader.__init__(self)
        Mover.__init__(self)
        Sprite.__init__(self)
