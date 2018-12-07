import pygame

import settings as st

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/obstacle.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = st.pixel(x, y)
        self.pos = x, y
