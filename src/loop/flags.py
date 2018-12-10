from images import by_name
from info import Info

class Flags:
    def __init__(self, turn):
        self.image_select = by_name("selected")
        self.image_motion = by_name("motion")
        self.info = Info()

        self.is_select = False
        self.sprite_select = None
        self.turn = turn
        self.is_info = False

    def select(self, sprite):
        self.sprite_select = sprite
        self.is_select = True
        self.info.set_sprite(sprite)

    def deselect(self):
        self.sprite_select = None
        self.is_select = False
        self.info.clear()

    def move(self, pos):
        if self.is_select and pos in self.sprite_select.nexts and self.sprite_select.team == self.turn:
            self.sprite_select.move(pos.x, pos.y)

    def switch_turn(self):
        self.turn %= 2
        self.turn += 1

    def draw(self, screen):
        if self.is_select:
            screen.blit(self.image_select, self.sprite_select.pos.pixel())
            for p in self.sprite_select.nexts:
                screen.blit(self.image_motion, p.pixel())
        self.info.draw(screen)
