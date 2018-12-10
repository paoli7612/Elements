from images import by_name
from info import Info

class Flags:
    def __init__(self):
        self.image_select = by_name("selected")
        self.info = Info()

        self.is_select = False
        self.sprite_select = None

        self.is_info = False

    def select(self, sprite):
        self.sprite_select = sprite
        self.is_select = True
        self.info.set_sprite(sprite)

    def deselect(self):
        self.sprite_select = None
        self.is_select = False
        self.info.clear()


    def draw(self, screen):
        if self.is_select:
            screen.blit(self.image_select, self.sprite_select.pos.pixel())
        self.info.draw(screen)
