import settings as st

class Pos:
    def __init__(self, pos):
        x, y = pos
        self.x = x
        self.y = y

    def pixel(self):
        x = self.x * st.TILE
        y = self.y * st.TILE
        return x, y

    def index(self):
        x = self.x
        y = self.y
        return x, y

    def __neg__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        p = Pos(x, y)
        return p
