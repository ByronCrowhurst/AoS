import pygame
from consts import *


def display_update(DISPLAY_SURFACE, FPS_CLOCK, game_state_list):
    """
    Update the screen to display any changes.

    :param DISPLAY_SURFACE:         Surface to be drawn onto
    :param FPS_CLOCK:               Clock object to track FPS
    :param game_state_list:         List of states to be updated
                                    on screen.
    :return:                        Nothing.
    """
    DISPLAY_SURFACE.blit(pygame.image.load("Assets/Art/screen.png"), (0, 0))
    for i in range(len(game_state_list)):
        object_to_blit = game_state_list[i]
        x = object_to_blit[i].x
        y = object_to_blit[i].y
        target_x = object_to_blit[i].target_x
        target_y = object_to_blit[i].target_y
        object_to_blit[i].x, object_to_blit[i].y = object_to_blit[i].incremental_movement(x, y, target_x, target_y, False)
        DISPLAY_SURFACE.blit(object_to_blit[i].sprites[0], (object_to_blit[i].x, object_to_blit[i].y))
        pygame.display.flip()
        FPS_CLOCK.tick(FPS)
        return (target_y / 44, target_x / 44)
