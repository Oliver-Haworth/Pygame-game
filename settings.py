# --- settings.py ---
''' this file holds all game settings and configurations
    I intend to make this a .txt file later on 
    potentially i use this file as a layer to read from that file'''


# --- import library ---
''' import all required libraries '''
import os
from log_system import log


class Settings():
    ''' Settings class to hold game configuration constants '''
        
    GAME_WIDTH, GAME_HEIGHT = 1280, 720
    WINDOW_WIDTH, WINDOW_HEIGHT = 1, 1

    FPS = 60
    

    class Paths():
        ''' defines the asset paths used in the game '''

        # root directory
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

        log.debug(f"Root directory set to: {ROOT_DIR}")

        # subfolders
        ASSETS_DIR = os.path.join(ROOT_DIR, "assets")
        LEVELS_DIR = os.path.join(ROOT_DIR, "levels")

        log.debug(f"root assets directory set to: {ASSETS_DIR}")
        log.debug(f"Levels directory set to: {LEVELS_DIR}")

        PLAYER_IMG1 = os.path.join(ASSETS_DIR, "PlayerImg1.png")