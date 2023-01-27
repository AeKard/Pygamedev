import pygame
from support import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        # Initializa the player
        # self.player = pygame.image.load('player/knight_m_idle_anim_f0').convert_alpha()
    
        # call support and for animation
        self.import_assets()
        self.status = 'right'
        self.frame_index = 0
        # character general setup
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center = pos)
        #orientation
        self.orientation_x = False
        self.orientation_y = False
        #movement attribute
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200
    
    def import_assets(self):
        self.animations = { 'hit': [], 'right_idle': [], 'left_idle': [], 'right_run':[], 'left_run': [], 'right': []}
        
        for animation in self.animations.keys():
            full_path = 'player/' + animation
            self.animations[animation] = import_folder(full_path)

    def animate(self, dt):
        self.frame_index += 4 * dt
        # print(self.status)
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0
        self.image = pygame.transform.scale(self.animations[self.status][int(self.frame_index)],(50,100))
    
    def input(self):
        keys = pygame.key.get_pressed()

        # Directionmovement
        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.status = 'right_run'
            self.orientation_y = True
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.status = 'left_run'
            self.orientation_y = True
        else:
            self.orientation_y = False
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.orientation_x = False
            self.direction.x = 1
            self.status = 'right_run'

        elif keys[pygame.K_LEFT]:
            self.orientation_x = True
            self.direction.x = -1
            self.status = 'left_run'
        else:
            if self.orientation_x == True and self.orientation_y != True:
                self.status = 'left_idle'
            elif self.orientation_x == False and self.orientation_y != True:
                self.status = 'right_idle'
            self.direction.x = 0
    
    def move(self,dt):
        # Normalize vector
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

        # horizontal movement
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.x = self.pos.x
        # vertical
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.y = self.pos.y

    def update(self, dt):
        self.input()
        self.move(dt)
        self.animate(dt)

