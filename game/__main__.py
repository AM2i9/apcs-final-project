import pygame
import sys

import game
import game.keys as bindings
import game.sprites as sprites

game.playerSprite = sprites.sprites["Player"]
game.mazeSprite = sprites.sprites["Maze"]

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    print(game.maze.x, game.maze.y, end='\r')
    bindings.checkKeyEvents()

    game.screen.fill((146, 146, 146))
    sprites.update(game.screen)
    pygame.display.flip()