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

    def add(self, dx, dy):
        self.x += dx
        self.y += dy

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        p = Pos((x, y))
        return p

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        p = Pos((x, y))
        return p

    def __eq__(self, other):
        ix = self.x == other.x
        iy = self.y == other.y
        return ix and iy

    def __hash__(self):
        return hash((self.x, self.y))

    def __gt__(self, other):
        return self.__lt__(other)

    def __lt__(self, other):
        ix = self.x < other.x
        iy = self.y < other.y
        return ix and iy

    def __str__(self):
        return "x:%s\ty:%s" %(self.x, self.y)

MARGIN = Pos(st.SIZE, True)
