import pygame

from images import by_code

from position import Pos
import settings as st
import colors as cl

class Sprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = by_code(self.id)
        self.rect = self.image.get_rect()
        self.init_surfaces()

    def init_surfaces(self):
        #Team
        self.team_image = pygame.Surface(st.TILES)
        self.team_image.set_colorkey(cl.BLACK)
        pygame.draw.circle(self.team_image, cl.TEAMS[self.team], (st.TILE//2,st.TILE//2), st.TILE//2)
        #exhaust
        self.exhaust_image = pygame.Surface(st.TILES)
        self.exhaust_image.set_colorkey(cl.BLACK)
        pygame.draw.circle(self.exhaust_image, cl.WHITE, (st.TILE//2,st.TILE//2), st.TILE//3*2)

    def draw(self, screen):
        if self.exhaust:
            screen.blit(self.exhaust_image, self.rect)
        screen.blit(self.team_image, self.rect)
        screen.blit(self.image, self.rect)


    def update(self):
        self.rect.topleft = self.pos.pixel()
