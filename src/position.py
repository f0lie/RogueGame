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
