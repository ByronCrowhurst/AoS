import pygame
import sys


def event_resolve(events_list, entity_to_update, player_location, array):
    """
    Check events that are true and resolves them.

    :param events_list:         List of possible inputs
                                made by player.
    :param entity_to_update:    List of entities to be
                                updated in render_loop.
    :return:                    Passes a list of entities
                                to be drawn to screen.
    """
    x = []
    y = []
    target_x = []
    target_y = []
    for i in range(len(entity_to_update)):
        x.append(entity_to_update[i].x)
        y.append(entity_to_update[i].y)
        target_x.append(entity_to_update[i].target_x)
        target_y.append(entity_to_update[i].target_y)
        moving = entity_to_update[i].incremental_movement(x, y, target_x, target_y, True)
    if not moving:
        for i in range(4):
            if events_list[i] == True:
                bools = entity_to_update.collision_detection(player_location, array)
        for i in range(len(entity_to_update)):
            if events_list[0] and bools[0]:
                entity_to_update[i].target_y -= 44
                player_location[1] -= 1
                print("up")
            if events_list[1] and bools[3]:
                entity_to_update[i].target_x -= 44
                player_location[0] -= 1
                print("Left")
            if events_list[2] and bools[2]:
                entity_to_update[i].target_y += 44
                player_location[1] += 1
                print("Down")
            if events_list[3] and bools[1]:
                entity_to_update[i].target_x += 44
                player_location[0] += 1
                print("Right")
    if events_list[4]:
        terminate()
    game_state_update = [entity_to_update]
    return game_state_update, player_location
        # 0 = w 1 = a 2 = s 3 = d 4 = Quit
        # w = -y a = -x s = +y d = +x


def terminate():
    pygame.quit()
    sys.exit()