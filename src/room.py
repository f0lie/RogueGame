from position import Position
from block import Block


class Room(object):
	def __init__(self, pos_y=0, pos_x=0, rows=1, cols=1, fill=Block.empty,
	             left=Block.wall, right=Block.wall, top=Block.wall, bottom=Block.wall,
	             top_left=Block.wall, top_right=Block.wall, bottom_left=Block.wall, bottom_right=Block.wall):
		self.pos_1 = Position(pos_y, pos_x)
		self.pos_2 = Position(pos_y+rows, pos_x+cols)
		self.rows = rows
		self.cols = cols
		self.fill = fill

		# Specific the block of walls
		self.left = left
		self.right = right
		self.top = top
		self.bottom = bottom

		self.top_left = top_left
		self.top_right = top_right
		self.bottom_left = bottom_left
		self.bottom_right = bottom_right

	def collision(self, other_room):
		return (self.pos_1.col <= other_room.pos_2.x and self.pos_2.col >= other_room.pos_1.x and
		        self.pos_1.row <= other_room.pos_2.y and self.pos_2.row >= other_room.pos_1.y)
