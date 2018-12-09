import pygame
import settings as st

class Loop:
    def __init__(self):
        self.screen = pygame.display.set_mode(st.SIZE)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(st.TITLE)

    def start(self):
        self.running = True
        while self.running:
            self.clock.tick(st.FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.change_flag(event.pos, "select")
                elif event.button == 3:
                    self.change_flag(event.pos, "show_info")

    def update(self):
        self.map.sprites.update()
        self.cursor.update()

    def draw(self):
        self.map.draw(self.screen)
        self.cursor.draw(self.screen)
        if self.flags["show_info"]:
            self.flags["show_info"].info.draw(self.screen)
        pygame.display.flip()
