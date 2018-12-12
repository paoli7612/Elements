from images import by_name
from info import Info

class Flags:
    def __init__(self, turn):
        self.image_select = by_name("selected")
        self.image_danger = by_name("danger")
        self.image_green = by_name("green")
        self.image_red = by_name("red")
        self.info = Info()

        self.is_select = False
        self.sprite_select = None
        self.turn = turn
        self.is_info = False

    def select(self, sprite):
        self.sprite_select = sprite
        self.is_select = True
        self.info.set_sprite(sprite)
        sprite.calculate()

    def deselect(self):
        self.sprite_select = None
        self.is_select = False
        self.info.clear()

    def move(self, pos):
        if self.is_select and pos in self.sprite_select.nexts and self.sprite_select.team == self.turn:
            self.sprite_select.move(pos.x, pos.y)

    def switch_turn(self, tot_team):
        self.turn %= tot_team
        self.turn += 1

    def show_nexts(self, screen, sprite):
        if sprite.team == self.turn:
            image = self.image_green
        else:
            image = self.image_red
        for p in sprite.nexts:
            screen.blit(image, p.pixel())
        for p in sprite.risks:
            screen.blit(self.image_danger, p.pixel())

    def draw(self, screen):
        if self.is_select:
            screen.blit(self.image_select, self.sprite_select.pos.pixel())
            self.show_nexts(screen, self.sprite_select)
        self.info.draw(screen)
