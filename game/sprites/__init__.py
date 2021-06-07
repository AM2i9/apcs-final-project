import os
import importlib

def update(screen, sprites):
    """
    Updates all loaded sprites

    Parameters:
        screen (pygame.Surface): The display surface
        sprites (dict): dict containing all loaded sprites, can be obtained from
            load_sprites().
    """

    for sprite in sprites:
        sprite = sprites[sprite]
        sprite.update()
        screen.blit(sprite.image, sprite.rect)

def load_sprites() -> dict:
    """
    Load sprites from game.sprites package, and return them in a dict by name

    Returns:
        dict: Loaded sprites, with their names as keys
    """

    # Dict for storing sprites
    sprites = {}

    # load every sprite from the non-internal files in this package
    for file in os.listdir('game/sprites'):

        # Test for internal scripts and non-python files
        if file.startswith('_') or not file.endswith('.py'):
            continue
        
        # Import the sprite's file
        sprite_name = file[:-3]
        sprite = importlib.import_module(f'..sprites.{sprite_name}', 'game.sprites')

        # Load the sprite into the sprites dict
        sprites[sprite_name] = sprite.load_sprite()
    
    return sprites