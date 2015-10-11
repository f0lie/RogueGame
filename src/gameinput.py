from enum import Enum


class MoveKey(Enum):
	forward = ord('w')
	backward = ord('s')
	left = ord('a')
	right = ord('d')
	done = ord('1')
	none = None


class GameInput(object):
	def __init__(self, stdscr):
		'''
		Uses curses screen to take in input

		:param stdscr: Curses screen to take input
		'''
		self._stdscr = stdscr

	def get_movekey(self):
		input = self._stdscr.getch()

		# Return the MoveKey that matches the input
		for key in MoveKey:
			if input == key.value:
				return key

		# Return none if none matches
		return MoveKey.none
