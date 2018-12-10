import pygame
import settings as st
import colors as cl

class Info:
    def __init__(self, player):
        self.player = player
        self.font_name = pygame.font.match_font("comicsansms")
        self.image = pygame.Surface(st.INFO_SIZE)
        self.rect = self.image.get_rect()

        self.made_screen()

    def write(self, text, size, pos, color):
        font = pygame.font.Font(self.font_name, size)
        image = font.render(text, True, color)
        rect = image.get_rect()
        rect.topleft = pos
        self.image.blit(image, rect)

    def made_screen(self):
        self.image.fill(cl.BLACK)
        p = pygame.Surface((st.INFO_WIDTH-st.INFO_MARGIN, st.INFO_HEIGHT-st.INFO_MARGIN))
        p.fill(cl.WHITE)
        self.image.blit(p, (st.INFO_MARGIN//2, st.INFO_MARGIN//2))

        self.write("Vita %s" %str(self.player.stats.life), st.TILE//2-4, (st.INFO_MARGIN,st.INFO_MARGIN), cl.RED)
        self.write("Mana %s" %str(self.player.stats.mana), st.TILE//2-4, (st.INFO_WIDTH/2,st.INFO_MARGIN), cl.BLUE)

        self.write("Attacco %s" %str(self.player.stats.attack), st.TILE//2-4, (st.INFO_MARGIN,st.INFO_MARGIN*4), cl.BLACK)
        self.write("Difesta %s" %str(self.player.stats.defense), st.TILE//2-4, (st.INFO_WIDTH/2,st.INFO_MARGIN*4), cl.BLACK)
        self.write("Velocita' %s" %str(self.player.stats.speed), st.TILE//2-4, (st.INFO_MARGIN,st.INFO_MARGIN*7), cl.BLACK)
        self.write("Gittata %s" %str(self.player.stats.range), st.TILE//2-4, (st.INFO_WIDTH/2,st.INFO_MARGIN*7), cl.BLACK)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        if self.player.pos.y < 4:
            self.rect.midtop = self.player.rect.midbottom
        else:
            self.rect.midbottom = self.player.rect.midtop
