ground_level = 1
roof_height = 4

material_list = [
    'default:brick',
    'default:sand',
    'default:stone',
    'default:grass',
    'air'
]


class Wall:
    def __init__(self, pos: tuple, blockworld, material_id="default:stone", rotated=False):
        self.width: int = 6
        self.height: int = 5
        self.pos = pos
        self.rotated = rotated
        self.material_id = material_id
        self._blockworld = blockworld

    def build(self):
        try:
            if self.rotated:
                self._blockworld.setBlocks(
                    self.pos[0], self.pos[1] - ground_level, self.pos[2], self.pos[0], self.pos[1] + self.height - ground_level, (self.pos[2] + self.width)-1, self.material_id)
            else:
                self._blockworld.setBlocks(
                    self.pos[0], self.pos[1] - ground_level, self.pos[2], self.pos[0]+4, self.pos[1] + self.height-ground_level, self.pos[2], self.material_id)
        except Exception as exception:
            raise exception


class WallWithDoor(Wall):
    def __init__(self, pos: tuple, blockworld, rotated=False):
        super().__init__(pos, blockworld)
        self.door_material_id = "air"
        self.rotated = rotated

    def build(self):
        try:
            super().build()
            if self.rotated:

                self._blockworld.setBlocks(
                    self.pos[0], self.pos[1]-ground_level, self.pos[2]+2, self.pos[0], self.pos[1]+2, self.pos[2]+3, self.door_material_id)
            else:
                self._blockworld.setBlocks(
                    self.pos[0]+2, self.pos[1]-ground_level, self.pos[2], self.pos[0]+3, self.pos[1]+2, self.pos[2], self.door_material_id)
        except Exception as exception:
            raise exception


class WallWithWindow(Wall):
    def __init__(self, pos: tuple, blockworld, window_material_id="air", rotated=False):
        super().__init__(pos, blockworld, rotated=True)
        self.window_material_id = window_material_id
        self.rotated = rotated

    def build(self):
        super().build()
        try:
            if self.rotated:

                self._blockworld.setBlocks(
                    self.pos[0], self.pos[1], self.pos[2]+2, self.pos[0], self.pos[1]+2, self.pos[2]+3, self.window_material_id)
            else:
                self._blockworld.setBlocks(
                    self.pos[0]+2, self.pos[1], self.pos[2], self.pos[0]+3, self.pos[1]+2, self.pos[2], self.window_material_id)
        except Exception as exception:
            raise exception


class Roof:
    def __init__(self, pos, blockworld, roof_material_id="default:brick", width=6, depth=6):
        self.width = width
        self.depth = depth
        self.roof_material_id = roof_material_id
        self.pos = pos
        self.__blockworld = blockworld

    def build(self):
        try:
            self.__blockworld.setBlocks(self.pos[0], self.pos[1]+roof_height, self.pos[2],
                                        self.pos[0]+5, self.pos[1]+roof_height, self.pos[2]+5, self.roof_material_id)
        except Exception as exception:
            raise exception


class House(Wall, Roof):
    def __init__(self, pos, blockworld):
        self.pos = pos
        self._blockworld = blockworld
        self.wall_back: Wall = Wall(self.pos, blockworld)
        self.wall_left: Wall = WallWithWindow(
            self.pos, blockworld, rotated=True)
        self.wall_right: Wall = WallWithWindow(
            (self.pos[0]+5, self.pos[1], self.pos[2]), blockworld, rotated=True)
        self.wall_front: Wall = WallWithDoor(
            (self.pos[0], self.pos[1], self.pos[2]+5), blockworld)
        self.roof = Roof(self.pos, blockworld)

    def change_wall_material(self, new_material_id):
        try:

            self.wall_back.material_id = new_material_id
            self.wall_left.material_id = new_material_id
            self.wall_right.material_id = new_material_id
            self.wall_front.material_id = new_material_id

        except Exception as exception:
            raise exception

    def build(self):
        try:
            self.wall.build()
            self.left_wall.build()
            self.right_wall.build()
            self.wall_with_door.build()
            self.roof.build()
        except Exception as exception:
            raise exception
