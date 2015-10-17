from unittest import TestCase

from tunnel import Connection, TunnelType

from position import Position
from orient import Orientation


class TestConnection(TestCase):
	def test_connect(self):
		connect = Connection(Position(0, 0), Position(10, 10))
		tunnel_1 = connect.tunnels[0]
		tunnel_2 = connect.tunnels[1]

		if tunnel_1.type == TunnelType.horizontal:
			self.assertEquals(tunnel_1.type, TunnelType.horizontal)
			self.assertEquals(tunnel_2.type, TunnelType.vertical)

			self.assertEquals(tunnel_1.pos.point, (0, 0))
			self.assertEquals(tunnel_1.length, 10)
			self.assertEquals(tunnel_1.orient, Orientation.right)

			self.assertEquals(tunnel_2.pos.point, (0, 10))
			self.assertEquals(tunnel_2.length, 10)
			self.assertEquals(tunnel_2.orient, Orientation.bottom)

		elif tunnel_1.type == TunnelType.vertical:
			self.assertEquals(tunnel_1.type, TunnelType.vertical)
			self.assertEquals(tunnel_2.type, TunnelType.horizontal)

			self.assertEquals(tunnel_1.pos.point, (0, 0))
			self.assertEquals(tunnel_1.length, 10)
			self.assertEquals(tunnel_1.orient, Orientation.bottom)

			self.assertEquals(tunnel_2.pos.point, (10, 0))
			self.assertEquals(tunnel_2.length, 10)
			self.assertEquals(tunnel_2.orient, Orientation.right)

		else:
			self.fail()
