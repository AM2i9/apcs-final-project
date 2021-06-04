import pygame

import game

class _maze:
    x = 0
    y = 0
    speed = 0.2
    unlocked = False

    def check_player_collision(self):
        collide = pygame.sprite.collide_mask(game.mazeSprite, game.playerSprite)
        if collide:
            return True

    def set_x(self, x):
        self.x = x
    
    def change_x(self, change):
        if not self.check_player_collision('x', change):
            self.x = self.x + (change*self.speed)
    
    def set_y(self, y):
        self.y = y
    
    def change_y(self, change):
        if not self.check_player_collision('y', change):
            self.y = self.y + (change*self.speed)

    def set_location(self, x, y): 
        self.x = x
        self.y = y