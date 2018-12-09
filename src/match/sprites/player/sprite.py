import pygame
from match.sprites.player.images import Images
import settings as st
import colors as cl

class Sprite(pygame.sprite.Sprite, Images):
    def __init__(self, pos, code):
        self.team_image = pygame.Surface(st.TILES)
        self.team_image.fill(cl.TEAMS[self.team])
        self.pos = pos
        pygame.sprite.Sprite.__init__(self)
        Images.__init__(self, code)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos.pixel()
        self.selected = False
        self.selected_image = pygame.image.load("images/selected.png")

    def draw(self, screen):
        if self.selected:
            screen.blit(self.selected_image, self.rect)
        else:
            screen.blit(self.team_image, self.rect)
        screen.blit(self.image, self.rect)

    def update(self):
        pass
