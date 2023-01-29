import pygame
from support import *
from entity import *
from entity import Entity

class Player(Entity):
    def __init__(self, pos, groups,obstacle_sprite, create_attack, destroy_attack): # NEED TO KNOW WHERE OBSTACLE IS SO USE OBSTACLE 
        super().__init__(groups)
        # Initializa the player
        # self.player = pygame.image.load('player/knight_m_idle_anim_f0').convert_alpha()
    
        # call support and for animation
        self.import_assets()
        self.status = 'right'
        # character general setup
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.character_scaled().get_rect(center = pos)
        self.hitbox = self.rect.inflate(0,-26)
        # print(self.rect)
        #orientation
        self.orientation_x = False
        self.orientation_y = False
        #movement attribute
        self.orient = 'right'
        self.speed = 5
        #obstacle
        self.obstacle_sprites = obstacle_sprite
        # Weapon
        self.attacking = False
        self.create_attack = create_attack
        self.destroy_attack = destroy_attack
        self.attack_cooldown = 400
    
        # character health
        self.stats = {'health': 100, 'attack': 10}
        self.health = self.stats['health']

        #DAMAGE TIMER
        self.vulnerable = True
        self.hurt_time = None
        self.invulnerability_duration = 500

        self.player = True
        self.weapon_attack_sound = pygame.mixer.Sound('sound/sword.wav')
        self.weapon_attack_sound.set_volume(0.4)
        self.player_death_sound = pygame.mixer.Sound('sound/playerdeath.mp3')
        self.player_death_sound.set_volume(0.6)
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
    
    def animate(self):
        self.frame_index += self.animation_speed
        # print(self.status)
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0
        self.image = pygame.transform.scale(self.animations[self.status][int(self.frame_index)],(16*3,22*3))
    
        #flicker
        if not self.vulnerable:
            alpha= self.wave_value()
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(255)

    def health_status(self):
        if self.health <= 0:
            self.player = False
            self.player_death_sound.play()
    
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
                self.weapon_attack_sound.play()
        else:
            self.direction.y = 0
            self.direction.x = 0
            if self.direction == 'right':
                self.status = 'right_idle'
            else:
                self.direction == 'left'

    def cooldown(self):
        current_time = pygame.time.get_ticks()

        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.attacking = False
                self.destroy_attack()
        
        if not self.vulnerable:
            if current_time - self.hurt_time >= self.invulnerability_duration:
                self.vulnerable = True

    def update(self):
        self.input()
        self.cooldown()
        self.move(self.speed)
        self.animate()
        self.health_status()
    
    def damage(self):
        return self.stats['attack'] 


