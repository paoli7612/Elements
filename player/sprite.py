import pygame
from player.images import Images
import settings as st
import colors as cl

class Sprite(pygame.sprite.Sprite, Images):
    def __init__(self, pos, code):
        pos = st.pixel(*pos)
        pygame.sprite.Sprite.__init__(self)
        Images.__init__(self,1,0)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
