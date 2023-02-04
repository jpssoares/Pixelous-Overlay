import pygame
import random

from time import time

class Animation():
    def __init__(self, imageList):
        self.imageList = imageList
        self.imageIndex = 0
        self.animationTimer = 0
        self.animatonSpeed = 10

    def update(self):
        self.animationTimer += 1
        if self.animationTimer >= self.animatonSpeed:
            self.animationTimer = 0
            self.imageIndex += 1
            if self.imageIndex > len(self.imageList) - 1:
                self.imageIndex = 0
    
    def draw(self, screen, x, y, flipX, flipY):
        screen.blit(pygame.transform.flip(self.imageList[self.imageIndex], flipX, flipY), (x, y))

class Character():
    def __init__(self, player_x, player_y, name, foldername = None, image_suffix = None):
        if foldername == None:
            foldername = 'character01'
        if image_suffix == None:
            image_suffix = 'vita_'

        self.name = name
        self.player_image = pygame.image.load(f'assets/{foldername}/{image_suffix}00.png')
        self.player_image_size = (45,51)
        self.player_x = player_x
        self.player_y = player_y
        self.player_animation_duration = random.randint(2,7)
        self.player_direction = 'right'
        self.player_state = 'idle' # or 'walking'
        self.player_speed = 0
        self.player_timestamp = int(time())
        self.player_animation = {
            'idle' : Animation([
                pygame.image.load(f'assets/{foldername}/{image_suffix}00.png'),
                pygame.image.load(f'assets/{foldername}/{image_suffix}01.png'),
                pygame.image.load(f'assets/{foldername}/{image_suffix}02.png'),
                pygame.image.load(f'assets/{foldername}/{image_suffix}03.png')
            ]),
            'walking' : Animation([
                pygame.image.load(f'assets/{foldername}/{image_suffix}04.png'),
                pygame.image.load(f'assets/{foldername}/{image_suffix}05.png'),
                pygame.image.load(f'assets/{foldername}/{image_suffix}06.png'),
                pygame.image.load(f'assets/{foldername}/{image_suffix}07.png'),
                pygame.image.load(f'assets/{foldername}/{image_suffix}08.png'),
                pygame.image.load(f'assets/{foldername}/{image_suffix}09.png')
            ])
        }


