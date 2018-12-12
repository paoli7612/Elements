from player.sprite import Sprite
from player.stats import Stats
from player.mover import Mover
from player.tracer import Tracer

import settings as st
import json, os

class Player(Sprite, Mover, Tracer):
    TOT_TEAM = 0
    TEAMS = set()
    def __init__(self, map, pos, id, team):
        self.map = map
        self.team = team
        Player.TEAMS.add(team)
        self.pos = pos
        self.load_stats(id)
        Mover.__init__(self)
        Tracer.__init__(self)
        Sprite.__init__(self)

    def load_stats(self, id):
        filename = "players.json"
        path = os.path.dirname(__file__)
        path_json = os.path.join(path, filename)
        file = open(path_json, "r")
        dict = json.load(file)
        p = dict[str(id)]
        self.stats = Stats(p["stats"])
        self.name = p["name"]
        self.id = id
