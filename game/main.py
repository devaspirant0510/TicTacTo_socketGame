import pygame
import random
import sys

SCREEN_WIDTH=1200
SCREEN_HEIGHT=900

if __name__ == "__main__":
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    while True:
        screen.fill(0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()
