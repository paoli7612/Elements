import pygame
from player import Player

Group = pygame.sprite.Group

class Sprites:
    def __init__(self):
        self.players = Group()
        self.teams = dict()

    def new_player(self, pos, code, team):
        p = Player(self, pos, code, team)
        if team in self.teams:
            self.teams[team].add(p)
        else: self.teams[team] = Group()
        self.players.add(p)

    def update(self):
        for sprite in self.players:
            sprite.update()

    def deselect_all(self):
        for sprite in self.players:
            sprite.selected = False

    def deshow_all(self):
        for sprite in self.players:
            sprite.show_info = False
