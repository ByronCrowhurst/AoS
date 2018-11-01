import pygame, random
from pygame.locals import *


def get_events(events_list):
    """
    Check each possible event in the game in order to be resolved in the game loop.

    :param events_list:         List of each possible event in game.
    :return:                    Returns event list to be passed to game loop.
    """
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_w:
                events_list[0] = True
            elif event.key == K_a:
                events_list[1] = True
            elif event.key == K_s:
                events_list[2] = True
            elif event.key == K_d:
                events_list[3] = True
        elif event.type == QUIT:
            events_list[4] = True
    return events_list
    # 0 = w 1 = a 2 = s 3 = d 4 = Quit
