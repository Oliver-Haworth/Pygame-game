# --- main.py ---
''' this file maintains the modules and runtime '''


# --- import library ---
''' import all required libraries '''

import pygame
from settings import Settings
from player import Player
from log_system import log  


# Clear Logs
with open('game_log.log', 'w'):
    log.debug('main.py - new session started')

log.debug('All modules imported')


# --- Game class ---
class Game:
    ''' Game class to manage game states and functionalities'''

    def __init__(self):
        # Initializations
        pygame.init()

        # Clock
        self.clock = pygame.time.Clock()
        
        # Set up display
        self.setup_display(
            Settings.GAME_WIDTH, 
            Settings.GAME_HEIGHT, 
            Settings.WINDOW_WIDTH, 
            Settings.WINDOW_HEIGHT
        )
        
        # Load Background
        self.LoadBackground(Settings.GAME_WIDTH, Settings.GAME_HEIGHT)
        
        self.running = True


    def setup_display(self, GAME_WIDTH, GAME_HEIGHT,
                      WINDOW_WIDTH, WINDOW_HEIGHT):
        """Sets up the main display and canvas."""

        self.screen = pygame.display.set_mode(
            (GAME_WIDTH * WINDOW_WIDTH, 
             GAME_HEIGHT * WINDOW_HEIGHT))
        self.canvas = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))

        log.debug('Display and canvas set up')
    

    def LoadBackground(self, GAME_WIDTH, GAME_HEIGHT):
        ''' Loads and scales the background image '''

        self.bg_surf = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        self.bg_surf.fill((40, 20, 60))

        log.debug('Background loaded and scaled')


    def run(self):
        ''' main game loop 
        NO LOGS ALLOWED IN THIS method, they will loop per frame'''

        while self.running:
            dt = self.clock.tick(Settings.FPS) / 1000.0
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # 1. Clear the canvas with new background
            self.canvas.blit(self.bg_surf, (0, 0))

            # 2. Draw the player onto the canvas
            pygame.draw.rect(self.canvas, Player.box_color, Player.box_rect)

            # 3. Scale the canvas to screen size
            scaled_window = pygame.transform.scale(self.canvas, self.screen.get_size())
            
            # 4. Draw to the screen
            self.screen.blit(scaled_window, (0, 0))
            
            pygame.display.flip()


if __name__ == "__main__":
    Game().run()
    pygame.quit()