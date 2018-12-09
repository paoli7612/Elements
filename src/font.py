import pygame

class Font:
    def __init__(self):
        self.font_name = pygame.font.match_font("arial")

    def write(self, text, size, color):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        return text_surface
