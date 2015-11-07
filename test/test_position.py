from unittest import TestCase

from position import Position, Size
from orient import Orientation


class TestPosition(TestCase):
    def test_compare(self):
        pos = Position(5, 5)

        pos_top = Position(4, 5)
        pos_bottom = Position(6, 5)
        pos_right = Position(5, 6)
        pos_left = Position(5, 4)

        pos_tests = [pos_left, pos_right, pos_bottom, pos_top]

        self.assertEquals(pos.compare_orient(pos_top), Orientation.top)
        self.assertEquals(pos.compare_orient(pos_bottom), Orientation.bottom)
        self.assertEquals(pos.compare_orient(pos_left), Orientation.left)
        self.assertEquals(pos.compare_orient(pos_right), Orientation.right)

        for pos_case in pos_tests:
            self.assertEquals(pos.distance(pos_case), 1)

    def test_position_raising(self):
        with self.assertRaises(ValueError):
            Position(-1,-1)

    def test_size_raising(self):
        with self.assertRaises(ValueError):
            Size(-1,-1)
