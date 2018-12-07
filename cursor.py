import pygame

import colors as cl
import settings as st

class Cursor:
    def __init__(self):
        self.image = pygame.Surface(st.TILES)
        pygame.draw.line(self.image, (cl.WHITE), (0,0), st.TILES,2)
        pygame.draw.line(self.image, (cl.WHITE), (0,st.TILE), (st.TILE, 0))
        self.image.set_colorkey(cl.BLACK)
        self.rect = self.image.get_rect()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        pos = pygame.mouse.get_pos()
        pos = st.index(*pos)
        pos = st.pixel(*pos)
        self.rect.topleft = pos
