from enum import Enum


class Orientation(Enum):
	"""
	Enum for the relative position of a display
	"""
	top, bottom, right, left, none = range(5)