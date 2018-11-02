import pygame
from pygame.locals import *


def load_sprites():
    """
    Load all player sprites into a list.

    :return:        Pass back list of assets.
    """
    player_up    = pygame.image.load("Assets/Art/BasicBoiUp.PNG")
    player_right = pygame.image.load("Assets/Art/BasicBoiRight.PNG")
    player_down  = pygame.image.load("Assets/Art/BasicBoiDown.PNG")
    player_left  = pygame.image.load("Assets/Art/BasicBoiLeft.PNG")
    player_sprites = [player_up, player_left, player_down, player_right]
    enemy_up     = pygame.image.load("Assets/Art/BadBoiUp.PNG")
    enemy_right  = pygame.image.load("Assets/Art/BadBoiRight.PNG")
    enemy_down   = pygame.image.load("Assets/Art/BadBoiDown.PNG")
    enemy_left   = pygame.image.load("Assets/Art/BadBoiLeft.PNG")
    enemy_sprites = [enemy_up, enemy_left, enemy_down, enemy_right]
    sand_floor           = pygame.image.load("Assets/Art/SandFloor1.PNG")
    sand_wall            = pygame.image.load("Assets/Art/SandWall1.PNG")
    sand_pit             = pygame.image.load("Assets/Art/SandPit.PNG")
    sand_door_up         = pygame.image.load("Assets/Art/SandDoorUp.PNG")
    sand_door_right      = pygame.image.load("Assets/Art/SandDoorRight.PNG")
    sand_door_down       = pygame.image.load("Assets/Art/SandDoorDown.PNG")
    sand_door_left       = pygame.image.load("Assets/Art/SandDoorLeft.PNG")
    environment_sprite = [sand_floor, sand_wall, sand_pit, sand_door_up, sand_door_right, sand_door_down,
                          sand_door_left]

    return player_sprites, enemy_sprites, environment_sprite
