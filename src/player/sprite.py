import pygame
from player.images import Images
import settings as st
import colors as cl

class Sprite(pygame.sprite.Sprite, Images):
    def __init__(self, pos, code):
        self.pos = pos
        pos = st.pixel(*pos)
        pygame.sprite.Sprite.__init__(self)
        Images.__init__(self, code)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

    def update(self):
        if self.is_moving:
            self.rect.left += -2*self.dx
            if self.dx > 0: self.dir = "left"
            else: self.dir = "right"
            xf, yf = st.pixel(*self.next_pos)
            ax = xf == self.rect.left
            ay = yf == self.rect.top
            if ax:
                self.dx = 0
                self.rect.top += -2*self.dy
                if self.dy > 0: self.dir = "up"
                else: self.dir = "down"
            if ay: self.dy = 0
            if ax and ay:
                self.is_moving = False
                self.pos = self.next_pos

            self.image = self.images[self.dir]["stand"]
        else:
            self.rect.topleft = st.pixel(*self.pos)
