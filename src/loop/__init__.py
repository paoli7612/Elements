import pygame
import settings as st

from loop.flags import Flags
from loop.std import Std

from map import Map
from position import Pos
import settings as st



class Loop(Std):
    def __init__(self):
        self.map = Map(1)
        self.flags = Flags(turn=1)
        Std.__init__(self)
        self.turn = 1

    def select(self, mouse_pos):
        pos = Pos(mouse_pos, is_pixel=True)
        sprite = self.map.get_sprite(pos)
        if sprite:
            self.flags.select(sprite)
        else: self.flags.deselect()

    def move(self, mouse_pos):
        pos = Pos(mouse_pos, is_pixel=True)
        self.flags.move(pos)

    def switch_turn(self):
        self.flags.switch_turn()
        for p in self.map.players:
            p.exhaust = False
