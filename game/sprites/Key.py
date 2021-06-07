import pygame

import game
import game.utils as utils

class Key(pygame.sprite.Sprite):
    def __init__(self):
        """
        Key object. A key used to unlock the end of the maze
        """

        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = utils.load_image('sprites/key.png', colorkey=(255,255,255))

        # Create an image mask for collisions
        self.mask = pygame.mask.from_surface(self.image)

        # Offset of key from upper left corner of the maze
        self.offset = (500, 400)
    
    def update(self):
        """
        Sprite update method. Executed every loop of the mainloop.
        """

        # Set location of key relative to maze
        mx, my = game.maze.rect.topleft
        self.rect.center = (mx + self.offset[0], my + self.offset[1])
        
        # Check for collision with player, and remove itself if it is touched
        if self.mask:
            if pygame.sprite.collide_mask(self, game.player):
                self.offset = (-1000, -1000)
                self.mask = None

                # Unlock the maze
                game.maze.state = 1

def load_sprite():
    return Key()