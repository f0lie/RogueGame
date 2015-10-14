from enum import Enum

class Block(Enum):
	wall, empty = range(2)

class Entity(Enum):
	player = 1