from unittest import TestCase

from position import Position
from orient import Orientation


class TestPosition(TestCase):
	def test_compare(self):
		pos = Position(5, 5)

		pos_top = Position(4, 5)
		pos_bottom = Position(6, 5)
		pos_right = Position(5, 6)
		pos_left = Position(5, 4)

		pos_tests = [pos_left, pos_right, pos_bottom, pos_top]

		self.assertEquals(pos.compare(pos_top), Orientation.top)
		self.assertEquals(pos.compare(pos_bottom), Orientation.bottom)
		self.assertEquals(pos.compare(pos_left), Orientation.left)
		self.assertEquals(pos.compare(pos_right), Orientation.right)

		for pos_case in pos_tests:
			self.assertEquals(pos.distance(pos_case), 1)