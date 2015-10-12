from gameinput import MoveKey
import position


class GameEntity(object):
	def __init__(self, pos_y=0, pos_x=0, icon='@'):
		'''
		The object that contains an entity with pos_x and pos_y with an icon to represent it

		:param pos_y: Position on the y axis of the map
		:param pos_x: Position on the x axis of the map
		:param icon: Represents the entity
		'''
		self.pos = position.Position(pos_y, pos_x)
		self.icon = icon

	def move(self, key):
		'''
		Take in keys and move the characters based off it

		:param key: Keys that the method receives
		'''
		if key.name == MoveKey.forward.name:
			self.pos.moveUp()
		elif key.name == MoveKey.backward.name:
			self.pos.moveDown()
		elif key.name == MoveKey.left.name:
			self.pos.moveLeft()
		elif key.name == MoveKey.right.name:
			self.pos.moveRight()
