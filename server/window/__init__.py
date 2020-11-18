import pygame, time
SIZE = WIDTH, HEIGHT = 500, 500

class Window:
    def __init__(self):
        self.screen = pygame.display.set_mode(SIZE)
        pygame.display.set_caption('Elements')
        self.loop()

    def loop(self):
        while True:
            print("ok")
