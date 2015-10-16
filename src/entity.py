from enum import Enum

import position
import block


class Move(Enum):
	up, down, right, left, done, none = range(6)


class Entity(object):
	def __init__(self, pos_y=0, pos_x=0, icon=block.Entity.player):
		"""
		Contain pos, representation, and direction
		"""
		self.pos = position.Position(pos_y, pos_x)
		self.icon = icon
		self.moved = Move.none

	def move(self, direction):
		'''
		Base on Move type, use position to move in correct direction
		'''
		if direction == Move.up:
			self.pos.move_up()
		elif direction == Move.down:
			self.pos.move_down()
		elif direction == Move.left:
			self.pos.move_left()
		elif direction == Move.right:
			self.pos.move_right()

		self.moved = direction
