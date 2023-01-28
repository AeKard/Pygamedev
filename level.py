import pygame
from setting import *
from player import Player
from tile import *
from sword import Sword
from UI import UI
from enemy import Enemy
from particle import AnimationPlayer

class level:
    def __init__(self):
        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # sprite Group
        # self.player_sprite = pygame.sprite.Group() # groups the player
        self.visible_sprite = YSortCameraGroup()
        self.obstacle_sprite = pygame.sprite.Group()
        

        #attack sprite 
        self.current_attack = None
        self.attackable_sprites = pygame.sprite.Group()
        self.attack_sprites = pygame.sprite.Group()
        # self.setup() # calls the function setup in init
        self.layer = 1
        #sprite setup
        self.create_map()
        # UI
        self.ui = UI()

        # ANIMATIONS
        self.animation_player = AnimationPlayer()
    
    def create_map(self):
        for row_index,row in enumerate(WORLD_MAP):
            # print(f'{row}' )
            for col_index, col in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE 
                if col == 'x':
                    Tile((x,y),[self.visible_sprite,self.obstacle_sprite]) # POSITION GROUP
                if col == '0':
                    Floor((x,y),[self.visible_sprite])
       
        self.enemy = Enemy('demon',(200,200),[self.visible_sprite, self.attackable_sprites], self.obstacle_sprite,self.damage_player,self.trigger_death_particles)
        self.enemy = Enemy('demon',(800,100),[self.visible_sprite, self.attackable_sprites], self.obstacle_sprite,self.damage_player,self.trigger_death_particles)
        self.enemy = Enemy('demon',(500,500),[self.visible_sprite, self.attackable_sprites], self.obstacle_sprite,self.damage_player,self.trigger_death_particles)
        self.player = Player((650,650),[self.visible_sprite], self.obstacle_sprite, self.create_attack,self.destroy_attack)
    # WEAPON
        

    def create_attack(self):
        self.current_attack = Sword(self.player,[self.visible_sprite,self.attack_sprites])

    def destroy_attack(self):
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None
    # def setup(self):
        # self.player = Player((640,360), self.player_sprite) # Gets the player pos and group

    def player_attack_logic(self):
        if self.attack_sprites:
            for attack_sprites in self.attack_sprites:
                collision_sprite = pygame.sprite.spritecollide(attack_sprites,self.attackable_sprites,False)
                if collision_sprite:
                    for target_prite in collision_sprite:
                        target_prite.get_damage(self.player)

    def damage_player(self, amount, attack_type):
            if self.player.vulnerable:
                self.player.health -= amount
                self.player.vulnerable = False
                self.player.hurt_time = pygame.time.get_ticks()

                # PARTICLEEEEESSRHASJHDGOJFB
                self.animation_player.create_particles(attack_type,self.player.rect.center,[self.visible_sprite])

    def trigger_death_particles(self,pos,particle_type):
        self.animation_player.create_particles(particle_type, pos, self.visible_sprite)
    def run(self, dt):
        self.display_surface.fill('#2e2e2e')
        self.visible_sprite.custom_draw(self.player)
        self.visible_sprite.update() # update the sprite and calls all children
        self.visible_sprite.enemy_update(self.player)
        self.player_attack_logic()
        self.ui.display(self.player)
        # self.player_sprite.draw(self.display_surface) # draw the sprite in display surface

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        # GENERAL SETUP
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()
    
    def custom_draw(self,player):
        for sprite in self.sprites():

            #geeting the offset of the player
            self.offset.x = player.rect.centerx - self.half_width
            self.offset.y = player.rect.centery - self.half_height
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)


    def enemy_update(self,player):
        enemy_sprites = [sprite for sprite in self.sprites() if hasattr(sprite, 'sprite_type') and sprite.sprite_type == 'enemy']
        for enemy in enemy_sprites:
            enemy.enemy_update(player)