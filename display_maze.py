"""Holds the function to display the maze visually using pygame."""
import pygame
import array_gen
from consts import *
#from pygame.locals import *


def display_maze(start_side):
    """
    Display the maze in pygame.

    Calls array_gen to get a random array for the maze, and using tiledict
    displays all the tiles to the screen once. Then saves the complete screen
    as "screen.png". Also returns the array used.

    :param start_side:       The side the player starts on.
    """
    width = int(WINDOW_WIDTH / 44)
    height = int(WINDOW_HEIGHT / 44)

    pygame.init()
    BLACK = (0, 0, 0)
    surface = pygame.display.set_mode((width*44, height*44))
    tile_dict = {0: "Assets/Art/SandFloor1.png",
                1: "Assets/Art/SandWall1.png",
                2: "Assets/Art/SandPit.png",
                'U': "Assets/Art/SandDoorUp.png",
                'R': "Assets/Art/SandDoorRight.png",
                'D': "Assets/Art/SandDoorDown.png",
                'L': "Assets/Art/SandDoorLeft.png",
                'X': "Assets/Art/SandFloor1.png"}

    maze = array_gen.create_room(width, height, start_side)
    # gives maze size, and spawn location
    for x in range(width):      # for each tile in the maze
        for y in range(height):  # display the appropriate tile
            tile = pygame.image.load(tile_dict[maze[y][x]])
            surface.blit(tile, (x * 44, y * 44))
    pygame.image.save(surface, "Assets/Art/screen.png")  # save as a file
    # saving as its own image might not be necessary, if we use diff surfaces
    return(maze)
