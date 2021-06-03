import pygame
import sys

import game

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    game.screen.blit(game.background, (0,0))
    pygame.display.flip()