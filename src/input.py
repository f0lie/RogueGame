from enum import Enum


class MoveKey(Enum):
	up = ord('w')
	down = ord('s')
	left = ord('a')
	right = ord('d')
	done = ord('1')
	none = None


class Input(object):
	def __init__(self, scr):
		'''
		Uses curses screen to take in input

		:param scr: Curses screen to take input
		'''
		self.scr = scr

	def get_move_key(self):
		input = self.scr.getch()

		# Return the MoveKey that matches the input
		for key in MoveKey:
			if input == key.value:
				return key

		# Return none if none matches
		return MoveKey.none
