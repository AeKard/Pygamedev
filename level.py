import pygame
from setting import *
from player import Player
from tile import Tile

class level:
    def __init__(self):
        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # sprite Group
        self.player_sprite = pygame.sprite.Group() # groups the player
        self.visible_sprite = pygame.sprite.Group()
        self.obstacle_sprite = pygame.sprite.Group()
        
        self.setup() # calls the function setup in init
        
        #sprite setup
        self.create_map()
        # SPRITE
    def create_map(self):
        for row_index,row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                if col == 'x':
                    Tile((x,y),[self.visible_sprite]) # POSITION GROUP
                if col == 'p':
                    Player((x,y),[self.player_sprite])


    def setup(self):
        self.player = Player((640,360), self.player_sprite) # Gets the player pos and group
 
    def run(self, dt):
        self.display_surface.fill('white') # fill the display surface
        self.visible_sprite.draw(self.display_surface)
        self.player_sprite.draw(self.display_surface) # draw the sprite in display surface
        self.player_sprite.update(dt) # update the sprite and calls all children