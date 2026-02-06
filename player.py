# --- player.py ---
''' this file maintains anything regarding the player e.g. mechanics '''


# --- import library ---
''' import all required libraries '''

import pygame
from settings import Settings
from log_system import log  


# --- Player class ---
class Player:
    box_color = (255, 0, 0)
    box_rect = pygame.Rect(200, 150, 200, 100)

