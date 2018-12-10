from position import Pos

class Mover:
    def __init__(self):
        self.nexts = list()
        self.exhaust = False
        self.calculate()

    def around(self, x, y, d):
        if not d: return
        if self.map.empty(Pos((x,y))):
            nexts = list()
            nexts.append((x+1, y))
            nexts.append((x-1, y))
            nexts.append((x, y+1))
            nexts.append((x, y-1))
            for x, y in nexts:
                self.nexts += nexts
                self.around(x, y, d-1)

    def calculate(self):
        x, y = self.pos.index()
        self.around(x, y, self.stats.speed.value)
        self.nexts = list(set(self.nexts))
        poss = list()
        for x,y in self.nexts:
            poss.append(Pos((x,y)))
        self.nexts = poss

    def move(self, dx, dy):
        next_pos = Pos((dx,dy))
        if not self.exhaust and next_pos in self.nexts:
            self.pos = next_pos
            self.exhaust = True

    def draw(self, screen):
        for p in self.nexts:
            self.map.light(screen, p)
