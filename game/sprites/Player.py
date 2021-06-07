import pygame

import game
import game.utils as utils

class Player(pygame.sprite.Sprite):
    def __init__(self):
        """
        Player object. A static red square in the middle of the screen to
        represent the player
        """

        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = utils.load_image('sprites/player.png')

        # Create an image mask for collisions
        self.mask = pygame.mask.from_surface(self.image)

        # Placing the player in the middle of the screen
        screenSize = game.screen.get_size()
        self.rect.center = (
            (screenSize[0]/2),
            (screenSize[1]/2)
        )
    
    def update(self):
        """
        Sprite update method. Executed every loop of the mainloop.
        """
        # Player does not need to be updated
        pass

def load_sprite():
    return Player()