from position import Pos

class Mover:
    def __init__(self):
        self.exhaust = False
        self.unloaded = False

    def around(self, x, y, d):
        if not d: return
        nexts = list()
        nexts.append((x+1, y))
        nexts.append((x-1, y))
        nexts.append((x, y+1))
        nexts.append((x, y-1))
        for x, y in nexts:
            if self.map.empty(Pos((x,y))):
                self.nexts.append((x,y))
                self.around(x, y, d-1)


    def find_enemy(self, pos):
        r = self.stats.range.value
        a = pos + Pos((-r, -r))
        b = pos + Pos((r, r))

        ss = self.map.get_sprites(a, b)
        self.risks += ss

    def calculate(self):
        self.nexts = list()
        self.risks = list()
        x, y = self.pos.index()
        self.around(x, y, self.stats.speed.value)
        self.nexts = list(set(self.nexts))
        poss = list()
        for x,y in self.nexts:
            p = Pos((x,y))
            if self.map.empty(p):
                poss.append(p)
                self.find_enemy(p)
        self.nexts = poss
        self.risks = list(set(self.risks))
        self.risks.remove(self.pos)

    def move(self, dx, dy):
        next_pos = Pos((dx,dy))
        if not self.exhaust and next_pos in self.nexts:
            self.pos = next_pos
            self.calculate()
            self.exhaust = True

    def draw(self, screen):
        for p in self.nexts:
            self.map.light(screen, p)
