import os
os.environ["SDL_AUDIODRIVER"] = "dummy"
os.environ["SDL_VIDEODRIVER"] = "dummy"

import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_KINDS, ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS, ASTEROID_SPAWN_RATE
from player import *

def main():
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    plater.containers = (updatable, drawable)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
       
        screen.fill((0, 0, 0))

        updatable.update(dt)
        
        for d in drawable: 
            d.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
