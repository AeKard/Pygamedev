import pygame
from setting import *

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,group):
        super().__init__(group)
        self.image = pygame.transform.scale(pygame.image.load('walls/wall_corner_front_right.png').convert_alpha(),(32 * 2, 32*2))
        
        self.rect = self.image.get_rect(topleft = pos)
        print(self.rect)
    # def transform(self):
    #     self.image = pygame.transform.scale(self.image,(60,120))
class Floor(pygame.sprite.Sprite):
    def __init__(self,pos,group):
        super().__init__(group)
        self.image = pygame.transform.scale(pygame.image.load('floor/floor_1.png').convert_alpha(),(32 *2, 32*2))
        self.rect = self.image.get_rect(topleft = pos)
        # print(self.image)
        