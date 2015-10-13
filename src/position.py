class Position(object):
	def __init__(self, y=0, x=0):
		self.y = y
		self.x = x

	def get_pos(self):
		return self.y, self.x

	def move(self, y, x):
		self.y = y
		self.x = x

	def move_up(self):
		self.y -= 1

	def move_down(self):
		self.y += 1

	def move_left(self):
		self.x -= 1

	def move_right(self):
		self.x += 1
