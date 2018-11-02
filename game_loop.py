import pygame
import sys
import random
from consts import *


def event_resolve(events_list, entity_list, location_list, array):
    """
    Check events that are true and resolves them.

    :param events_list:         List of possible inputs
                                made by player.
    :param entity_list:         List of entities to be
                                updated in render_loop.
    :param location_list:       List of locations to
                                blit entities.
    :param array:               Maze array.
    :return:                    Passes a list of entities
                                to be drawn to screen.
    """

    for i in range(len(entity_list)):
        x = entity_list[i].x
        y = entity_list[i].y
        target_x = entity_list[i].target_x
        target_y = entity_list[i].target_y
        current_turn = entity_list[i].current_turn
        moves = entity_list[i].moves
        made_move = entity_list[i].made_move
        moving = entity_list[i].incremental_movement(x, y, target_x, target_y, True)
        if entity_list[i].entity_type == "player" and entity_list[i].current_turn and not moving:
            for j in range(4):
                if events_list[j] == True:
                    bools = entity_list[i].collision_detection(location_list[i], array)
            if events_list[0] and bools[0]:
                entity_list[i].target_y -= TILE_SIZE
                entity_list[i].direction = 0
                location_list[i][1] -= 1
                made_move = True
            elif events_list[1] and bools[3]:
                entity_list[i].target_x -= TILE_SIZE
                location_list[i][0] -= 1
                entity_list[i].direction = 1
                made_move = True
            elif events_list[2] and bools[2]:
                entity_list[i].target_y += TILE_SIZE
                location_list[i][1] += 1
                entity_list[i].direction = 2
                made_move = True
            elif events_list[3] and bools[1]:
                entity_list[i].target_x += TILE_SIZE
                location_list[i][0] += 1
                entity_list[i].direction = 3
                made_move = True
            entity_list[i].turn_order(current_turn, moves, made_move)
        elif entity_list[i].entity_type == "enemy" and not moving:
            # simulate_movement = random.randint(0, 3)
            if entity_list[i].current_turn:
                simulate_move = random.randint(0, 3)
                if simulate_move == 0:
                    entity_list[i].target_y -= TILE_SIZE
                    made_move = True
                elif simulate_move == 1:
                    entity_list[i].target_x -= TILE_SIZE
                    made_move = True
                elif simulate_move == 2:
                    entity_list[i].target_y += TILE_SIZE
                    made_move = True
                elif simulate_move == 3:
                    entity_list[i].target_x += TILE_SIZE
                    made_move = True
            entity_list[i].turn_order(current_turn, moves, made_move)
        change_turns(entity_list)
        if events_list[4]:
            terminate()
    return entity_list, location_list
        # 0 = w 1 = a 2 = s 3 = d 4 = Quit
        # w = -y a = -x s = +y d = +x


def change_turns(entity_list):
    end_of_list = int(len(entity_list))
    for i in range(end_of_list):
        if entity_list[i].current_turn and entity_list[i].moves <= 0:
            entity_list[i].current_turn = False
            next_entity = i+1
            if next_entity == end_of_list:
                next_entity -= end_of_list
            entity_list[next_entity].start_turn()




def terminate():
    pygame.quit()
    sys.exit()
