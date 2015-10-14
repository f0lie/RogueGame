from position import Position


class Room(object):
	def __init__(self, pos_y=0, pos_x=0, rows=1, cols=1):
		self.pos_1 = Position(pos_y, pos_x)
		self.pos_2 = Position(pos_y+rows, pos_x+cols)
		self.rows = rows
		self.cols = cols

	def collision(self, other_room):
		return (self.pos_1.x <= other_room.pos_2.x and self.pos_2.x >= other_room.pos_1.x and
		        self.pos_1.y <= other_room.pos_2.y and self.pos_2.y >= other_room.pos_1.y)
