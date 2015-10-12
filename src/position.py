class Position(object):
	def __init__(self, y=0, x=0):
		self.y = y
		self.x = x

	def move(self, y, x):
		self.y = y
		self.x = x

	def moveUp(self):
		self.y -= 1

	def moveDown(self):
		self.y += 1

	def moveLeft(self):
		self.x -= 1

	def moveRight(self):
		self.x += 1