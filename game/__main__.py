import pygame
import sys

import game
import game.keys as bindings
import game.sprites as sprites

game.playerSprite = sprites.sprites["Player"]
game.maze = sprites.sprites["Maze"]

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    game.maze.set_x_vel(0)
    game.maze.set_y_vel(0)

    bindings.checkKeyEvents()

    game.screen.fill((146, 146, 146))
    sprites.update(game.screen)
    pygame.display.flip()