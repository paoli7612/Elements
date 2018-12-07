import os
import json
import pygame
import settings as st
import colors as cl

class Images:
    def __init__(self, code):
        self.big_image, json = self.load()
        r = json[code]
        x = r["x"]
        y = r["y"]
        self.images = dict()
        self.images["down"] = dict()
        self.images["down"]["stand"] = self.get_frame(x+1,y)
        self.images["down"]["walk"] = self.get_frame(x,y)
        self.images["up"] = dict()
        self.images["up"]["stand"] = self.get_frame(x+1,y+3)
        self.images["up"]["walk"] = self.get_frame(x,y+3)
        self.images["right"] = dict()
        self.images["right"]["stand"] = self.get_frame(x+1,y+2)
        self.images["right"]["walk"] = self.get_frame(x,y+2)
        self.images["left"] = dict()
        self.images["left"]["stand"] = self.get_frame(x+1,y+1)
        self.images["left"]["walk"] = self.get_frame(x,y+1)
        self.dir = "down"
        self.image = self.images[self.dir]["stand"]

    def get_frame(self, x, y):
        image = pygame.Surface(st.TILES)
        quad = (x*st.TILE,y*st.TILE,st.TILE,st.TILE)
        print(quad)
        image.blit(self.big_image, (0,0), quad)
        image.set_colorkey(cl.BLACK)
        return image

    def load(self):
        path = os.path.dirname(__file__)
        img = os.path.join(path, "images", "players.png")
        dataset = os.path.join(path, "images", "players.json")
        return pygame.image.load(img), json.load(open(dataset, "r"))
