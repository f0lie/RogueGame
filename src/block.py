from enum import Enum


class Block(Enum):
	"""
	Enum that represents blocks on the map
	"""
	wall, space, empty, error = range(4)


class Entity(Enum):
	"""
	Enum that represents entities on the map
	"""
	player = 0
