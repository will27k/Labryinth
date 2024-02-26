import pygame
import os
from spritesheet import screen_height,screen_width

pygame.init()

dir_path = os.path.dirname(__file__)

# Load your sprite sheet
sprite_sheet_map = pygame.image.load(os.path.join(dir_path, 'assets/Room_Builder_free_48x48.png')).convert_alpha()

# Define the size of each sprite in the map sprite sheet
SPRITE_WIDTH, SPRITE_HEIGHT = 48, 48

starting_rect_player1 = pygame.Rect(54, 95,48,48)
starting_rect_player2 = pygame.Rect(918,95,48,48)

# Define your mapping between characters and sprite elements
sprite_mapping_tiles = {
    "a": (528, 240), #tile
    "b": (576, 240), #tile
    "c": (624, 240), #tile
    "d": (528, 288), #tile
    "e": (576, 288), #tile
    "f": (624, 288), #tile
    "g": (528,336), #Player 1 starting tile
    "h": (528,432) #Player 2 starting tile
}

sprite_mapping_walls = {
    "a": (0, 240), #wall top left
    "b": (48, 240), #wall top middle
    "c": (96, 240), #wall top right
    "d": (0, 288), #wall bottom left
    "e": (48, 288), #wall bottom middle
    "f": (96, 288), #wall bottom right
    "g": (144, 240), #wall column top
    "h": (144, 288), #wall column bottom
}

sprite_mapping_ceiling = {
    "a": (720, 0), #top piece empty top left half and top right half and bottom
    "b": (720, 48), #top piece empty bottom and top
    "c": (384, 96), #top piece bottom empty
    "d": (672, 0), #top piece empty top left half and bottom
    "e": (768, 0), #top piece empty top right half and bottom
    "f": (240, 96), #corner border right
    "g": (288, 96), #corner border left
    "h": (624, 96), #left border down
    "i": (528, 96), #right border down
    "j": (240, 48), #corner border right
    "k": (288, 48), #corner border left
    "l": (576, 144), #bottom wall
}


# Example background data string
background_data_tiles = [
    "baebadcdfabcdfbcadbca",
    "adfcefdcbdfebadfebefa",
    "agedcfcbedacfdbefcdhe",
    "ecafdbcabcedbcedacedd",
    "eedbacebcdabdcebcdabf",
    "ddbacebdcebcdbacdeceb",
    "bbcaefabcdefabcdefabd",
    "cecdbcabedbaecdacdbcc",
    "dcbcdbeacdbcebcdacbea",
    "cfdecabdfecabefcdabee",
    "abcdefabcdefabcdefabc",
    "bdfbecdbfceabefdcbefe",
    "dbedcfcbedacfdbefcdea",
]

background_data_walls = [
    "abbbbbbbbbbbbbbbbbbbc",
    "deeeeeeeeeeeeeeeeeeef",
    ".....................",
    ".....................",
    ".....................",
    ".....................",
    ".....................",
    ".....................",
    ".....................",
    ".....................",
    ".....................",
    ".....................",
    ".....................",
]

background_data_ceiling = [
    "g...................f",
    "h...................i",
    "h...................i",
    "h...................i",
    "h...................i",
    "h...................i",
    "h...................i",
    "h...................i",
    "h...................i",
    "h...................i",
    "h...................i",
    "h...................i",
    "klllllllllllllllllllj",
]

maze_map_vertical = [
    "...............",
    "....|.||...|...",
    "||...||.|.||||.",
    ".|..|.||.||||.|",
    ".||..|..|.|.|||",
    "|.|||.||...|..|",
    "|.|.||.|....|.|",
    ".|....|......|.",
    "...............",
]

maze_map_horizontal = [
    "................",
    "................",
    "..---....-....-.",
    "-..---..-.-...-.",
    ".-.--.--.-..-...",
    "....--..-.--.-..",
    ".--...-.---.---.",
    "...---.-.----...",
]

wall_rects = [
    pygame.Rect(0, 0, screen_width, 60), #topwall
    pygame.Rect(0, 0, 20, screen_height), #leftwall
    pygame.Rect((screen_width-18), 0, 50, screen_height), #rightwall
    pygame.Rect(0, (screen_height-15), screen_width, 20), #bottomwall
]

# Function to draw the background based on the input string
def draw_background(window, background_data, sprite_mapping, sprite_sheet_map):
    for y, row in enumerate(background_data):
        for x, char in enumerate(row):
            if char in sprite_mapping:
                sprite_x, sprite_y = sprite_mapping[char]
                window.blit(sprite_sheet_map, (x * SPRITE_WIDTH, y * SPRITE_HEIGHT), (sprite_x, sprite_y, SPRITE_WIDTH, SPRITE_HEIGHT))

def draw_maze(window, maze_map):
    for y, row in enumerate(maze_map):
        for x, char in enumerate(row):
            vertical = pygame.Rect((80+60*x),72*y,5,75)
            horizontal = pygame.Rect((20+60*x),72*y,65,5)
            if char == '|':
                wall_rects.append(vertical)
            if char == '-':
                wall_rects.append(horizontal)


