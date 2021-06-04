import pygame

import game
import game.utils as utils

class Maze(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.unlocked = False
        
        locked, _ = utils.load_image('maze/maze_locked.png', colorkey=(255,255,255))
        unlocked, _ = utils.load_image('maze/maze_unlocked.png', colorkey=(255,255,255))
        
        l_size = locked.get_size()
        ul_size = unlocked.get_size()

        scaled_l = pygame.transform.scale(locked, (int(l_size[0]*0.7), int(l_size[1]*0.7)))
        scaled_ul = pygame.transform.scale(unlocked, (int(ul_size[0]*0.7), int(ul_size[1]*0.7)))

        self.states = [
            (scaled_l.convert_alpha(), scaled_l.get_rect()),
            (scaled_ul.convert_alpha(), scaled_ul.get_rect())
        ]

        self.image, self.rect = self.states[0]
        self.mask = pygame.mask.from_surface(self.image)   

        screenSize = game.screen.get_size()

        startLocation = (
            (screenSize[0]/2) - 140,
            (screenSize[1]/2) + 140
        )

        game.maze.set_location(*startLocation)

    def update(self):
        self.image, self.rect = self.states[int(game.maze.unlocked)]
        if game.maze.unlocked and not self.unlocked:
            self.unlocked = True
            self.mask = pygame.mask.from_surface(self.image)
        
        self.rect.bottomleft = (game.maze.x, game.maze.y)

def load_sprite():
    return Maze()