from enum import Enum
import curses

import position
from block import Block, Entity


class Orientation(Enum):
	top, bottom, right, left, none = range(5)


class Display(object):
	def __init__(self, rows=1, cols=1, pos_y=0, pos_x=0):
		"""
		Object that interacts with curses to display on screen
		"""
		self.pos = position.Position(pos_y, pos_x)

		self._win = curses.newwin(rows, cols, pos_y, pos_x)
		self._win.border()

		self.rows, self.cols = rows, cols

	def refresh(self):
		''' Avoid spamming doupdate with regular win.refresh '''
		self._win.noutrefresh()

	@staticmethod
	def update():
		curses.doupdate()


class DisplayMap(Display):
	def __init__(self, game_map, pos_y=0, pos_x=0):
		self.game_map = game_map
		super().__init__(game_map.rows + 2, game_map.cols + 2, pos_y, pos_x)

		self._win_map = self._win.subwin((self.rows - 2) + 1, self.cols - 2,
		                                 pos_y + 1, pos_x + 1)
		self._win.noutrefresh()

		self.graphic = {
			Block.empty: curses.ACS_BULLET,
			Entity.player: ord('@')
		}

	def refresh_map(self):
		""" Draw the entire map on the screen and refresh the screen """
		for row in range(self.game_map.rows):
			for col in range(self.game_map.cols):
				item = self.game_map.get(row, col)
				self._win_map.addch(row, col, self.graphic.get(item, 'X'))

		self._win_map.noutrefresh()


class DisplayHook(Display):
	def __init__(self, hook_display, orient=Orientation.none, rows=1, cols=1):
		super().__init__(rows, cols)
		# Where to place the screen in relation to the hooked display
		self.orient = orient
		# Move the screen to the hooked display
		self._orient(hook_display)

		self._win_word = self._win.subwin((rows - 2) + 1, cols - 2,
		                                  self.pos.y + 1, self.pos.x + 1)

	def print(self, str, y=None, x=None):
		if y != None or x != None:
			self._win_word.addstr(y, x, str)
		else:
			self._win_word.addstr(str)

	def _orient(self, hook_display):
		if self.orient == Orientation.right or self.orient == Orientation.none:
			self.pos.y = hook_display.pos.y
			self.pos.x = hook_display.pos.x + hook_display.cols

		elif self.orient == Orientation.left:
			self.pos.y = hook_display.pos.y
			self.pos.x = hook_display.pos.x - self.cols

		elif self.orient == Orientation.bottom:
			self.pos.y = hook_display.pos.y + hook_display.rows
			self.pos.x = hook_display.pos.x

		elif self.orient == Orientation.top:
			self.pos.y = hook_display.pos.y - self.rows
			self.pos.x = hook_display.pos.x

		self._win.mvwin(*self.pos.get_pos())
