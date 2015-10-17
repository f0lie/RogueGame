from unittest import TestCase

from orient import Orientation
from position import Position
from tunnel import Tunnel


class TestTunnel(TestCase):
	def test_create_vertical(self):
		pos_1 = Position(5, 5)
		pos_2 = Position(6, 6)

		tunnel = Tunnel.create_vertical(pos_1, pos_2)

		self.assertEquals(tunnel.pos.point, pos_1.point)
		self.assertEquals(tunnel.length, 1)
		self.assertEquals(tunnel.orient, Orientation.bottom)

	def test_create_horizontal(self):
		pos_1 = Position(5, 5)
		pos_2 = Position(7, 7)

		tunnel = Tunnel.create_horizontal(pos_1, pos_2)

		self.assertEquals(tunnel.pos.point, pos_1.point)
		self.assertEquals(tunnel.length, 2)
		self.assertEquals(tunnel.orient, Orientation.right)