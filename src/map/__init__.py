import pygame
import settings as st
import colors as cl
from map.sprites import Sprites

class Map(Sprites):
    def __init__(self):
        Sprites.__init__(self)
        self.light_image = pygame.image.load("images/light.png")
        self.screen = pygame.Surface(st.SIZE)
        self.screen.fill(cl.GREY)
        for x in range(0, st.WIDTH, st.TILE):
            pygame.draw.line(self.screen, cl.BLACK, (x, 0), (x, st.HEIGHT))
        for y in range(0, st.HEIGHT, st.TILE):
            pygame.draw.line(self.screen, cl.BLACK, (0,y), (st.WIDTH, y))

    def light(self, screen, pos):
        try:
            screen.blit(self.light_image, pos.pixel())
        except: print("no")

    def draw(self, screen):
        screen.blit(self.screen, (0,0))
        for sprite in self.players:
            sprite.draw(screen)

    def empty(self, pos):
        sprite = self.get_sprite(pos)
        return sprite == None

    def get_sprite(self, pos):
        for sprite in self.players:
            if sprite.pos == pos:
                return sprite
