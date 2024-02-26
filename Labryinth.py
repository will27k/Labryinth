import pygame
import os
from spritesheet import *
from map import *
from character_movement import *

pygame.init()

level = 'Title Screen'
running = True

dir_path = os.path.dirname(__file__)

play_button = pygame.image.load(os.path.join(dir_path, 'assets/pixil-frame-0.png')).convert_alpha()
help_button = pygame.image.load(os.path.join(dir_path, 'assets/pixil-frame-0(3).png')).convert_alpha()
quit_button = pygame.image.load(os.path.join(dir_path, 'assets/pixil-frame-0(4).png')).convert_alpha()
home_button = pygame.image.load(os.path.join(dir_path, 'assets/pixil-frame-0(5).png')).convert_alpha()
home_button_rect = pygame.rect.Rect(0,0,0,0)
blank_template = pygame.image.load(os.path.join(dir_path, 'assets/pixil-frame-0(1).png'))

font = pygame.font.Font('freesansbold.ttf', 20)
help_text = font.render('Player 1 use arrow keys for movement', True,(0,0,0),None)
help_text2 = font.render('Player 2 use WASD', True,(0,0,0),None)
help_text3 =font.render('Try to reach the opponents square', True,(0,0,0),None)
help_text4 = font.render('Simple.', True,(0,0,0),None)
player1_win_text = font.render('Player 1 wins!', True,(0,0,0), None)
player2_win_text = font.render('Player 2 wins!', True,(0,0,0), None)


def draw_button(image,x,y):
    image = pygame.transform.scale(image,(100,50))
    image_rect = image.get_rect(topleft = (x,y))
    window.blit(image,(x,y))
    return image_rect

def button_click(event):
    global level, running, playing, player1_x, player1_y, player2_x, player2_y, player1_idle_position,player2_idle_position

    mouse_position = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if play_button_rect.collidepoint(mouse_position):
            level = 'Game'
        elif help_button_rect.collidepoint(mouse_position):
            level = 'Help'
        elif quit_button_rect.collidepoint(mouse_position):
            running = False
        elif home_button_rect.collidepoint(mouse_position):
            playing = False
            level = 'Title Screen'
            player1_x, player1_y = 54, 95
            player2_x, player2_y = 918, 95
            player1_idle_position = 3   
            player2_idle_position = 3

def check_win():
    global level, playing
    player1_rect = pygame.Rect(player1_x,player1_y,SPRITE_WIDTH,SPRITE_HEIGHT)
    player2_rect = pygame.Rect(player2_x,player2_y,SPRITE_WIDTH,SPRITE_HEIGHT)
    if player1_rect.colliderect(starting_rect_player2):
        playing = False
        level = 'Player 1'
    if player2_rect.colliderect(starting_rect_player1):
        playing = False
        level = 'Player 2'

while running:

    if level == 'Title Screen':
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            button_click(event)
        
        draw_background(window, background_data_tiles, sprite_mapping_tiles, sprite_sheet_map)
        draw_background(window, background_data_walls, sprite_mapping_walls, sprite_sheet_map)
        draw_background(window, background_data_ceiling, sprite_mapping_ceiling, sprite_sheet_map)
        play_button_rect = draw_button(play_button,425,150)
        help_button_rect = draw_button(help_button,425,250)    
        quit_button_rect = draw_button(quit_button,425,350)

        pygame.display.flip()

    if level == 'Help':
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            button_click(event)
        draw_background(window, background_data_tiles, sprite_mapping_tiles, sprite_sheet_map)
        draw_background(window, background_data_walls, sprite_mapping_walls, sprite_sheet_map)
        draw_background(window, background_data_ceiling, sprite_mapping_ceiling, sprite_sheet_map)
        home_button_rect = draw_button(home_button,25, 30)
        window.blit(blank_template, (300,100))
        window.blit(help_text,(310,110))
        window.blit(help_text2,(310,150))
        window.blit(help_text3,(310,190))
        window.blit(help_text4,(310,230))

        pygame.display.flip()

    if level == 'Game':
        playing = True
        draw_background(window, background_data_tiles, sprite_mapping_tiles, sprite_sheet_map)
        draw_background(window, background_data_walls, sprite_mapping_walls, sprite_sheet_map)
        draw_background(window, background_data_ceiling, sprite_mapping_ceiling, sprite_sheet_map)
        draw_maze(window,maze_map_horizontal)
        draw_maze(window,maze_map_vertical)
        pygame.display.flip()
        while playing == True:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    playing = False
                button_click(event)

            keys = pygame.key.get_pressed()
            draw_background(window, background_data_tiles, sprite_mapping_tiles, sprite_sheet_map)
            draw_background(window, background_data_walls, sprite_mapping_walls, sprite_sheet_map)
            draw_background(window, background_data_ceiling, sprite_mapping_ceiling, sprite_sheet_map)
            last_update,frame = run_animation(last_update,animation_cooldown,frame)
            player1_x, player1_y, player1_idle_position = movement(keys,move_length, window,player1_x,player1_y,animation_list_left,animation_list_right,animation_list_up,animation_list_down,idle_list,player1_idle_position, frame,wall_rects,player1_left,player1_right,player1_up,player1_down)
            player2_x, player2_y, player2_idle_position = movement(keys,move_length, window,player2_x,player2_y,player2_animation_list_left,player2_animation_list_right,player2_animation_list_up,player2_animation_list_down,player2_idle_list,player2_idle_position, frame,wall_rects,player2_left,player2_right,player2_up,player2_down)
            home_button_rect = draw_button(home_button,25,30)
            draw_maze(window,maze_map_horizontal)
            draw_maze(window,maze_map_vertical)
            check_win()
            pygame.display.flip()

    if level == 'Player 1':
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            button_click(event)
        draw_background(window, background_data_tiles, sprite_mapping_tiles, sprite_sheet_map)
        draw_background(window, background_data_walls, sprite_mapping_walls, sprite_sheet_map)
        draw_background(window, background_data_ceiling, sprite_mapping_ceiling, sprite_sheet_map)
        home_button_rect = draw_button(home_button,25,30)
        window.blit(blank_template, (300,100))
        window.blit(player1_win_text, (320,120))

        pygame.display.flip()

    if level == 'Player 2':
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            button_click(event)
        draw_background(window, background_data_tiles, sprite_mapping_tiles, sprite_sheet_map)
        draw_background(window, background_data_walls, sprite_mapping_walls, sprite_sheet_map)
        draw_background(window, background_data_ceiling, sprite_mapping_ceiling, sprite_sheet_map)
        home_button_rect = draw_button(home_button,25,30)
        window.blit(blank_template, (300,100))
        window.blit(player2_win_text, (320,120))

        pygame.display.flip()

pygame.quit()