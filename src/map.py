from block import Block, Room, Entity
from entity import Move
from room import RoomList
from position import Size, Position

def bound(func):
	"""
	Decorator to put an entity within the bounds of the map.
	"""

	def check(self, entity):
		if entity.pos.col < 0:
			entity.pos.col = 0

		if entity.pos.row < 0:
			entity.pos.row = 0

		if entity.pos.col > self.size.cols - 1:
			entity.pos.col = self.size.cols - 1

		if entity.pos.row > self.size.rows - 1:
			entity.pos.row = self.size.rows - 1

		func(self, entity)

	return check


def collision(func):
	"""
	Decorator to check if the entity moved into the pos of a wall and move it back
	"""
	def check(self, entity):
		if self.get(*entity.pos.get_pos()) in Room:
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
	def __init__(self, rows=1, cols=1, rooms=1, room_size=Size(10,10), fill=Block.space):
		self.map = [[fill for col in range(cols)] for row in range(rows)]
		self.size = Size(rows, cols)

		self.fill = fill
		self.room_list = RoomList()
		self.room_list.generate(rooms, Position(), Position(rows, cols), Size(5, 5), room_size)
		self.put_room_list()

	@bound
	@collision
	def put_entity(self, entity):
		"""
		Place entity's icon with its pos
		"""
		self.map[entity.pos.row][entity.pos.col] = entity.icon

	def put_room_list(self):
		for room in self.room_list:
			self.put_room(room)

	def put_room(self, room):
		"""
		Add room to map and place walls in the correct places
		"""
		for row in range(room.size.rows):
			for col in range(room.size.cols):
				room_row, room_col = room.pos_1.row+row, room.pos_1.col+col

				if row == 0:
					if col == 0:
						self.set(room_row, room_col, room.top_left)
					elif col == room.size.cols-1:
						self.set(room_row, room_col, room.top_right)
					else:
						self.set(room_row, room_col, room.top)

				elif row == room.size.rows-1:
					if col == 0:
						self.set(room_row, room_col, room.bottom_left)
					elif col == room.size.cols-1:
						self.set(room_row, room_col, room.bottom_right)
					else:
						self.set(room_row, room_col, room.bottom)

				elif col == 0:
					self.set(room_row, room_col, room.left)

				elif col == room.size.cols-1:
					self.set(room_row, room_col, room.right)

				else:
					self.set(room_row, room_col, room.fill)

	def flush(self):
		"""
		If the block isn't a wall, empty or space, then set it empty
		Horribly inefficient as it iterates through the entire map
		"""
		for row in range(self.size.rows):
			for col in range(self.size.cols):
				block = self.map[row][col]
				if (block in Entity):
					self.set(row, col, Block.empty)

	def get(self, row, col):
		return self.map[row][col]

	def set(self, row, col, icon):
		self.map[row][col] = icon
