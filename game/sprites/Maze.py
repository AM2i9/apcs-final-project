import pygame

import game
import game.utils as utils

class Maze(pygame.sprite.Sprite):

    x_vel = 0
    y_vel = 0

    speed = 1
    unlocked = False

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

        self.rect.bottomleft = startLocation

    def update(self):
        self.image, self.rect = self.states[int(self.unlocked)]
        if self.unlocked:
            self.unlocked = True
            self.mask = pygame.mask.from_surface(self.image)

        x, y = self.rect.topleft
        
        self.rect.x = x + self.x_vel
        if self.collision(): self.rect.x = x - self.x_vel
        self.rect.y = y + self.y_vel
        if self.collision(): self.rect.y = y - self.y_vel

    def set_x_vel(self,vel):
        self.x_vel = vel * self.speed

    def set_y_vel(self,vel):
        self.y_vel = vel * self.speed
    
    def collision(self):
        return bool(pygame.sprite.collide_mask(self, game.playerSprite))

def load_sprite():
    return Maze()