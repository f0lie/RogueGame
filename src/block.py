from enum import Enum


class Block(Enum):
	wall, space, empty = range(3)


class Entity(Enum):
	player = range(1)
