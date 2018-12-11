import os
import pygame
import settings as st
import colors as cl

def get_img(name):
    path = os.path.dirname(__file__)
    img_path = os.path.join(path, name + ".png")
    img = pygame.image.load(img_path)
    return img

def by_code(id):
    img = get_img("players")

    x, y = st.PLAYER_COORDS[id]
    quad = (x*32, y*32, 32, 32)

    image = pygame.Surface((32,32))
    image.fill(cl.KEY)
    image.blit(img, (0,0), quad)
    image.set_colorkey(cl.KEY)
    image = pygame.transform.scale(image, (32*st.TILE//32, 32*st.TILE//32))
    return image

def by_name(name):
    img = get_img(name)
    img = pygame.transform.scale(img, (32*st.TILE//32, 32*st.TILE//32))
    return img
