from input import MoveKey
import position


class Entity(object):
	def __init__(self, pos_y=0, pos_x=0, icon='@'):
		'''
		The object that contains an entity with pos_x and pos_y with an icon to represent it

		:param pos_y: Position on the y axis of the map
		:param pos_x: Position on the x axis of the map
		:param icon: Represents the entity
		'''
		self.pos = position.Position(pos_y, pos_x)
		self.icon = icon
		self.key = MoveKey.none

	def move(self, key):
		'''
		Take in keys and move the characters based off it

		:param key: Keys that the method receives
		'''
		if key == MoveKey.up:
			self.pos.moveUp()
		elif key == MoveKey.down:
			self.pos.moveDown()
		elif key == MoveKey.left:
			self.pos.moveLeft()
		elif key == MoveKey.right:
			self.pos.moveRight()

		self.key = key
