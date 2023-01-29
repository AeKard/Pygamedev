import pygame
from support import *
from entity import Entity
from setting import *

class Enemy(Entity):
    def __init__(self,monster_name,pos,groups, obstacle_sprites, damage_player, trigger_death_particles):
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
        self.hitbox = self.rect.inflate(0,10)
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

        #Player interaction for tboss
        self.can_attack = True
        self.attack_time = None
        self.attack_cooldown = 400
        self.damage_player = damage_player
        self.trigger_death_particles = trigger_death_particles
        # invincibility timer
        self.vulnerable = True
        self.hit_time = None
        self.invincibility_duration = 300
        #
        self.death_sound = pygame.mixer.Sound('sound/death.wav')
        self.hit_sound = pygame.mixer.Sound('sound/hit.wav')
        self.attack_sound = pygame.mixer.Sound('sound/slash.wav')
        self.death_sound.set_volume(0.2)
        self.hit_sound.set_volume(0.2)
        self.attack_sound.set_volume(0.3)
        #Number of enemy
    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.animations[self.status]):
            if self.status2 == 'attack':
                self.can_attack = False
            self.frame_index = 0
        self.image = pygame.transform.scale(self.animations[self.status][int(self.frame_index)],(16*3,22*3))
        self.rect = self.image.get_rect(center = self.hitbox.center)
        if not self.vulnerable:
            alpha = self.wave_value()
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(255)
    
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
        
        if distance <= self.monster_attack_radius and self.can_attack:
            self.status2 = 'attack'
            self.status = 'move'
        elif distance <= self.monster_notice_radius:
            self.status = 'move'
            self.status2 = 'move'
        else:
            self.status = 'idle'
            self.status2 = 'idle'

    def update(self):
        self.hit_reaction()
        self.move(self.monster_speed)
        self.animate()
        self.cooldowns()
        self.check_death()
        # self.numberOfenemy()

    def enemy_update(self,player):
        self.get_status(player)
        self.action(player)

    def action(self, player):
        if self.status2 == 'attack':
            self.attack_time = pygame.time.get_ticks()
            self.damage_player(self.monster_damage, self.monster_attack_type,player)
            self.attack_sound.play()
        elif self.status2 == 'move': # movement towards the palyer
            self.direction = self.get_player_distance_direction(player)[1]
        else:
            self.direction = pygame.math.Vector2() # stops the direction of enemy
    
    def cooldowns(self): # THE BOSS
        current_time = pygame.time.get_ticks()
        if not self.can_attack:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.can_attack = True
        
        if not self.vulnerable:
            if current_time - self.hit_time >= self.invincibility_duration:
                self.vulnerable = True
    
    def get_damage(self, player):
        if self.vulnerable:
            self.hit_sound.play()
            self.monster_health -= player.damage()
            self.hit_time = pygame.time.get_ticks()
            self.vulnerable = False
    
    def hit_reaction(self):
        if not self.vulnerable:
            self.direction *= -self.monster_resistance
    
        
    def check_death(self):
        if self.monster_health <= 0:
            self.trigger_death_particles(self.rect.center,self.monster_name)
            self.kill()
            self.death_sound.play()

