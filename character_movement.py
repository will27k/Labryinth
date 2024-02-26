import pygame
from spritesheet import *

pygame.init()


clock = pygame.time.Clock()

def movement(keys, move_length, window, sprite_x, sprite_y, animation_list_left, animation_list_right, animation_list_up, animation_list_down, idle_list, idle_position, frame, wall_rects,left,right,up,down):
    move_direction = None

    if keys[left]:
        move_direction = 'left'
    elif keys[right]:
        move_direction = 'right'
    elif keys[up]:
        move_direction = 'up'
    elif keys[down]:
        move_direction = 'down'
    
    if move_direction:
        next_x, next_y = sprite_x, sprite_y
        if move_direction == 'left':
            next_x -= move_length
        elif move_direction == 'right':
            next_x += move_length
        elif move_direction == 'up':
            next_y -= move_length
        elif move_direction == 'down':
            next_y += move_length
        
        # Check for collision before moving
        next_rect = pygame.Rect(next_x, next_y, 32, 46)
        collision = False
        for wall_rect in wall_rects:
            if next_rect.colliderect(wall_rect):
                collision = True
                break
        
        if not collision:
            sprite_x, sprite_y = next_x, next_y
    
    # Draw the sprite
    if move_direction == 'left':
        window.blit(animation_list_left[frame], (sprite_x, sprite_y))
        idle_position = 2
    elif move_direction == 'right':
        window.blit(animation_list_right[frame], (sprite_x, sprite_y))
        idle_position = 0
    elif move_direction == 'up':
        window.blit(animation_list_up[frame], (sprite_x, sprite_y))
        idle_position = 1
    elif move_direction == 'down':
        window.blit(animation_list_down[frame], (sprite_x, sprite_y))
        idle_position = 3
    else:
        window.blit(idle_list[idle_position], (sprite_x, sprite_y))
    
    return sprite_x, sprite_y, idle_position

#Values for animations
move_length = 5
player1_idle_position = 3
player2_idle_position = 3
idle_count = 4
animation_count = 24
animation_cooldown = 60
frame = 0
last_update = pygame.time.get_ticks()



#Lists for animations of sprites
idle_list = []
animation_list_left = []
animation_list_right = []
animation_list_up = []
animation_list_down = []
player1_left,player1_right,player1_up,player1_down = pygame.K_LEFT,pygame.K_RIGHT,pygame.K_UP,pygame.K_DOWN
            
for x in range(idle_count):
    idle_list.append(player1_idle.get_image(x,16,23))

for x in range(0,6):
    animation_list_right.append(player1_moving.get_image(x,16,23))
for x in range(6,12):
    animation_list_up.append(player1_moving.get_image(x,16,23))
for x in range(12,18):
    animation_list_left.append(player1_moving.get_image(x,16,23))
for x in range(18,24):
    animation_list_down.append(player1_moving.get_image(x,16,23))

player2_idle_list = []
player2_animation_list_left = []
player2_animation_list_right = []
player2_animation_list_up = []
player2_animation_list_down = []
player2_left,player2_right,player2_up,player2_down = pygame.K_a,pygame.K_d,pygame.K_w,pygame.K_s

            
for x in range(idle_count):
    player2_idle_list.append(player2_idle.get_image(x,16,23))

for x in range(0,6):
    player2_animation_list_right.append(player2_moving.get_image(x,16,23))
for x in range(6,12):
    player2_animation_list_up.append(player2_moving.get_image(x,16,23))
for x in range(12,18):
    player2_animation_list_left.append(player2_moving.get_image(x,16,23))
for x in range(18,24):
    player2_animation_list_down.append(player2_moving.get_image(x,16,23))

def run_animation(last_update,animation_cooldown,frame):
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        if frame == 5:
            frame = 0
        else:
            frame += 1
            last_update = current_time
    return last_update, frame