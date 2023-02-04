# Dinosaur player images by Arks
# https://arks.itch.io/dino-characters
# Twitter: @ScissorMarks

import pygame
import random
import src.engine as engine
from time import time 
from screeninfo import get_monitors

# CONSTANT VARIABLES
gravity_acceleration = 1
framerate = 60
fontname = 'arialunicode' 
monitors = get_monitors()
main_monitor = monitors[0]
SCREEN_SIZE = (main_monitor.width, main_monitor.height/4)

# COLORS
BLACK = (50,50,50)
WHITE = (255, 255, 255)

def random_start_coordinates():
    return random.randint(10, SCREEN_SIZE[0]-10)

def draw_text(character):
    # create a text surface object,
    # on which text is drawn on it.
    text = font.render(character.name, True, WHITE)
    # create a rectangular object for the
    # text surface object
    textRect = text.get_rect()

    # set the center of the rectangular object.
    textRect.center = (character.player_x + character.player_image_size[0]//2, character.player_y-10)
    screen.blit(text, textRect)

if __name__ == '__main__':
    # init
    pygame.init()
    logo = pygame.image.load("./assets/icon/icon_1024x1024x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption('Pixelous')
    font = pygame.font.SysFont(fontname, 12)
    screen = pygame.display.set_mode(SCREEN_SIZE, pygame.NOFRAME)
    screen_border = pygame.Rect(*screen.get_rect().center, 0, 0).inflate(SCREEN_SIZE)
    center_of_screen = screen.get_rect().center

    clock = pygame.time.Clock()

    characters = []
    
    # get followers/subscribers from Twitch
    # TODO

    # get subscribers from Youtube
    # TODO

    # get name from text file
    all_names = open('./names.txt','r')
    for line in all_names:
        characters.append( \
            engine.Character(random_start_coordinates(),center_of_screen[1], line.strip()))

    # for testing purposes
    # characters.append(engine.Character(random_start_coordinates(),center_of_screen[1], "HelloWorld"))
    # characters.append(engine.Character(random_start_coordinates(),center_of_screen[1], "joana"))
    
    running = True
    while running:
    # game loop
        screen.fill(BLACK) # draw a black screen
        
        # update player animation cycle
        for character in characters:
            if(int(time()) > character.player_timestamp + character.player_animation_duration):
                character.player_timestamp = int(time())
                character.player_animation_duration = random.randint(2,7)
                if character.player_state == 'idle':
                    character.player_state = 'walking'
                    if bool(random.getrandbits(1)): # random boolean
                        character.player_direction = 'left'
                    else: character.player_direction = 'right'

                else: character.player_state = 'idle'

            # update player animations
            character.player_animation[character.player_state].update()

            # write character name
            draw_text(character)

            # player input
            new_player_x = character.player_x
            new_player_y = character.player_y

            if character.player_state == 'walking':
                if character.player_direction == 'left':
                    new_player_x-=2
                elif character.player_direction == 'right':
                    new_player_x+=2
            
            # vertical movement(gravity)
            character.player_speed += gravity_acceleration
            new_player_y += character.player_speed
            
            inside_border = screen_border.collidepoint(character.player_x,\
                new_player_y + character.player_image_size[1])
            
            if inside_border:
                character.player_y = new_player_y
            else:
                character.player_speed = 0 # hit the bottom, vertical movement stops

            # horizontal movement
            new_player_rect = pygame.Rect(new_player_x,100,\
                character.player_image_size[0], character.player_image_size[1])
            
            # check if character is inside screen
            inside_border = screen_border.collidepoint(new_player_x,character.player_y) \
                and screen_border.collidepoint(new_player_x + character.player_image_size[0],character.player_y)
            
            if inside_border:
                character.player_x = new_player_x
            else:
                if character.player_direction == 'left':
                    character.player_direction = 'right'
                else: character.player_direction = 'left'
            
            # draw
            if character.player_direction == 'right':
                character.player_animation[character.player_state]\
                    .draw(screen,character.player_x,character.player_y, False, False)
            else:
                character.player_animation[character.player_state]\
                    .draw(screen,character.player_x,character.player_y, True, False)
        
        # check for quit
        for event in pygame.event.get() :
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()

        clock.tick(framerate)

    # quit
    pygame.quit()