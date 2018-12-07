import pygame
import settings as st
import colors as cl

class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos):
        pos = st.pixel(*pos)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(st.TILES)
        self.image.fill(cl.GREEN)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
