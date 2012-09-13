import pygame
from pygame.locals import *

class Paddle(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self, self.containers)
        self.rect = self.image.get_rect()
        self.rect.bottom = self.arena.rect.bottom - self.arena.tileside

    def update(self):
        self.rect.centerx = pygame.mouse.get_pos()[0]
        self.rect.clamp_ip(self.arena.rect)