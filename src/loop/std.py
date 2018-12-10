import pygame
import settings as st

class Std:
    def __init__(self):
        self.screen = pygame.display.set_mode((st.WIDTH, st.HEIGHT + st.INFO_HEIGHT))
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
                    self.select(event.pos)

    def update(self):
        self.map.update()

    def draw(self):
        self.map.draw(self.screen)
        self.flags.draw(self.screen)
        pygame.display.flip()
