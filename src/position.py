class Position(object):
	def __init__(self, row=0, col=0):
		self.row = row
		self.col = col

	def get_pos(self):
		return self.row, self.col

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
		self.cols =cols

	def get_size(self):
		return self.rows, self.cols

	def resize(self, rows, cols):
		self.rows = rows
		self.cols = cols