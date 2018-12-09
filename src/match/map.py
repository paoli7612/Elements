import pygame
import settings as st
import colors as cl
from match.sprites import Sprites

class Map:
    def __init__(self):
        self.sprites = Sprites(self)
        self.screen = pygame.Surface(st.SIZE)
        self.draw_grill()

    def draw_grill(self):
        self.screen.fill(cl.GREY)
        for x in range(0, st.WIDTH, st.TILE):
            pygame.draw.line(self.screen, cl.BLACK, (x, 0), (x, st.HEIGHT))
        for y in range(0, st.HEIGHT, st.TILE):
            pygame.draw.line(self.screen, cl.BLACK, (0,y), (st.WIDTH, y))

    def light(self, screen, pos):
        t = pygame.image.load("images/light.png")
        pos = st.pixel(*pos)
        screen.blit(t, pos)

    def draw(self, screen):
        screen.blit(self.screen, (0,0))
        self.sprites.draw(screen)

    def get_sprite(self, pos):
        for sprite in self.sprites:
            if sprite.pos == pos:
                return sprite 