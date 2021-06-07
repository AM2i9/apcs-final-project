import pygame
import sys

import game

# List of key bindings
bindings = [
    {
        "key": pygame.K_UP,
        "alt-key": pygame.K_w,
        "callback": lambda: game.maze.set_y_vel(1)
    },
    {
        "key": pygame.K_DOWN,
        "alt-key": pygame.K_s,
        "callback": lambda: game.maze.set_y_vel(-1)
    },
    {
        "key": pygame.K_LEFT,
        "alt-key": pygame.K_a,
        "callback": lambda: game.maze.set_x_vel(1)
    },
    {
        "key": pygame.K_RIGHT,
        "alt-key": pygame.K_d,
        "callback": lambda: game.maze.set_x_vel(-1)
    }
]

def loop():
    """
    Main event loop
    """

    for event in pygame.event.get():

        # Quit event
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Execute key bindings
    keysPressed = pygame.key.get_pressed()
    
    for bind in bindings:
        key = bind['key']
        alt = bind['alt-key']

        if keysPressed[key] or (keysPressed[alt] if alt else False):
            bind['callback']()

    