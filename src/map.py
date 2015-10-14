from block import Block
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

		if entity.pos.x > self.cols-1:
			entity.pos.x = self.cols-1

		if entity.pos.y > self.rows-1:
			entity.pos.y = self.rows-1

		func(self, entity)

	return check

def collision(func):
	def check(self, entity):
		if self.get(*entity.pos.get_pos()) == Block.wall:
			if self.entity.moved == Move.up:
				self.entity.pos.move_down()

			elif self.entity.moved == Move.down:
				self.entity.pos.mose_up()

			elif self.entity.moved == Move.left:
				self.entity.pos.move_right()

			elif self.entity.pos.moved == Move.right:
				self.entity.pos.move_left()

		func(self, entity)

	return check

class Map(object):
	def __init__(self, rows=1, cols=1):
		self.fill = Block.empty
		self.map = [[self.fill for col in range(cols)] for row in range(rows)]
		self.rows = rows
		self.cols = cols

	def put_icon(self, row, col, icon):
		self.map[row, col] = icon

	@bound
	@collision
	def put_entity(self, entity):
		"""
		Takes an entity object and uses its pos_y and pos_x to place it on the map with its icon

		:param entity: The entity object to be read
		"""
		self.map[entity.pos.y][entity.pos.x] = entity.icon

	def flush(self):
		for row in range(self.rows):
			for col in range(self.cols):
				self.map[row][col] = self.fill

	def get(self, row, col):
		return self.map[row][col]
