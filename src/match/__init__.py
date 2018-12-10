from map import Map
from loop import Loop

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
        self.map.turn = 1

        self.flags = {"select": False, "show_info": False}

        self.start()

    def switch_turn(self):
        self.map.turn %= MAX_TEAM
        self.map.turn += 1

    def change_flag(self, pos, flag):
        pos = Pos(pos, is_pixel=True)
        sprite = self.map.get_sprite(pos)
        try: self.flags[flag].change(flag, False)
        except: pass
        self.flags[flag] = False
        if sprite:
            self.flags[flag] = sprite
            sprite.change(flag, True)
