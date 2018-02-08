#!/usr/bin/env python3
import tdl


class TdlAdapter:
    def __init__(self, window_title, width, height, fps_limit=20):
        pass

    @staticmethod
    def flush():
        # draw on-screen
        tdl.flush()

    @staticmethod
    def calculate_fov(origin_x, origin_y, is_tile_walkable_callback, algorithm, view_radius, should_light_walls):
        return tdl.map.quickFOV(
            origin_x, origin_y,
            is_tile_walkable_callback,
            fov=algorithm,
            radius=view_radius,
            lightWalls=should_light_walls
        )

    @staticmethod
    def wait_for_input():
        # wait for response
        key = tdl.event.key_wait()
        return key

    @staticmethod
    def get_input():
        """
        Ask for input. If none, returns None.
        """
        keypress = False
        for event in tdl.event.get():
            if event.type == 'KEYDOWN':
                print("KEY DOWN: {0}".format(event))
                return event # contains key pressed
            if event.type == 'MOUSEMOTION':
                print("MOUSE: {0}".format(event))
                return event.cell
    
        if not keypress:
            return None
