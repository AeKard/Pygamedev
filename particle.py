import pygame
from support import import_folder

class AnimationPlayer():
    def __init__(self):
        # attack
        self.frames = {
            'slash': import_folder('slash/'),
            #monster Death:
            'demon': import_folder('nova/'),
            'oger': import_folder('nova/')
        }

    def create_particles(self,attack_type,pos,groups):
        
        animation_frames = self.frames[attack_type]
        ParticleEffect(pos,animation_frames,groups)


class ParticleEffect(pygame.sprite.Sprite):
    def __init__(self,pos,animation_frames, groups):
        super().__init__(groups)
        self.frame_index = 0
        self.animations_speed = 0.15
        self.frames = animation_frames
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center = pos)
    
    
    def animate(self):
        self.frame_index += self.animations_speed
        if self.frame_index >= len(self.frames):
            self.kill() # Killing the particle animation
        else:
            self.image = self.frames[int(self.frame_index)]
    
    def update(self):
        self.animate()