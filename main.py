from core.engine import *
import pygame
import sys


def main():
    engine = Engine()
    engine.start()
    
    while engine.running:
        engine.main_loop()
    pygame.quit()
    sys.exit(0)
    
    
if __name__ == '__main__':
    main()