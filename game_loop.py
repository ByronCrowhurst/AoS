import pygame
import sys


def event_resolve(events_list, entity_list, location_list, array):
    """
    Check events that are true and resolves them.

    :param events_list:         List of possible inputs
                                made by player.
    :param entity_to_update:    List of entities to be
                                updated in render_loop.
    :return:                    Passes a list of entities
                                to be drawn to screen.
    """

    for i in range(len(entity_list)):
        x = entity_list[i].x
        y = entity_list[i].y
        target_x = entity_list[i].target_x
        target_y = entity_list[i].target_y
        moving = entity_list[i].incremental_movement(x, y, target_x, target_y, True)
        if not moving:
            for j in range(4):
                if events_list[j] == True:
                    bools = entity_list[i].collision_detection(location_list[i], array)
            if events_list[0] and bools[0]:
                entity_list[i].target_y -= 44
                location_list[i][1] -= 1
                print("up")
            if events_list[1] and bools[3]:
                entity_list[i].target_x -= 44
                location_list[i][0] -= 1
                print("Left")
            if events_list[2] and bools[2]:
                entity_list[i].target_y += 44
                location_list[i][1] += 1
                print("Down")
            if events_list[3] and bools[1]:
                entity_list[i].target_x += 44
                location_list[i][0] += 1
                print("Right")
        if events_list[4]:
            terminate()
    return entity_list, location_list
        # 0 = w 1 = a 2 = s 3 = d 4 = Quit
        # w = -y a = -x s = +y d = +x


def terminate():
    pygame.quit()
    sys.exit()