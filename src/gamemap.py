def bound(func):
	'''
	Decorator to put an entity within the bounds of the map.
	Requires an entity and instance of GameMap.
	'''

	def check(self, entity):
		if entity.pos.x < 0:
			entity.pos.x = 0

		if entity.pos.y < 0:
			entity.pos.y = 0

		if entity.pos.x > self.width - 1:
			entity.pos.x = self.width - 1

		if entity.pos.y > self.height - 1:
			entity.pos.y = self.height - 1

		return func(self, entity)

	return check


class Gamemap(object):
	def __init__(self, height=10, width=10, fill='-'):
		'''
		The object that contains the map of characters for the game

		:param height: height of the map
		:param width:  width of the map
		:param fill: character representation of empty
		'''
		self.map = [[fill for col in range(width)] for row in range(height)]
		self.height = height
		self.width = width
		self.fill = fill

	def put_icon(self, row, col, icon):
		'''
		Takes row and col parameters and puts a icon on the position

		:param row: row position of icon
		:param col: col position of icon
		:param icon: character to be placed
		'''
		self.map[row][col] = icon

	@bound
	def put_entity(self, entity):
		'''
		Takes an entity object and uses its pos_y and pos_x to place it on the map with its icon

		:param entity: The entity object to be read
		'''
		self.map[entity.pos.y][entity.pos.x] = entity.icon

	def flush(self):
		''' Read entire map and replace any character that isn't empty with empty '''
		for row in range(len(self.map)):
			for col in range(len(self.map[row])):
				if self.map[row][col] != self.fill:
					self.map[row][col] = self.fill
