import pygame
from game._maze import _maze

pygame.init()

maze = _maze()

playerSprite = None
mazeSprite = None

screen = pygame.display.set_mode((640,480))