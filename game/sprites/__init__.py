import os
import pygame
import importlib

sprites = {}

def update(screen):
    for sprite in sprites:
        sprite = sprites[sprite]
        sprite.update()
        screen.blit(sprite.image, sprite.rect)

for file in os.listdir('game/sprites'):

    if file.startswith('__') or not file.endswith('.py'):
        continue

    sprite_name = file[:-3]
    sprite = importlib.import_module(f'..sprites.{sprite_name}', 'game.sprites')
    sprites[sprite_name] = sprite.load_sprite()