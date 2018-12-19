import pygame
import settings as st

from loop.flags import Flags
from loop.std import Std

from map import Map
from position import Pos
import settings as st
from player import Player

class Loop(Std):
    def __init__(self, id_map):
        self.map = Map(id_map)
        self.flags = Flags(turn=1)
        Std.__init__(self)
        self.turn = 1

    def select(self, mouse_pos):
        pos = Pos(mouse_pos, is_pixel=True)
        sprite = self.map.get_sprite(pos)
        if sprite:
            self.flags.select(sprite)
        else: self.flags.deselect()

    def confirm(self, mouse_pos):
        pos = Pos(mouse_pos, is_pixel=True)
        self.flags.confirm(pos)

    def switch_turn(self):
        print(len(Player.TEAMS))
        self.flags.switch_turn(len(Player.TEAMS))
        for p in self.map.players:
            p.exhaust = False
            p.unloaded = False
