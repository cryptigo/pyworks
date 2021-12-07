import pygame
from pygame.locals import *

from .config import *
from .utils.color import *
from .utils.common import *


""" 
A basic pygame framework, made to be expandable and facilitate faster development of games and visualizations. 
----------------------------
Sample Usage:
----------------------------
    engine = Engine()
    engine.start()
    
    while engine.running:
        engine.main_loop()
    pygame.quit()
    sys.exit(0)
----------------------------
"""
class Engine:
    def __init__(self):
        # Initialize pygame
        pygame.init()
        
        # Load all assets
        self.load_assets()
        
        # Create screen
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption(WIN_TITLE)
        
        self.clock = pygame.time.Clock()
        self.running = True

    """ Load font files, icons, and other assets. """
    def load_assets(self):
        self.window_icon = pygame.image.load(ICON_FILE)
        self.ui_font = pygame.font.Font(UI_FONT_FILE, UI_FONT_SIZE)

    """ Runs before the game starts. This should be the first function you call, before the update function. """
    def start(self):
        pygame.display.set_icon(self.window_icon)
        self.running = True
        
    """ Runs every frame """
    def update(self):
        pass

    """ Render function. """
    def draw(self):
        self.screen.fill(WHITE)
        self.clock.tick(FPS)
        
        # Draw fps
        self.screen.blit(self._debug_fps(), FPS_TEXT_POS)
        pygame.display.update()

    """ Get the rounded FPS and return a text object with it. """
    def _debug_fps(self):
        self.fps = str(int(self.clock.get_fps()))
        fps_text = self.ui_font.render(self.fps, 1, FPS_TEXT_COLOR)
        return fps_text
    
    """ Check for events, such as closing the window, or detecting keypresses. """
    def events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = False               
            
    """ The main program loop. Call this when you have initialized everything. """
    def main_loop(self):
        while self.running:
            self.events()
            self.update()
            self.draw()
        self.running = False