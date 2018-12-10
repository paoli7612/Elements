from position import Pos

class Mover:
    def __init__(self):
        self.nexts = list()
        self.calculate()

    def around(self, pos, d):
        if not d: return
        if self.map.empty(pos):
            nexts = list()
            nexts.append(Pos((pos.x+1, pos.y)))
            nexts.append(Pos((pos.x-1, pos.y)))
            nexts.append(Pos((pos.x, pos.y+1)))
            nexts.append(Pos((pos.x, pos.y-1)))
            for n in nexts:
                self.nexts += nexts
                self.around(n, d-1)

    def calculate(self):
        self.around(self.pos, self.stats.speed.value)
        self.nexts = list(set(self.nexts))

    def move(self, dx, dy):
        if self.speed:
            next_pos = Pos((dx,dy)) + self.player.pos
            if next_pos in self.nexts:
                self.nexts = list()
                self.player.pos.add(dx,dy)
                self.speed -= 1
                self.around(next_pos, self.speed)
                self.calculate()

    def draw(self, screen):
        for p in self.nexts:
            self.map.light(screen, p)
