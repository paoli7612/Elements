import pygame
from match.sprites.player.images import Images
import settings as st
import colors as cl
from font import Font
from position import Pos

class Sprite(pygame.sprite.Sprite, Images):
    def __init__(self, pos, code, team=0):
        self.pos = pos
        self.font = Font(pos)
        pygame.sprite.Sprite.__init__(self)
        Images.__init__(self, code)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos.pixel()
        self.selected = False
        self.init_surfaces()

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
        if self.selected:
            screen.blit(self.selected_image, self.rect)
        screen.blit(self.team_image, self.rect)
        screen.blit(self.image, self.rect)
        if self.map.turn == self.team:
            s,r = self.font.write(str(self.speed),26)
            screen.blit(s, r)

    def update(self):
        pass