from enum import Enum
from config import keys

class Move(Enum):
	up, down, right, left, done, none = range(6)


class Input(object):
	def __init__(self, scr):
		"""
		Uses curses screen to take in input

		:param scr: Curses screen to take input
		"""
		self.scr = scr

	def get_move_key(self):
		input_move = chr(self.scr.getch())

		for key, value in keys.items():
			if value == input_move:
				for move_key in Move:
					if key == move_key.name:
						return move_key

		return Move.none