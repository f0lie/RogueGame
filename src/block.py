from enum import Enum


class Block(Enum):
    """
    Enum that represents blocks on the map
    """
    space, empty, tunnel = range(3)


class Entity(Enum):
    """
    Enum that represents entities on the map
    """
    player = 0


class Room(Enum):
    """
    Enum that represents the type of walls on a room
    """
    left, right, top, bottom,\
        top_left, top_right, bottom_left, bottom_right = range(8)
