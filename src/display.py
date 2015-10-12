import position

class Display(object):
	def __init__(self, stdscr, pos_y=0, pos_x=0):
		'''
		Object that interacts with curses

		:param stdscr: Curses screen to write on
		:param pos_y: The y position on the screen to begin drawing
		:param pos_x: The x position on the screen to begin drawing
		'''
		self._stdscr = stdscr
		self.pos = position.Position(pos_y, pos_x)

class DisplayMap(Display):
	def __init__(self, stdscr, map, pos_y=0, pos_x=0):
		super().__init__(stdscr, pos_y, pos_x)

		self.game_map = map

		stdscr.resize(self.game_map.height + 2, self.game_map.width + 2)
		stdscr.border()

		self._stdscr.mvwin(self.pos.y, self.pos.x)

	def refresh_map(self):
		''' Draw the entire map on the screen and refresh the screen '''

		# Move the cursor to within the borders of the screen
		self._stdscr.move(1, 1)
		cursor_y, cursor_x = self._stdscr.getyx()

		for i, row in enumerate(self.game_map.map):
			for icon in row:
				self._stdscr.addch(icon)
			# Moved cursor down by one to print top row otherwise the top row is cut off (I don't know why)
			# Move the cursor to the next row at the first col
			self._stdscr.move(cursor_y + i + 1, cursor_x)

		self._stdscr.refresh()