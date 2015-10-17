from math import sqrt, pow, floor, fabs

from orient import Orientation


class Position(object):
	def __init__(self, row=0, col=0):
		self._row = row
		self._col = col

	@property
	def row(self):
		return self._row

	@row.setter
	def row(self, value):
		self._row = value

	@property
	def col(self):
		return self._col

	@col.setter
	def col(self, value):
		self._col = value

	@property
	def point(self):
		return self._row, self._col

	@point.setter
	def point(self, value):
		row, col = value
		self._row = row
		self._col = col

	def distance(self, other_pos):
		y = fabs(self._row - other_pos.row)
		x = fabs(self._col - other_pos.col)

		return floor(sqrt(pow(y, 2) + pow(x, 2)))

	def compare(self, other_pos):
		"""
		Returns the relative position of other_pos to the object
		Thus if other_pos is to the right of object then
		you will find other_pos to the right of object
		"""
		if self._row == other_pos.row:
			if self._col < other_pos.col:
				return Orientation.right
			elif self._col > other_pos.col:
				return Orientation.left
			elif self._col == other_pos.col:
				return Orientation.same

		elif self._col == other_pos.col:
			if self._row < other_pos.row:
				return Orientation.bottom
			elif self._row > other_pos.row:
				return Orientation.top
			elif self._row == other_pos.row:
				return Orientation.same

		else:
			# meaning other_pos is diagonal to the object
			return Orientation.none

	def move_up(self):
		self._row -= 1

	def move_down(self):
		self._row += 1

	def move_left(self):
		self._col -= 1

	def move_right(self):
		self._col += 1


class Size(object):
	def __init__(self, rows=1, cols=1):
		self._rows = rows
		self._cols = cols

	@property
	def rows(self):
		return self._rows

	@rows.setter
	def rows(self, value):
		self._rows = value

	@property
	def cols(self):
		return self._cols

	@cols.setter
	def cols(self, value):
		self._col = value

	@property
	def size(self):
		return self._rows, self._cols

	@size.setter
	def size(self, value):
		rows, cols = value
		self._rows = rows
		self._cols = cols
