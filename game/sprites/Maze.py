import pygame

import game
import game.utils as utils

class Maze(pygame.sprite.Sprite):

    # Velocities
    x_vel = 0
    y_vel = 0

    # Constants
    speed = 1

    # State
    state = 1

    def __init__(self):
        """
        Maze object. The maze the player is tasked in navigating through.
        """
        pygame.sprite.Sprite.__init__(self)
        
        # Load both the locked and unlocked images of the maze
        locked, _ = utils.load_image('maze/maze_locked.png', colorkey=(255,255,255))
        unlocked, _ = utils.load_image('maze/maze_unlocked.png', colorkey=(255,255,255))
        
        # Scale the images to fit on the screen the way I want it to
        l_size = locked.get_size()
        ul_size = unlocked.get_size()

        scaled_l = pygame.transform.scale(locked, (int(l_size[0]*0.9), int(l_size[1]*0.9)))
        scaled_ul = pygame.transform.scale(unlocked, (int(ul_size[0]*0.9), int(ul_size[1]*0.9)))

        # Saving the scaled images into a list
        self.states = [
            (scaled_l.convert_alpha(), scaled_l.get_rect()),
            (scaled_ul.convert_alpha(), scaled_ul.get_rect())
        ]

        # Setting default state
        self.image, self.rect = self.states[self.state]

        # Creating a mask for collisions
        self.mask = pygame.mask.from_surface(self.image)   

        # Determining start position
        screenSize = game.screen.get_size()

        startLocation = (
            (screenSize[0]/2) - 140,
            (screenSize[1]/2) + 140
        )

        self.rect.bottomleft = startLocation

    def update(self):
        """
        Sprite update method. Executed every loop of the mainloop.
        """

        # Set state of maze
        self.image, self.rect = self.states[self.state]
        if self.state == 1:
            self.state = -1
            self.mask = pygame.mask.from_surface(self.image)

        # Get the current coordinate of the top left corner of the maze sprite
        x, y = self.rect.topleft
        
        # Move the mazes X coordinate, and move it back if it collides with the player
        self.rect.x = x + self.x_vel
        if self.collision(): self.rect.x = x - self.x_vel


        # Move the mazes Y coordinate, and move it back if it collides with the player
        self.rect.y = y + self.y_vel
        if self.collision(): self.rect.y = y - self.y_vel

    def set_x_vel(self,vel):
        """
        Sets the X velocity of the sprite

        Parameters:
        vel: A number
        """
        self.x_vel = vel * self.speed

    def set_y_vel(self,vel):
        """
        Sets the Y velocity of the sprite

        Parameters:
        vel: A number
        """
        self.y_vel = vel * self.speed
    
    def collision(self):
        """
        Tests for a collision between the player and the maze sprites
        """
        return bool(pygame.sprite.collide_mask(self, game.player))

def load_sprite():
    return Maze()