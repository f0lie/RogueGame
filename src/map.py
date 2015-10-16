from block import Block, Entity
from entity import Move


def bound(func):
	"""
	Decorator to put an entity within the bounds of the map.
	"""

	def check(self, entity):
		if entity.pos.col < 0:
			entity.pos.col = 0

		if entity.pos.row < 0:
			entity.pos.row = 0

		if entity.pos.col > self.cols - 1:
			entity.pos.col = self.cols - 1

		if entity.pos.row > self.rows - 1:
			entity.pos.row = self.rows - 1

		func(self, entity)

	return check


def collision(func):
	'''
	Decorator to check if the entity moved into the pos of a wall and move it back
	'''
	def check(self, entity):
		if self.get(*entity.pos.get_pos()) == Block.wall:
			if entity.moved == Move.up:
				entity.pos.move_down()

			elif entity.moved == Move.down:
				entity.pos.move_up()

			elif entity.moved == Move.left:
				entity.pos.move_right()

			elif entity.moved == Move.right:
				entity.pos.move_left()

		func(self, entity)

	return check


class Map(object):
	def __init__(self, rows=1, cols=1, fill=Block.space):
		self.map = [[fill for col in range(cols)] for row in range(rows)]
		self.rows = rows
		self.cols = cols
		self.fill = fill
		self.room_list = []

	@bound
	@collision
	def put_entity(self, entity):
		"""
		Place entity's icon with its pos
		"""
		self.map[entity.pos.row][entity.pos.col] = entity.icon

	def put_room(self, room):
		'''
		Add room to list and place walls in the correct places
		'''
		self.room_list.append(room)

		for row in range(room.rows):
			for col in range(room.cols):

				if(row == 0 or row == room.rows-1 or
				   col == 0 or col == room.cols-1):
					self.set(room.pos_1.row+row, room.pos_1.col+col, Block.wall)
				else:
					self.set(room.pos_1.row+row, room.pos_1.col+col, room.fill)

				'''
				is broke

				room_row, room_col = room.pos_1.row+row, room.pos_1.col+col

				if row == 0:
					if col == 0:
						self.set(room_row, room_col, room.top_left)
					elif col == room.cols-1:
						self.set(room_row, room_col, room.top_right)
					else:
						self.set(room_row, room_col, Block.error)

				elif row == room.rows-1:
					if col == 0:
						self.set(room_row, room_col, room.bottom_left)
					elif col == room.cols-1:
						self.set(room_row, room_col, room.bottom_right)
					else:
						self.set(room_row, room_col, room.bottom)

				elif col == 0:
					self.set(room_row, room_col, room.left)

				elif col == room.cols-1:
					self.set(room_row, room_col, room.right)

				self.set(room_row, room_col, room.fill)
				'''
	def flush(self):
		'''
		If the block isn't a wall, empty or space, then set it empty
		'''
		for row in range(self.rows):
			for col in range(self.cols):
				block = self.map[row][col]
				if (block != Block.wall and
					block != Block.empty and
					block != Block.space):
					self.set(row, col, Block.empty)

	def get(self, row, col):
		return self.map[row][col]

	def set(self, row, col, icon):
		self.map[row][col] = icon
