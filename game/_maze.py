import pygame

import game

class _maze:
    x = 0
    y = 0

    x_vel = 0
    y_vel = 0

    speed = 1
    unlocked = False

    def set_x_vel(self,vel):
        self.x_vel = vel * self.speed

    def set_y_vel(self,vel):
        self.y_vel = vel * self.speed

    def updatepos(self):
        self.x += self.x_vel
        self.y += self.y_vel
        self.check_collisions()

    def set_location(self,x,y):
        self.x, self.y = x, y

    def check_collisions(self):

        offset = (
            (game.mazeSprite.rect.x - game.playerSprite.rect.x),
            (game.playerSprite.rect.y - game.mazeSprite.rect.y)
            )

        collision = pygame.sprite.collide_mask(game.mazeSprite, game.playerSprite)

        if collision:
            print('c', collision)
            if self.x_vel > 0:
                self.x = collision[0] + offset[0]
                print(offset)
                print(self.x, self.y)
        