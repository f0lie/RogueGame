from enum import Enum

import curses
from curses import panel

import position


class Orientation(Enum):
	none, right, left, top, bottom = range(5)


class Display(object):
	def __init__(self, rows=1, cols=1, pos_y=0, pos_x=0):
		"""
		Object that interacts with curses to display on screen
		"""
		self.pos = position.Position(pos_y, pos_x)

		self._win = curses.newwin(1, 1, pos_y, pos_x)
		self._win.mvwin(*self.pos.get_pos())
		self._win.resize(rows, cols)
		self._win.border()

	def get_height(self):
		return self._win.getmaxyx()[0]

	def get_width(self):
		return self._win.getmaxyx()[1]

	def refresh(self):
		''' Avoid spamming doupdate with regular win.refresh '''
		self._win.noutrefresh()


class DisplayMap(Display):
	def __init__(self, game_map, pos_y=0, pos_x=0):
		self.game_map = game_map
		super().__init__(game_map.height+2, game_map.width+2, pos_y, pos_x)

	def refresh_map(self):
		""" Draw the entire map on the screen and refresh the screen """
		for i, row in enumerate(self.game_map.map):
			self._win.move(i+1, 1)
			for icon in row:
				self._win.addch(icon)
		self.refresh()

class DisplayHook(Display):
	def __init__(self, hook_display, orient=Orientation.none, rows=1, cols=1):
		super().__init__(rows, cols)
		# Where to place the screen in relation to the hooked display
		self.orient = orient
		# Move the screen to the hooked display
		self._orient(hook_display)

	def _orient(self, hook_display):
		if self.orient == Orientation.right or self.orient == Orientation.none:
			self.pos.y = hook_display.pos.y
			self.pos.x = hook_display.pos.x + hook_display.get_width()

		elif self.orient == Orientation.left:
			self.pos.y = hook_display.pos.y
			self.pos.x = hook_display.pos.x - self.get_width()

		elif self.orient == Orientation.bottom:
			self.pos.y = hook_display.pos.y + hook_display.get_height()
			self.pos.x = hook_display.pos.x

		elif self.orient == Orientation.top:
			self.pos.y = hook_display.pos.y - self.get_height()
			self.pos.x = hook_display.pos.x

		self._win.mvwin(*self.pos.get_pos())
