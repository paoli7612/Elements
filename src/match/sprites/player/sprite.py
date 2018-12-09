import pygame
from match.sprites.player.images import Images
import settings as st
import colors as cl

class Sprite(pygame.sprite.Sprite, Images):
    def __init__(self, pos, code):
        self.pos = pos
        pygame.sprite.Sprite.__init__(self)
        Images.__init__(self, code)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos.pixel()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
