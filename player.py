import pygame
from support import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups,obstacle_sprite, create_attack, destroy_attack): # NEED TO KNOW WHERE OBSTACLE IS SO USE OBSTACLE 
        super().__init__(groups)
        # Initializa the player
        # self.player = pygame.image.load('player/knight_m_idle_anim_f0').convert_alpha()
    
        # call support and for animation
        self.import_assets()
        self.status = 'right'
        self.frame_index = 0
        # character general setup
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.character_scaled().get_rect(center = pos)
        # print(self.rect)
        #orientation
        self.orientation_x = False
        self.orientation_y = False
        #movement attribute
        self.direction = pygame.math.Vector2()
        self.orient = 'right'
        self.speed = 5
        #obstacle
        self.obstacle_sprite = obstacle_sprite
        # Weapon
        self.attacking = False
        self.create_attack = create_attack
        self.destroy_attack = destroy_attack
        self.attack_cooldown = 400
    
        # character health
        self.health = 100

    def import_assets(self):
        self.animations = { 'hit': [],
         'right_idle': [], 
         'left_idle': [], 
         'right_run':[], 
         'left_run': [], 
         'right': []}
         
        for animation in self.animations.keys():
            full_path = 'player/' + animation
            self.animations[animation] = import_folder(full_path)

    def character_scaled(self):
        self.image = pygame.transform.scale(self.image,(16*3,22*3))
        return self.image
    
    def animate(self, dt):
        self.frame_index += 4 * dt
        # print(self.status)
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0
        self.image = pygame.transform.scale(self.animations[self.status][int(self.frame_index)],(16*3,22*3))
    def input(self):
        if not self.attacking:
            keys = pygame.key.get_pressed()
            # Directionmovement
            if keys[pygame.K_UP]:
                self.direction.y = -1
                self.status = 'right_run'
                self.orientation_y = True
                self.orient = 'up'
            elif keys[pygame.K_DOWN]:
                self.direction.y = 1
                self.status = 'left_run'
                self.orientation_y = True
                self.orient = 'down'
            else:
                self.direction.y = 0
                self.orientation_y = False

            if keys[pygame.K_RIGHT]:
                self.direction.x = 1
                self.orientation_x = False
                self.status = 'right_run'
                self.orient = 'right'

            elif keys[pygame.K_LEFT]:
                self.direction.x = -1
                self.orientation_x = True
                self.status = 'left_run'
                self.orient = 'left'
            else:
                if self.orientation_x == True and self.orientation_y != True:
                    self.status = 'left_idle'
                elif self.orientation_x == False and self.orientation_y != True:
                    self.status = 'right_idle'
                
                self.direction.x = 0
            
            if keys[pygame.K_SPACE]:
                self.attacking = True
                self.attack_time = pygame.time.get_ticks()
                self.create_attack()
        else:
            self.direction.y = 0
            self.direction.x = 0
            if self.direction == 'right':
                self.status = 'right_idle'
            else:
                self.direction == 'left'
    def move(self, speed):
        # self.rect.center += self.direction * speed
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        # horizontal movement
        self.rect.x += self.direction.x * speed
        self.collision('horizontal')
        # vertical
        self.rect.y += self.direction.y * speed
        self.collision('vertical')

    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprite:
                if sprite.rect.colliderect(self.rect): #sprite.rect.colide is the obstacle sprite #self.rect is the player 
                    if self.direction.x > 0: # moving right
                        self.rect.right = sprite.rect.left # right = to left
                    if self.direction.x < 0:
                        self.rect.left = sprite.rect.right # moving left
                

        if direction == 'vertical':
            for sprite in self.obstacle_sprite:
                if sprite.rect.colliderect(self.rect): #sprite.rect.colide is the obstacle sprite #self.rect is the player 
                    if self.direction.y > 0: # moving right
                        self.rect.bottom = sprite.rect.top # moving down
                    if self.direction.y < 0:
                        self.rect.top = sprite.rect.bottom # moving up

    def cooldown(self):
        current_time = pygame.time.get_ticks()

        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.attacking = False
                self.destroy_attack()
    def update(self,dt):
        self.input()
        self.cooldown()
        self.move(self.speed)
        self.animate(dt)

