import pygame
import settings as st
import colors as cl
from position import Pos

class Font:
    def __init__(self, image):
        self.font_name = pygame.font.match_font("arial")
        self.image = image

    def write(self, text, size, pos, color):
        font = pygame.font.Font(self.font_name, size)
        image = font.render(text, True, color)
        rect = image.get_rect()
        rect.topleft = pos
        self.image.blit(image, rect)
