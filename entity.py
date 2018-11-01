from consts import *
from itertools import cycle

class Entity:

    def __init__(self, entity_type, sprites, x, y, target_x, target_y):
        self.entity_type = entity_type
        self.sprites = sprites
        self.x = x
        self.y = y
        self.target_x = target_x
        self.target_y = target_y
        self.bottom_x = x + TILE_SIZE
        self.bottom_y = y + TILE_SIZE
        pass

    def convert_entity_type(self, entity_type):
        entity_type_dictionary = {"player": 0, "enemy": 1, "environment": 2}
        sprite_set = entity_type_dictionary[entity_type]
        return sprite_set


    def incremental_movement(self, x, y, target_x, target_y, movement_check):
        if x > target_x:
            if movement_check:
                return True
            else:
                x -= SPEED
        elif x < target_x:
            if movement_check:
                return True
            else:
                x += SPEED

        if y > target_y:
            if movement_check:
                return True
            else:
                y -= SPEED
        elif y < target_y:
            if movement_check:
                return True
            else:
                y += SPEED

        if movement_check:
            return False
        return x, y

    def collision_detection(self, location, array):
        cyc = cycle(([0, -1], [1, 0], [0, 1], [-1, 0]))
        # creates a cycle for getting adjacent tile location in order
        collision_bools = [True, True, True, True]
        for i in range(4):
            mod = next(cyc)
            x_check = location[0] + mod[0]
            y_check = location[1] + mod[1]
            # print(x_check, y_check)
            if array[y_check][x_check] == 1:
                collision_bools[i] = False
        # print(collision_bools)
        # print(location)
        return collision_bools
