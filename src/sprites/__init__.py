import pygame
from player import Player

Group = pygame.sprite.Group

class Sprites:
    def __init__(self, map):
        self.players = Group()
        self.walls = Group()
        self.all = Group()
        self.teams = dict()
        self.map = map

    def new_player(self, pos, code, team):
        p = Player(self.map, pos, code, team)
        if team in self.teams:
            self.teams[team].add(p)
        else: self.teams[team] = Group()
        self.players.add(p)
        self.all.add(p)

    def new_wall(self, pos, code):
        w = Wall(pos, code)
        self.walls.add(w)
        self.all.add(w)

    def draw(self, screen):
        for sprite in self.all:
            sprite.draw(screen)

    def update(self):
        for sprite in self.all:
            sprite.update()

    def deselect_all(self):
        for sprite in self.all:
            sprite.selected = False
    def deshow_all(self):
        for sprite in self.all:
            sprite.show_info = False

    def __iter__(self):
        return self.all.__iter__()
