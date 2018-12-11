TILE = 32
SIZE = WIDTH, HEIGHT = 25*TILE, 15*TILE
INFO_SIZE = INFO_WIDTH, INFO_HEIGHT = WIDTH, TILE*3
TILES = TILE, TILE
TITLE = "Elements - paoli7612"
FPS = 40

INFO_MARGIN = 10

PLAYER_COORDS = list()
for y in range(6):
    for x in range(8):
        PLAYER_COORDS.append((x,y))

PLAYER_NAMES = list()
for _ in PLAYER_COORDS:
    PLAYER_NAMES.append(str(_))
