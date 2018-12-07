import os
import pygame
import settings as st
import colors as cl

class Images:
    def __init__(self, x, y):
        image = self.load()
        self.image = pygame.Surface(st.TILES)
        quad = (x*st.TILE,y*st.TILE,st.TILE,st.TILE)
        self.image.blit(image, (0,0), quad)
        self.image.set_colorkey(cl.BLACK)

    def load(self):
        path = os.path.dirname(__file__)
        img = os.path.join(path, "images", "players.png")
        return pygame.image.load(img)
