from match.map import Map
from match.loop import Loop
from match.cursor import Cursor

from position import Pos
import settings as st

MAX_TEAM = 2

class Match(Loop):
    def __init__(self):
        Loop.__init__(self)
        self.map = Map()
        self.map.sprites.new_player(Pos((2,2)), "1", team=1)
        self.map.sprites.new_player(Pos((3,4)), "2", team=1)
        self.map.sprites.new_player(Pos((6,7)), "3", team=2)
        self.map.sprites.new_player(Pos((9,10)), "4", team=2)
        self.cursor = Cursor()
        self.map.turn = 1
        self.start()

    def switch_turn(self):
        self.map.turn %= MAX_TEAM
        self.map.turn += 1

    def select(self, pos):
        pos = Pos(pos, is_pixel=True)
        sprite = self.map.get_sprite(pos)
        self.map.sprites.deselect_all()
        if sprite and sprite.team == self.map.turn:
            self.selected = sprite
            sprite.selected = True
