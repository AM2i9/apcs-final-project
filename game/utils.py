import pygame
from pygame.constants import RLEACCEL

# Stole it from the pygame docs, just to let you know :)
def load_image(name, colorkey=None):
    """
    Loads an image from the assets folder

    name (string) : Path to the image file relative to the assets folder
    colorkey (RGB Value) : Colorkey
    """
    try:
        image = pygame.image.load(f'game/assets/{name}')
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()