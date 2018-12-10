import os
import pygame
import settings as st
import colors as cl

def get_image(code):
    path = os.path.dirname(__file__)
    img_path = os.path.join(path, "img", "players.png")
    img = pygame.image.load(img_path)

    x, y = code.split("/")
    x, y = int(x)*3+1, int(y)*4
    quad = (x*32, y*32, 32, 32)

    image = pygame.Surface((32,32))
    image.fill(cl.KEY)
    image.blit(img, (0,0), quad)
    image.set_colorkey(cl.KEY)
    image = pygame.transform.scale(image, (32*st.TILE//32, 32*st.TILE//32))
    return image
