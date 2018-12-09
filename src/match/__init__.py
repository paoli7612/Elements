from match.map import Map
from match.loop import Loop

from position import Pos
import settings as st


FIRST = 1
SECOND = 2
PAUSE = 3

class Match(Loop):
    def __init__(self):
        Loop.__init__(self)
        self.map = Map()
        self.round = FIRST
        self.map.sprites.new_player(Pos((2,2)), "1")
        self.start()


    def change_round():
        self.round %= 2
        self.round += 1
