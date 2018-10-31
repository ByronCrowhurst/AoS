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
    ''' Load and convert sprites. '''
    player_sprites, enemy_sprites, environment_sprites = load_assets.load_sprites()
    player_sprites, enemy_sprites, environment_sprites = convert_images(
                                                                        player_sprites,
                                                                        enemy_sprites,
                                                                        environment_sprites
                                                                        )
    ''' Initialise maze array. '''
    array = display_maze.display_maze(0)
    for x in range(len(array)):
        for y in range(len(array[0])):
            if array[x][y] == 'X':
                spawn_tile = (y*TILE_SIZE, x*TILE_SIZE)
                player_location = [y, x]
    ''' Create player and enemy objects. '''
    player = Entity("player", player_sprites, spawn_tile[0], spawn_tile[1], spawn_tile[0], spawn_tile[1])
    enemy = Entity("enemy", enemy_sprites, 166, 166, 166, 166)
    enemy_location = [enemy.y/44, enemy.x/44]
    entity_list = [player, enemy]
    location_list = [player_location, enemy_location]
    while True:
        ''' Main game loop. '''
        events_list = event_loop.get_events(events_list, entity_list)
        game_state_list, player_location = game_loop.event_resolve(events_list, entity_list, location_list, array)
        render_loop.display_update(DISPLAY_SURFACE, FPS_CLOCK, game_state_list)
        events_list = clear_events(events_list)


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
    :param environment_sprites: List of environment sprites.
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
