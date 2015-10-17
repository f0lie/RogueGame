from enum import Enum
from random import randint

from orient import Orientation
from position import Position


class TunnelType(Enum):
	none, horizontal, vertical = range(3)


class Tunnel(object):
	def __init__(self, pos_row, pos_col, length=1, orient=Orientation.right):
		self.pos = Position(pos_row, pos_col)
		self.length = length
		self.orient = orient

		if orient == Orientation.right or orient == Orientation.left:
			self.type = TunnelType.horizontal
		elif orient == Orientation.top or orient == Orientation.bottom:
			self.type = TunnelType.vertical
		else:
			self.type = TunnelType.none
			raise AttributeError

	@classmethod
	def from_pos(cls, pos_1, pos_2):
		orient = pos_1.compare(pos_2)
		if orient != Orientation.none:
			length = pos_1.distance(pos_2)
		else:
			raise AttributeError
		return cls(pos_1.row, pos_1.col, length, orient)

	@classmethod
	def create_vertical(cls, pos_1, pos_2):
		"""
		From pos_1 ignore pos_2's col to create a horizontal line to pos_2's row
		"""
		return cls.from_pos(pos_1, Position(pos_2.row, pos_1.col))

	@classmethod
	def create_horizontal(cls, pos_1, pos_2):
		"""
		From pos_1 ignore pos_2's row to create a vertical to pos_2's col
		"""
		return cls.from_pos(pos_1, Position(pos_1.row, pos_2.col))


class Connection(object):
	def __init__(self, pos_1, pos_2):
		self.tunnels = []
		self.connect(pos_1, pos_2)

	def __iter__(self):
		return iter(self.tunnels)

	def connect(self, pos_1, pos_2):
		if randint(0, 1) == 0:
			self.tunnels.append(Tunnel.create_horizontal(pos_1, pos_2))
			self.tunnels.append(Tunnel.create_vertical(Position(pos_1.row, pos_2.col), pos_2))
		else:
			self.tunnels.append(Tunnel.create_vertical(pos_1, pos_2))
			self.tunnels.append(Tunnel.create_horizontal(Position(pos_2.row, pos_1.col), pos_2))
