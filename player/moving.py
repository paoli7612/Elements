import settings as st
class Moving:
    def __init__(self, max):
        self.max = max

    def around(self, pos, max):
        if max:
            x, y = pos
            l = list()
            l.append((x+1, y))
            l.append((x-1, y))
            l.append((x, y+1))
            l.append((x, y-1))
            self.nexts+=l
            for n in l:
                self.around(n, max-1)

    def get_nexts(self):
        self.nexts = list()
        pos = st.index(*self.rect.topleft)
        self.around(pos, self.max)
        self.nexts = list(set(self.nexts))
        self.nexts.remove(pos)
        return self.nexts

    def move(self, pos):
        if pos in self.nexts:
            pos = st.pixel(*pos)
            self.rect.topleft = pos
