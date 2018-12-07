import settings as st
class Moving:
    def __init__(self, max):
        self.max = max
        self.nexts = list()

    def get_nexts(self):
        x, y = st.index(*self.rect.topleft)
        nexts = list()
        nexts.append((x+1, y))
        nexts.append((x-1, y))
        nexts.append((x, y+1))
        nexts.append((x, y-1))
        self.nexts = nexts
        return nexts

    def move(self, pos):
        if pos in self.nexts:
            pos = st.pixel(*pos)
            self.rect.topleft = pos
