# --- player.py ---
''' 
this file maintains anything regarding the player e.g. mechanics
all functions and methods must only use variables and constants from __init__ or peramiters
'''


# --- import library ---
''' import all required libraries '''

import pygame
from settings import Settings
from log_system import log  


# --- Player class ---
class Player:
    ''' '''

    def __init__(self, x, y, image_path):
        self.position = pygame.math.Vector2(x, y)
        self.velocity = pygame.math.Vector2(0, 0)
        self.on_ground = False

        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(topleft=(x, y))


    def draw_player(self, surface):
        ''' '''
        
        self.rect.topleft = (self.position.x, self.position.y)
        surface.blit(self.image, self.rect)