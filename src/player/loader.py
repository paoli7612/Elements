import json, os
from player.stats import Stats

class Loader:
    def __init__(self):
        filename = "players.json"
        path = os.path.dirname(__file__)
        path_json = os.path.join(path, filename)
        file = open(path_json, "r")
        dict = json.load(file)
        p = dict[str(self.id)]
        self.stats = Stats(p["stats"])
        self.name = p["name"]
