import pygame
from font import Font
import settings as st
import colors as cl

class Info:
    def __init__(self, player):
        self.image = pygame.Surface(st.INFO_SIZE)
        self.image.fill(cl.WHITE)
        self.rect = self.image.get_rect()
        self.rect.midbottom = player.rect.midtop
        self.player = player
        self.font = Font(player.pos)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        pass
