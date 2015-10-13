from enum import Enum
import position


class Orientation(Enum):
	none, right, left, top, bottom = range(5)


class Display(object):
	def __init__(self, scr, pos_y=0, pos_x=0):
		"""
		Object that interacts with curses to display on screen

		:param scr: The curses object
		:param pos_y: Y position to draw screen
		:param pos_x: X position to draw screen
		"""
		self._scr = scr

		# Resize screen to something small so moving it doesn't crash game
		height, width = scr.getmaxyx()
		self._scr.resize(1, 1)

		self.pos = position.Position(pos_y, pos_x)
		self._scr.mvwin(*self.pos.get_pos())

		# Return screen to old size
		self._scr.resize(height, width)

	def get_height(self):
		return self._scr.getmaxyx()[0]

	def get_width(self):
		return self._scr.getmaxyx()[1]


class DisplayMap(Display):
	def __init__(self, scr, game_map, pos_y=0, pos_x=0):
		super().__init__(scr, pos_y, pos_x)

		self.game_map = game_map

		# Resize screen to fit borders and the game game_map
		self._scr.resize(self.game_map.height + 2, self.game_map.width + 2)
		self._scr.border()

	def refresh_map(self):
		""" Draw the entire map on the screen and refresh the screen """

		# Move the cursor to within the borders of the screen
		self._scr.move(1, 1)
		cursor_y, cursor_x = self._scr.getyx()

		for i, row in enumerate(self.game_map.map):
			for icon in row:
				self._scr.addch(icon)
			# Moved cursor down by one to print top row otherwise the top row is cut off (I don't know why)
			# Move the cursor to the next row at the first col
			self._scr.move(cursor_y + i + 1, cursor_x)

		self._scr.refresh()


class DisplayGUI(Display):
	def __init__(self, scr, hook_display, orient=Orientation.none, fill=ord(' '), pos_y=0, pos_x=0):
		super().__init__(scr, pos_y, pos_x)
		# Where to place the screen in relation to the hooked display
		self.orient = orient
		# Fill empty space
		self.fill = fill

		# Move the screen to the hooked display
		self._orient(hook_display)

		self._scr.border()
		self._scr.refresh()

	def _orient(self, hook_display):
		"""
		Uses orients to figure out where to put the screen

		:param hook_display: The display to attach the screen to
		"""
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

		self._scr.mvwin(*self.pos.get_pos())
