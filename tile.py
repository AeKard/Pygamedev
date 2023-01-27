import pygame
from setting import *

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,group):
        super().__init__(group)
        self.image = pygame.image.load('walls/wall_corner_front_right.png').convert_alpha()
        self.image_scale = pygame.transform.scale2x(self.image)
        self.rect  = self.image.get_rect(topleft = pos)
        self.transform()
    
    def transform(self):
        self.image = pygame.transform.scale(self.image,(70,100))
