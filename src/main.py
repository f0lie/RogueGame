import curses

import map
import display
from display import Display
import input
import entity

'''
	Screen should be 80x24 like a VT100
	I'll figure out how to deal with different screens or enforce this.
'''


def main(stdscr):
	curses.curs_set(0)
	stdscr.noutrefresh()

	game_input = input.Input(stdscr)

	game_map = map.Map(10, 10)
	game_display = display.DisplayMap(game_map)

	game_gui = display.DisplayHook(game_display, display.Orientation.right, 12, 12)

	for i in range(game_gui.rows - 2):
		game_gui.print('hello', i, 0)

	player = entity.Entity()
	game_map.put_entity(player)

	game_display.refresh_map()
	game_gui.refresh()
	Display.update()

	done = False
	while not done:
		key = game_input.get_move_key()
		player.move(key)

		game_map.flush()

		game_map.put_entity(player)

		game_display.refresh_map()
		Display.update()

		if key == input.Move.done:
			done = True


if __name__ == "__main__":
	curses.wrapper(main)
