import os
import json
import pygame
import settings as st
import colors as cl

class Images:
    def __init__(self, code):
        image, json = self.load()
        r = json[code]
        x = r["x"]
        y = r["y"]
        self.image = pygame.Surface(st.TILES)
        quad = (x*st.TILE,y*st.TILE,st.TILE,st.TILE)
        self.image.blit(image, (0,0), quad)
        self.image.set_colorkey(cl.BLACK)

    def load(self):
        path = os.path.dirname(__file__)
        img = os.path.join(path, "images", "players.png")
        dataset = os.path.join(path, "images", "players.json")
        return pygame.image.load(img), json.load(open(dataset, "r"))
