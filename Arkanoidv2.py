#
# scriptedfun.com
#
# Screencast #2
# Arinoid - Using Sprite Sheets and Drawing the Background
#
#
import os, pygame
from pygame.locals import *
from Arkinoid.engine import Arena
from engine.Spritesheet import Spritesheet
from engine.Paddle import Paddle


SCREENRECT = Rect(0, 0, 640, 480) # Create a REct object the size of the display

def paddleimage(spritesheet):
    paddle = pygame.Surface((55, 11)).convert()
    # left half
    paddle.blit(spritesheet.imgat((261, 143, 27, 11)), (0, 0))
    # right half
    paddle.blit(spritesheet.imgat((289, 143, 28, 11)), (27, 0))
    paddle.set_colorkey(paddle.get_at((0, 0)), RLEACCEL)
    return paddle

def main():
    pygame.init()

    screen = pygame.display.set_mode(SCREENRECT.size)

    spritesheet = Spritesheet('arinoid_master.bmp')

    Arena.tiles = spritesheet.imgsat([(129, 321, 31, 31),   # purple - 0
                                      (161, 321, 31, 31),   # dark blue - 1
                                      (129, 353, 31, 31),   # red - 2
                                      (161, 353, 31, 31),   # green - 3
                                      (129, 385, 31, 31)])  # blue - 4

    Paddle.image = paddleimage(spritesheet)

    # make background
    arena = Arena()
    arena.makebg(2) # you may change the background color here
    screen.blit(arena.background, (0, 0))
    pygame.display.update()


    Paddle.arena = arena

    # keep track of sprites
    all = pygame.sprite.RenderUpdates()

    Paddle.containers = all

    # keep track of time
    clock = pygame.time.Clock()

    paddle = Paddle()


    # game loop
    while 1:

        # get input
        for event in pygame.event.get():
            if event.type == QUIT\
            or (event.type == KEYDOWN and\
                event.key == K_ESCAPE):
                return

        # clear sprites
        all.clear(screen, arena.background)

        # update sprites
        all.update()

        # redraw sprites
        dirty = all.draw(screen)
        pygame.display.update(dirty)

        # maintain frame rate
        clock.tick(30)

if __name__ == '__main__': main()