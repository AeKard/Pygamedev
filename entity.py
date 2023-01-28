import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self,groups):
        super().__init__(groups)
        self.frame_index = 0
        self.animation_speed = 0.15
        self.direction = pygame.math.Vector2()    

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
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect): #sprite.rect.colide is the obstacle sprite #self.rect is the player 
                    if self.direction.x > 0: # moving right
                        self.rect.right = sprite.rect.left # right = to left
                    if self.direction.x < 0:
                        self.rect.left = sprite.rect.right # moving left
                

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect): #sprite.rect.colide is the obstacle sprite #self.rect is the player 
                    if self.direction.y > 0: # moving right
                        self.rect.bottom = sprite.rect.top # moving down
                    if self.direction.y < 0:
                        self.rect.top = sprite.rect.bottom # moving up