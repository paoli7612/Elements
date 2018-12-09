import settings as st

class Pos:
    def __init__(self, pos, is_pixel=False):
        x, y = pos
        if is_pixel:
            self.x = x // st.TILE
            self.y = y // st.TILE
        else:
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

    def __eq__(self, other):
        ix = self.x == other.x
        iy = self.y == other.y
        return ix and iy
