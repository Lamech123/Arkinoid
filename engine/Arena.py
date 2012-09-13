import pygame
from pygame.locals import *

SCREENRECT = Rect(0, 0, 640, 480)


class Arena:
    tileside = 31
    numxtiles = 12
    numytiles = 14
    topx = (SCREENRECT.width - SCREENRECT.width/tileside*tileside)/2
    topy = (SCREENRECT.height - SCREENRECT.height/tileside*tileside)/2
    rect = Rect(topx + tileside, topy + tileside, tileside*numxtiles, tileside*numytiles)

    # Class Constructor
    def __init__(self):
        self.background = pygame.Surface(SCREENRECT.size).convert()

    def drawtile(self, tile, x, y):
        self.background.blit(tile, (self.topx + self.tileside*x, self.topy + self.tileside*y))

    def makebg(self, tilenum):
        for x in range(self.numxtiles):
            for y in range(self.numytiles):
                self.drawtile(self.tiles[tilenum], x + 1, y + 1)