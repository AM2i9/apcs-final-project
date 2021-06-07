import pygame

import game
import game.events as events
import game.sprites as sprites

game.loaded_sprites = sprites.load_sprites()

# Create the player and maze sprites
game.player = game.loaded_sprites["Player"]
game.maze = game.loaded_sprites["Maze"]

while True:

    # Reset velocities
    game.maze.set_x_vel(0)
    game.maze.set_y_vel(0)

    # Check events
    events.loop()

    # Draw graphics
    game.screen.fill((146, 146, 146))
    sprites.update(game.screen, game.loaded_sprites)

    # Update the display
    pygame.display.flip()