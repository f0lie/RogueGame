from math import sqrt, pow, floor, fabs

from orient import Orientation


class Position(object):
	def __init__(self, row=0, col=0):
		self.row = row
		self.col = col

	def get_pos(self):
		return self.row, self.col

	def distance(self, other_pos):
		y = fabs(self.row - other_pos.row)
		x = fabs(self.col - other_pos.col)

		return floor(sqrt(pow(y, 2) + pow(x, 2)))

	def compare(self, other_pos):
		"""
		Returns the relative position of other_pos to the object
		Thus if other_pos is to the right of object then
		you will find other_pos to the right of object
		"""
		if self.row == other_pos.row:
			if self.col < other_pos.col:
				return Orientation.right
			elif self.col > other_pos.col:
				return Orientation.left
			elif self.col == other_pos.col:
				return Orientation.same

		elif self.col == other_pos.col:
			if self.row < other_pos.row:
				return Orientation.bottom
			elif self.row > other_pos.row:
				return Orientation.top
			elif self.row == other_pos.row:
				return Orientation.same

		else:
			# meaning other_pos is diagonal to the object
			return Orientation.none

	def move(self, row, col):
		self.row = row
		self.col = col

	def move_up(self):
		self.row -= 1

	def move_down(self):
		self.row += 1

	def move_left(self):
		self.col -= 1

	def move_right(self):
		self.col += 1


class Size(object):
	def __init__(self, rows=1, cols=1):
		self.rows = rows
		self.cols = cols

	def get_size(self):
		return self.rows, self.cols

	def resize(self, rows, cols):
		self.rows = rows
		self.cols = cols
