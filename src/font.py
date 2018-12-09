import pygame
import settings as st
import colors as cl
from position import Pos

class Font:
    def __init__(self, pos):
        self.font_name = pygame.font.match_font("arial")
        self.pos = pos

    def write(self, text, size):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, cl.TEXT)
        rect = text_surface.get_rect()
        pos = Pos(self.pos.index())
        pos.x += 0.5
        rect.midbottom = pos.pixel()
        return text_surface, rect
