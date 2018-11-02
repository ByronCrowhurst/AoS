import pygame, sys, random, event_loop, game_loop, render_loop, load_assets, display_maze
from consts import *
from entity import *


def main():
    """
    Run the game.

    :return:        Nothing.
    """

    ''' Initialise events, display and clock. '''
    events_list = intialise_events()
    DISPLAY_SURFACE = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    FPS_CLOCK = pygame.time.Clock()


    array, spawn_tile, entity_list, location_list= \
        new_room(0)



    while True:
        ''' Main game loop. '''
        events_list = event_loop.get_events(events_list)
        game_state_list, location_list = game_loop.event_resolve(events_list, entity_list, location_list, array, spawn_tile)
        special_tile = entity_list[0].special_tile_check(location_list[0], array)
        if special_tile ==  "PIT":
            location_list[0][0] = int(spawn_tile[0]/TILE_SIZE)
            location_list[0][1] = int(spawn_tile[1]/TILE_SIZE)
            entity_list[0].x, entity_list[0].target_x = \
                spawn_tile[0], spawn_tile[0]
            entity_list[0].y, entity_list[0].target_y = spawn_tile[1], spawn_tile[1]
        elif special_tile == "TOP DOOR":
            array, spawn_tile, entity_list, location_list = new_room(2)
        elif special_tile == "RIGHT DOOR":
            array, spawn_tile, entity_list, location_list = new_room(3)
        elif special_tile == "BOTTOM DOOR":
            array, spawn_tile, entity_list, location_list = new_room(0)
        elif special_tile == "LEFT DOOR":
            array, spawn_tile, entity_list, location_list = new_room(1)
        render_loop.display_update(DISPLAY_SURFACE, FPS_CLOCK, game_state_list)
        events_list = clear_events(events_list)

def new_room(start_side):
    """
    Function that creates a new room and all required object, for the game to
    run for a single room.

    This function will be called at the start of the game, and upon reaching a
    door to the next room. A new room and new enemies will be generated and the
    player will be moved to the new spawn tile.

    :param start_side:  the side in which the door will be created
    :return:            returns all needed variables for creating a new room
                        from scratch
    """
    ''' Load and convert sprites. '''
    player_sprites, enemy_sprites, environment_sprites = load_assets.load_sprites()
    player_sprites, enemy_sprites, environment_sprites = convert_images(
        player_sprites,
        enemy_sprites,
        environment_sprites
    )
    ''' Initialise maze array. '''
    array = display_maze.display_maze(start_side)
    for x in range(len(array)):
        for y in range(len(array[0])):
            if array[x][y] == 'X':
                spawn_tile = (y * TILE_SIZE, x * TILE_SIZE)
                player_location = [y, x]

    ''' Create player and enemy objects. '''
    player = Entity("player", player_sprites, spawn_tile[0], spawn_tile[1], spawn_tile[0], spawn_tile[1], 0, True,
                    MOVES, False)
    enemy = Entity("enemy", enemy_sprites, 176, 176, 176, 176, 0, False, MOVES, False)
    enemy_location = [int(enemy.y / TILE_SIZE), int(enemy.x / TILE_SIZE)]
    entity_list = [player, enemy]
    location_list = [player_location, enemy_location]

    return array, spawn_tile, entity_list, location_list

def intialise_events():
    """
    Initialise all possible event types.

    :return:        Return a list of events.
    """
    ''' Events created to be checked later. '''
    w_key_press = False
    a_key_press = False
    s_key_press = False
    d_key_press = False
    quit_event = False
    ''' Stores list of events for easy access. '''
    events_list = [w_key_press, a_key_press, s_key_press, d_key_press, quit_event]
    return events_list


def convert_images(player_sprites, enemy_sprites, environment_sprites):
    """
    convert_images simply converts every image in order to correctly work with them.

    :param player_sprites:      List of player sprites.
    :param enemy_sprites:       List of enemy sprites.
    :param environment_spritesa: List of environment sprites.
    :return:                    Returns converted sprites.
    """
    for i in range(len(player_sprites)):
        player_sprites[i].convert()
    for i in range(len(enemy_sprites)):
        enemy_sprites[i].convert()
    for i in range(len(environment_sprites)):
        environment_sprites[i].convert()
    return player_sprites, enemy_sprites, environment_sprites


def clear_events(events_list):
    """
    Change all boolean values to False so that
    the events do not continually trigger.

    :param events_list:         List of events.
    :return:                    Return list of events set to False.
    """
    for i in range(len(events_list)):
        events_list[i] = False
    return events_list

if __name__ == "__main__":
    main()
