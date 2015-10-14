from position import Position


class Room(object):
	def __init__(self, pos_y=0, pos_x=0, rows=1, cols=1):
		self.pos = Position(pos_y, pos_x)
		self.rows = rows
		self.cols = cols

	def collision(self, other_room):
		pass
