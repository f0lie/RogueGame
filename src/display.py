from enum import Enum
import curses

from position import Position, Size
from block import Block, Entity, Room


class Orientation(Enum):
	"""
	Enum for the relative position of a display
	"""
	top, bottom, right, left, none = range(5)


class Display(object):
	def __init__(self, rows=1, cols=1, pos_row=0, pos_col=0):
		"""
		The class that other displays inherit from
		"""
		self._win = curses.newwin(rows, cols, pos_row, pos_col)
		self._win_pos = Position(pos_row, pos_col)
		self._win_size = Size(rows, cols)

		self._win.border()

	def refresh(self):
		"""
		Avoid spamming curses.doupdate with regular win.refresh
		"""
		self._win.noutrefresh()

	@staticmethod
	def update():
		"""
		Make the curses.doupdate method easier to read as Display.update
		"""
		curses.doupdate()


class DisplayMap(Display):
	def __init__(self, map, rows=1, cols=1, pos_row=0, pos_col=0):
		"""
		The class that displays handling the map inherits from
		Contains graphics dict to transform Enum representations to graphics on console
		"""
		self.map = map
		super().__init__(rows, cols, pos_row, pos_col)

		self.graphic = {
			Block.empty: curses.ACS_BULLET,
			Block.space: ord(' '),
			Entity.player: ord('@'),
			Block.error: curses.ACS_CKBOARD,

			Room.left: curses.ACS_VLINE,
			Room.right: curses.ACS_VLINE,
			Room.top: curses.ACS_HLINE,
			Room.bottom: curses.ACS_HLINE,

			Room.top_left: curses.ACS_ULCORNER,
			Room.top_right: curses.ACS_URCORNER,
			Room.bottom_left: curses.ACS_LLCORNER,
			Room.bottom_right: curses.ACS_LRCORNER
		}


class DisplayMapScroll(DisplayMap):
	def __init__(self, map, player, rows=1, cols=1, size_y=100, size_x=100, pos_row=0, pos_col=0):
		"""
		Display that focuses on player to display map
		Allows for maps of huge sizes as only a small portion of the map is displayed at once

		rows, cols is the size of the display
		size_y, size_x is the size of the pad screen map is written on
		"""
		super().__init__(map, rows, cols, pos_row, pos_col)

		self._win_scroll = curses.newpad(size_y, size_x)

		# Sub 2 so scroll doesn't overwrite screen borders
		self._scroll_size = Size(rows - 2, cols - 2)

		self._mid_size = Size(self._scroll_size.rows // 2, self._scroll_size.cols // 2)

		self._player = player

		# Draw main screen borders
		self.refresh()

	def refresh_map(self):
		"""
		Redraws the map and draw only a small portion of the map on the screen relative to the player
		"""
		for row in range(self.map.size.rows):
			for col in range(self.map.size.cols):
				item = self.map.get(row, col)
				# Off set drawing of map with mid_rows and mid_cols so player is in the center
				self._win_scroll.addch(row + self._mid_size.rows,
				                       col + self._mid_size.cols,
				                       self.graphic.get(item, ord('X')))

			# Curses pad uses refresh to move the "focus" of screen, hence ugly code
			# Begin drawing from player's pos
		self._win_scroll.noutrefresh(self._player.pos.row,
		                             self._player.pos.col,
		                             # Draw pad on main screen within the borders
		                             self._win_pos.row + 1,
		                             self._win_pos.col + 1,
		                             # End drawing at before the borders of the specified screen
		                             self._win_pos.row + self._scroll_size.rows,
		                             self._win_pos.col + self._scroll_size.cols)


class DisplayMapBounded(DisplayMap):
	def __init__(self, map, pos_row=0, pos_col=0):
		"""
		Display that represents the map as the same size of the display
		"""
		super().__init__(map, map.size.rows + 2, map.size.cols + 2, pos_row, pos_col)

		self._win_map = self._win.derwin((self._win_size.rows - 2) + 1, self._win_size.cols - 2, 1, 1)
		self._win.noutrefresh()

	def refresh_map(self):
		""" Draw the entire map on the screen and refresh the screen """
		for row in range(self.map.size.rows):
			for col in range(self.map.size.cols):
				item = self.map.get(row, col)
				self._win_map.addch(row, col, self.graphic.get(item, 'X'))

		self._win_map.move(0, 0)
		self._win_map.noutrefresh()


class DisplayHook(Display):
	def __init__(self, hook_display, orient=Orientation.none, rows=1, cols=1):
		"""
		Create a display that is placed relative to another display
		"""
		super().__init__(rows, cols)
		# Where to place the screen in relation to the hooked display
		self.orient = orient
		# Move the screen to the hooked display
		self._orient(hook_display)

		self._win_word = self._win.derwin((rows - 2) + 1, cols - 2, 1, 1)

	def print(self, str, y=None, x=None, clear_line=True):
		# Avoids crashing when the cursor reaches the end of the window
		if self._win_word.getyx()[0] == (self._win_size.rows - 2):
			self._win_word.move(0, 0)

		# Clears the text on the line so it doesn't overlap
		if clear_line:
			self._win_word.move(y, x)
			self._win_word.clrtoeol()

		if y != None or x != None:
			self._win_word.addstr(y, x, str)
		else:
			self._win_word.addstr(str)

		self._win_word.noutrefresh()

	def _orient(self, hook_display):
		"""
		Given the orientation relative to the hook_display, moves the display to orient
		"""
		if self.orient == Orientation.right or self.orient == Orientation.none:
			self._win_pos.row = hook_display._win_pos.row
			self._win_pos.col = hook_display._win_pos.col + hook_display._win_size.cols

		elif self.orient == Orientation.left:
			self._win_pos.row = hook_display._win_pos.row
			self._win_pos.col = hook_display._win_pos.col - self._win_size.cols

		elif self.orient == Orientation.bottom:
			self._win_pos.row = hook_display._win_pos.row + hook_display._win_size.rows
			self._win_pos.col = hook_display._win_pos.col

		elif self.orient == Orientation.top:
			self._win_pos.row = hook_display._win_pos.row - self._win_size.rows
			self._win_pos.col = hook_display._win_pos.col

		self._win.mvwin(*self._win_pos.get_pos())
