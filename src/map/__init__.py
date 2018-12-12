import pygame
import settings as st
import colors as cl
from position import Pos, MARGIN
from map.sprites import Sprites
from map.loader import Loader

class Map(Sprites, Loader):
    def __init__(self, id):
        Sprites.__init__(self)
        Loader.__init__(self, id)
        self.screen = pygame.Surface(st.SIZE)
        self.screen.fill(cl.GREY)
        for x in range(0, st.WIDTH, st.TILE):
            pygame.draw.line(self.screen, cl.BLACK, (x, 0), (x, st.HEIGHT))
        for y in range(0, st.HEIGHT, st.TILE):
            pygame.draw.line(self.screen, cl.BLACK, (0,y), (st.WIDTH, y))

    def draw(self, screen):
        screen.blit(self.screen, (0,0))
        for sprite in self.players:
            sprite.draw(screen)

    def empty(self, pos):
        if not pos < MARGIN:
            return False
        sprite = self.get_sprite(pos)
        return sprite == None

    def get_sprite(self, pos):
        for sprite in self.players:
            if sprite.pos == pos:
                return sprite

    def get_sprites(self, min, max):
        sprites = list()
        yy = range(min.y, max.y+1)
        xx = range(min.x, max.x+1)
        for y in yy:
            for x in xx:
                s = self.get_sprite(Pos((x,y)))
                if s:
                    sprites.append(s.pos)
        return sprites
