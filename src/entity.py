from enum import Enum

from position import Position
from block import Block, Entity


class Move(Enum):
	up, down, right, left, done, none = range(6)


class Entity(object):
	def __init__(self, pos_row=0, pos_col=0, icon=Entity.player):
		"""
		Contain pos, representation, and direction
		"""
		self.pos = Position(pos_row, pos_col)
		self.icon = icon
		self.prev_icon = Block.empty
		self.moved = Move.none

	def move(self, direction):
		"""
		Base on Move type, use position to move in correct direction
		"""
		if direction == Move.up:
			self.pos.move_up()
		elif direction == Move.down:
			self.pos.move_down()
		elif direction == Move.left:
			self.pos.move_left()
		elif direction == Move.right:
			self.pos.move_right()

		self.moved = direction
