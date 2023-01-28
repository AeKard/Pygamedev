import pygame
from support import *
from entity import Entity
from setting import *

class Enemy(Entity):
    def __init__(self,monster_name,pos,groups, obstacle_sprites):
        super().__init__(groups)
        # general setup
        self.sprite_type = 'enemy'
        self.attacking = False
        # Graphic
        self.import_graphics(monster_name)
        self.status = 'idle'
        self.status2 = 'idle'
        self.image = self.animations[self.status][self.frame_index]
        
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-10)
        # movement 

        self.obstacle_sprites = obstacle_sprites
    
        #stats
        self.monster_name = monster_name
        monster_info = monster_data[self.monster_name]
        self.monster_health = monster_info['health']
        self.monster_damage = monster_info['damage'] 
        self.monster_attack_type = monster_info['attack_type'] 
        self.monster_resistance = monster_info['resistance'] 
        self.monster_speed = monster_info['speed'] 
        self.monster_attack_radius = monster_info['attack_radius'] 
        self.monster_notice_radius = monster_info['notice_radius'] 
        
    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0
        
        self.image = self.animations[self.status][int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)

    def import_graphics(self, name):
        self.animations = {'idle': [], 'move': []}
        main_path = f'enemy/{name}/'
        for animation in self.animations.keys():
            self.animations[animation] = import_folder(main_path + animation)
    

    # distance and direction
    def get_player_distance_direction(self, player):
        enemy_vec = pygame.math.Vector2(self.rect.center)
        player_vec = pygame.math.Vector2(player.rect.center)
        distance = (player_vec - enemy_vec).magnitude()

        if distance > 0:
            direction = (player_vec - enemy_vec).normalize()
        else: 
            direction = pygame.math.Vector2()
        # print(f'{player_vec} - {enemy_vec}')
        return (distance, direction)

    def get_status(self, player):
        distance = self.get_player_distance_direction(player)[0]
        
        if distance <= self.monster_attack_radius:
            self.status2 = 'attack'
            self.status = 'move'
        elif distance <= self.monster_notice_radius:
            self.status = 'move'
            self.status2 = 'move'
        else:
            self.status = 'idle'
            self.status2 = 'idle'
    
    def update(self,dt):
        self.move(self.monster_speed)
        self.animate()

    def enemy_update(self,player):
        self.get_status(player)
        self.action(player)
    
    
    
    def action(self, player):
        if self.status2 == 'attack':
            print('attack')
        elif self.status2 == 'move': # movement towards the palyer
            self.direction = self.get_player_distance_direction(player)[1]
        else:
            self.direction = pygame.math.Vector2() # stops the direction of enemy
    