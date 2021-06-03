import pygame

pygame.init()

screen = pygame.display.set_mode((640,480))
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((146, 146, 146))