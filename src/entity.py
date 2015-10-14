from input import Move
import position
import block


class Entity(object):
	def __init__(self, pos_y=0, pos_x=0, icon=block.Entity.player):
		"""
		The object that contains an entity with pos_x and pos_y with an icon to represent it

		:param pos_y: Position on the y axis of the map
		:param pos_x: Position on the x axis of the map
		:param icon: Represents the entity
		"""
		self.pos = position.Position(pos_y, pos_x)
		self.icon = icon
		self.moved = Move.none

	def move(self, direction):
		if direction == Move.up:
			self.pos.move_up()
		elif direction == Move.down:
			self.pos.move_down()
		elif direction == Move.left:
			self.pos.move_left()
		elif direction == Move.right:
			self.pos.move_right()

		self.moved = direction
