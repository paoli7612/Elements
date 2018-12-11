import json, os
from position import Pos

class Loader:
    def __init__(self, id):
        file_name = str(id) + ".json"
        path = os.path.dirname(__file__)
        path_json = os.path.join(path, "data", file_name)
        file = open(path_json)
        dict = json.load(file)

        players = dict["players"]

        for t,team in enumerate(players):
            for player in team:
                self.parse_player(t+1, player) # 0->1


    def parse_player(self, team, element):
        id = element["id"]
        coord = element["coord"]
        pos = Pos(coord)
        self.new_player(pos, int(id), team)
