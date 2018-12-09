import pygame

import colors as cl
import settings as st
from position import Pos

class Cursor:
    def __init__(self):
        self.image = pygame.image.load("images/cursor.png")
        self.image.set_colorkey(cl.BLACK)
        self.rect = self.image.get_rect()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        pos = pygame.mouse.get_pos()
        pos = Pos(pos, is_pixel=True)
        self.rect.topleft = pos.pixel()
