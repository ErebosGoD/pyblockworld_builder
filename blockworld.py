from classes import Wall, WallWithDoor, WallWithWindow, Roof, House
from pyblockworld import World
# pylint: skip-file


def build_walls_on_b_press(world):
    try:
        position = world.player_position()
        """ wall = Wall(position, world)
        wall.build()
        wall_rotated = Wall(position, world, rotated=True)
        wall_rotated.build() """
        """ wall_with_door = WallWithDoor(position, world)
        wall_with_door.build()
        wall_with_door_rotated = WallWithDoor(position, world, rotated=True)
        wall_with_door_rotated.build() """
        """ wall_with_window = WallWithWindow(position, world)
        wall_with_window.build()
        wall_with_window_rotated = WallWithWindow(position, world, rotated=True)
        wall_with_window_rotated.build() """
        """ roof = Roof(position, world)
        roof.build() """
        house = House(position, world)
        # house.change_wall_material(2)
        house.build()
    except Exception as exception:
        print("Hello")
        raise exception


world = World()
world.build_key_pressed = build_walls_on_b_press
world.run()
