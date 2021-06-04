import pygame

import game
import game.utils as utils

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = utils.load_image('sprites/player.png')

        self.mask = pygame.mask.from_surface(self.image)

        screenSize = game.screen.get_size()
        self.rect.midtop = (
            (screenSize[0]/2),
            (screenSize[1]/2) - (self.rect.height/2)
        )
    
    def update(self):
        pass

def load_sprite():
    return Player()