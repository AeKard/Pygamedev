# module
from os import walk # allows us to walk different folder
import pygame
def import_folder(path):
    surface_list = []

    for _,__,img_file in walk(path):
        for image in img_file:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            print(full_path)
            surface_list.append(image_surf)
    return surface_list