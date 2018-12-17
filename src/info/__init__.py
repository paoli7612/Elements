import pygame
import settings as st
import colors as cl
from position import Pos

class Info:
    def __init__(self):
        self.font_name = pygame.font.match_font("comicsansms")
        self.image = pygame.Surface(st.INFO_SIZE)
        self.rect = self.image.get_rect()
        self.rect.top = st.HEIGHT
        self.clear()

    def write(self, text, size, pos, color):
        pos = (Pos(pos) + Pos((0.5,0))).pixel()
        font = pygame.font.Font(self.font_name, size)
        image = font.render(text, True, color)
        rect = image.get_rect()
        rect.topleft = pos
        self.image.blit(image, rect)

    def clear(self):
        self.image.fill(cl.GREY)

    def set_sprite(self, sprite):
        self.clear()
        icon = pygame.Surface((st.TILE*3, st.TILE*3))
        icon.fill(cl.TEAMS[sprite.team])
        image_sprite = pygame.transform.scale(sprite.image, (st.TILE*2,st.TILE*2))
        icon.blit(image_sprite, (st.TILE//2,st.TILE//2))
        self.image.blit(icon, (0,0))

        self.write("%s" %str(sprite.name), st.TILE//2, (3,0), cl.WHITE)
        self.write("Vita %s" %str(sprite.stats.life), st.TILE//2, (11,0), cl.RED)
        self.write("Mana %s" %str(sprite.stats.mana), st.TILE//2, (16,0), cl.BLUE)
        self.write("TEAM %d" %sprite.team, st.TILE//2, (22,0), cl.TEAMS[sprite.team])

        self.write("Attacco %s" %str(sprite.stats.attack), st.TILE//2, (3,1), cl.BLACK)
        self.write("Difesta %s" %str(sprite.stats.defense), st.TILE//2, (9,1), cl.BLACK)
        self.write("Velocita' %s" %str(sprite.stats.speed), st.TILE//2, (3,2), cl.BLACK)
        self.write("Gittata %s" %str(sprite.stats.range), st.TILE//2, (9,2), cl.BLACK)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
