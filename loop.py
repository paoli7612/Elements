import pygame
import settings as st
from map import Map
from player import Player
from cursor import Cursor

class Loop:
    def __init__(self):
        self.screen = pygame.display.set_mode(st.SIZE)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(st.TITLE)

        self.map = Map()
        self.cursor = Cursor()
        self.players = pygame.sprite.Group()


        p = Player((10,10),10)
        self.players.add(p)

        self.selected = p
        self.lights = p.get_nexts()

    def start(self):
        self.running = True
        while self.running:
            self.clock.tick(40)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            # KEYBOARD
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                pass
            # MOUSE
            if event.type ==pygame.MOUSEBUTTONDOWN:
                pos = st.index(*event.pos)
                self.selected.move(pos)
                self.lights = self.selected.get_nexts()

    def update(self):
        self.cursor.update()

    def draw(self):
        self.map.draw(self.screen)
        self.players.draw(self.screen)

        for l in self.lights:
            self.map.light(self.screen, l)

        self.cursor.draw(self.screen)
        pygame.display.flip()


if __name__ == "__main__":
    l = Loop()
    l.start()
