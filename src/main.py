import pygame

from loop import Loop

class Boss:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.loop = Loop(2)
        self.loop.start()

def main(argv):
    b = Boss()

if __name__ == "__main__":
    import sys
    main(sys.argv)
