from block import Block, Entity
from input import Move


def bound(func):
	"""
	Decorator to put an entity within the bounds of the map.
	Requires an entity and instance of GameMap.
	"""

	def check(self, entity):
		if entity.pos.x < 0:
			entity.pos.x = 0

		if entity.pos.y < 0:
			entity.pos.y = 0

		if entity.pos.x > self.cols - 1:
			entity.pos.x = self.cols - 1

		if entity.pos.y > self.rows - 1:
			entity.pos.y = self.rows - 1

		func(self, entity)

	return check


def collision(func):
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
	def __init__(self, rows=1, cols=1):
		self.map = [[Block.space for col in range(cols)] for row in range(rows)]
		self.rows = rows
		self.cols = cols
		self.room_list = []

	@bound
	@collision
	def put_entity(self, entity):
		"""
		Takes an entity object and uses its pos_y and pos_x to place it on the map with its icon

		:param entity: The entity object to be read
		"""
		self.map[entity.pos.y][entity.pos.x] = entity.icon

	def put_room(self, room):
		self.room_list.append(room)

		for row in range(room.rows):
			for col in range(room.cols):
				if(row == 0 or row == room.rows-1 or
				   col == 0 or col == room.cols-1):
					self.set(room.pos_1.y+row, room.pos_1.x+col, Block.wall)
				else:
					self.set(room.pos_1.y+row, room.pos_1.x+col, Block.empty)

	def flush(self):
		for row in range(self.rows):
			for col in range(self.cols):
				block = self.map[row][col]
				if block == Entity.player:
					self.set(row, col, Block.space)
				elif (block != Block.wall and
					block != Block.empty and
					block != Block.space):
					self.set(row, col, Block.empty)

	def get(self, row, col):
		return self.map[row][col]

	def set(self, row, col, icon):
		self.map[row][col] = icon
