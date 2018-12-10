import pygame
from player import Player

Group = pygame.sprite.Group

class Sprites:
    def __init__(self):
        self.players = Group()

    def new_player(self, pos, code, team):
        p = Player(self, pos, code, team)
        self.players.add(p)

    def update(self):
        for sprite in self.players:
            sprite.update()
