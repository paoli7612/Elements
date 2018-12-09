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
        self.map.sprites.new_player(Pos((3,6)), "2", team=2)
        self.cursor = Cursor()
        self.turn = 1
        self.start()

    def switch_turn(self):
        self.turn %= MAX_TEAM
        self.turn += 1

    def select(self, pos):
        pos = Pos(pos, is_pixel=True)
        sprite = self.map.get_sprite(pos)
        if sprite:
            self.selected = sprite
            self.map.sprites.deselect_all()
            sprite.selected = True
