import pygame
from match.sprites.player import Player

class Sprites:
    def __init__(self, map):
        self.players = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.sprites = pygame.sprite.Group()
        self.map = map

    def new_player(self, pos, code):
        p = Player(self.map, pos, code)
        self.players.add(p)
        self.sprites.add(p)

    def new_wall(self, pos, code):
        w = Wall(pos, code)
        self.walls.add(w)
        self.sprites.add(w)

    def draw(self, screen):
        for sprite in self.sprites:
            sprite.draw(screen)

    def update(self):
        for sprite in self.sprites:
            sprite.update()
