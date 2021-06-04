import pygame

import game

class _maze:
    x = 0
    y = 0

    speed = 1
    unlocked = False

    def check_player_collision(self):
        return game.playerSprite.mask.overlap(game.mazeSprite.mask, (
            game.mazeSprite.rect.x - game.playerSprite.rect.x,
            game.mazeSprite.rect.y - game.playerSprite.rect.y
        ))

    def set_x(self, x):
        self.set_location(x, self.y)
    
    def change_x(self, change):
        self.set_location(self.x + change, self.y)
    
    def set_y(self, y):
        self.set_location(self.x, y)
    
    def change_y(self, change):
        self.set_location(self.x, self.y + change)

    def set_location(self, x, y, start=False):
        _prev_x, _prev_y = self.x, self.y
        self.x, self.y = x, y
        print(x,y,_prev_x,_prev_y)
        if not start and self.check_player_collision():
            print("There is a collision")
            print(self.x, self.y)
            self.x, self.y = _prev_x, _prev_y
            print(self.x, self.y)
           
        