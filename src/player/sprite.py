import pygame

from player.images import get_image

from position import Pos
import settings as st
import colors as cl

class Sprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = get_image(self.code)
        self.rect = self.image.get_rect()

    def init_surfaces(self):
        #Team
        self.team_image = pygame.Surface(st.TILES)
        self.team_image.set_colorkey(cl.BLACK)
        pygame.draw.circle(self.team_image, cl.TEAMS[self.team], (st.TILE//2,st.TILE//2), st.TILE//2)
        #Selected
        self.selected_image = pygame.Surface(st.TILES)
        self.selected_image.set_colorkey(cl.BLACK)
        pygame.draw.circle(self.selected_image, cl.WHITE, (st.TILE//2,st.TILE//2), st.TILE//3*2)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect.topleft = self.pos.pixel()
