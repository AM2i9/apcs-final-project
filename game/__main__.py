import pygame

import game
import game.events as events
import game.sprites as sprites

game.loaded_sprites = sprites.load_sprites()

# Create the player and maze sprites
game.player = game.loaded_sprites["Player"]
game.maze = game.loaded_sprites["Maze"]

# Overrides

# Player Speed:
game.maze.speed = 2

# Start with maze unlocked (0: Locked, 1: Unlocked)
# game.maze.state = 1

# End screen stuff
font = pygame.font.SysFont('Ariel',  60)
end_text = font.render("You completed the maze!", True, (0,0,0))
end_text_rect = end_text.get_rect()
end_text_rect.center = game.screen_size[0] // 2, game.screen_size[1] // 2

# Main game loop
while True:

    # Reset velocities
    game.maze.set_x_vel(0)
    game.maze.set_y_vel(0)

    # Check events
    events.loop()

    if game.running:
        # Checking if the player has reached the end zone
        # Currently only works on 480p resolution, because of screen coordinates
        if (-3064 > game.maze.rect.x > -3362 and game.maze.rect.y > 117):
            game.running = False
            continue

        # Draw graphics
        game.screen.fill((146, 146, 146))
        sprites.update(game.screen, game.loaded_sprites)
    else:
        game.screen.fill((255,255,255))
        game.screen.blit(end_text, end_text_rect)

    # Update the display
    pygame.display.flip()