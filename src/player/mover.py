from position import Pos

class Mover:
    def __init__(self):
        self.exhaust = False    # has motion
        self.unloaded = False   # has attack

    def around(self, x, y, d):
        print("around", x, y)
        if not d: return
        nexts = list()
        nexts.append((x+1, y))
        nexts.append((x-1, y))
        nexts.append((x, y+1))
        nexts.append((x, y-1))
        for x, y in nexts:
            pos = Pos((x,y))
            if self.map.empty(pos):
                if not pos in self.nexts:
                    self.nexts.append(pos)
                self.around(*pos.index(), d-1)

    def calculate(self):
        # motion
        self.nexts = list()
        speed = self.stats.speed.value
        x, y = self.pos.index()
        self.around(x, y, speed)

        # attack
        self.risks = list()
        range = self.stats.range.value
        topleft = self.pos + Pos((-range, -range))
        bottomdown = self.pos + Pos((range, range))
        ss = self.map.get_sprites(topleft, bottomdown)
        for s in ss:
            self.risks.append(s.pos)

    def move(self, dx, dy):
        next_pos = Pos((dx,dy))
        if not self.exhaust and next_pos in self.nexts:
            self.pos = next_pos
            self.calculate()
            self.exhaust = True
