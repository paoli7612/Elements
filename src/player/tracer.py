from position import Pos

class Tracer:
    def __init__(self):
        self.unloaded = False

    def find_enemy(self, pos):
        r = self.stats.range.value
        a = pos + Pos((-r, -r))
        b = pos + Pos((r, r))

        ss = self.map.get_sprites(a, b)
        self.risks += ss
