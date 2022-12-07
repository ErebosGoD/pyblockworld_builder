import unittest
from classes import House, Wall, WallWithDoor, WallWithWindow, Roof
from pyblockworld import World

material_list = [
    'default:brick',
    'default:sand',
    'default:stone',
    'default:grass',
    'air'
]


class TestChangeWallMaterialMethod(unittest.TestCase):
    def setUp(self):
        test_world = World()
        player_position = test_world.player_position()
        self.test_house = House(player_position, test_world)
        self.test_house.change_wall_material(material_list[3])

    def test_change_wall_material_right_id(self):
        self.assertEqual(
            self.test_house.wall_back.material_id, material_list[3])
        self.assertEqual(
            self.test_house.wall_front.material_id, material_list[3])
        self.assertEqual(
            self.test_house.wall_left.material_id, material_list[3])
        self.assertEqual(
            self.test_house.wall_right.material_id, material_list[3])

    # def test_change_wall_material_wrong_id(self):
    #   self.assertRaises(Exception, self.test_house.change_wall_material, 2)


if __name__ == "__main__":
    unittest.main()
