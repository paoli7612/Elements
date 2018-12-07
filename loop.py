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

        self.cursor = Cursor()
        self.players = pygame.sprite.Group()
        self.map = Map(self.players)

        self.round = 0
        self.new_player(2,2,"1")
        self.new_player(1,12,"2")
        self.new_player(21,4,"3")

    def new_player(self, x, y, code):
        p = Player(self.map,(x,y),code)
        self.players.add(p)

    def change_round(self):
        self.round = self.round%len(self.players)+1
        p = self.players.sprites()[self.round-1]
        self.selected = p
        self.lights = p.get_nexts()


    def start(self):
        self.running = True
        self.change_round()
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = st.index(*event.pos)
                if pos in self.lights and self.map.empty(pos):
                    self.selected.move(pos)
                    self.lights = self.selected.get_nexts()
                    self.change_round()

    def update(self):
        self.cursor.update()
        self.players.update()

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
