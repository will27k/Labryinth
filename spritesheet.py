import pygame
import os

pygame.init()

dir_path = os.path.dirname(__file__)

screen_width, screen_height = 1008, 594

window = pygame.display.set_mode((screen_width,screen_height))

class SpriteSheet():
    def __init__(self, image) -> None:
        self.sheet = image

    def get_image(self,frame,width,height):
        image = pygame.Surface((width,height)).convert_alpha()
        image.blit(self.sheet,(0,0),((frame*width),9,width,height))
        image = pygame.transform.scale(image,(32,46))
        return image
    

#Player 1 Sprite
player1_moving = pygame.image.load(os.path.join(dir_path, 'assets/Bob_Run_16x16.png')).convert()
player1_idle = pygame.image.load(os.path.join(dir_path, 'assets/Bob_idle_16x16.png')).convert()
player1_moving = SpriteSheet(player1_moving)
player1_idle = SpriteSheet(player1_idle)
player1_x, player1_y = 54, 95

#Player 2 Sprite
player2_moving = pygame.image.load(os.path.join(dir_path, 'assets/Adam_Run_16x16.png')).convert()
player2_idle = pygame.image.load(os.path.join(dir_path, 'assets/Adam_idle_16x16.png')).convert()
player2_moving = SpriteSheet(player2_moving)
player2_idle = SpriteSheet(player2_idle)
player2_x, player2_y = 918, 95
