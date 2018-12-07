SIZE = WIDTH, HEIGHT = 600,600
TILE = 25
TILES = TILE, TILE
TITLE = "Elements - paoli7612"

def pixel(x, y):
    x = x*TILE
    y = y*TILE
    return x, y

def index(x, y):
    x = x//TILE
    y = y//TILE
    return x, y
