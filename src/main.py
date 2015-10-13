import curses

import map
import display
import input
import entity

'''
	Screen should be 80x24 like a VT100
	I'll figure out how to deal with different screens or enforce this.
'''


def main(stdscr):
	curses.curs_set(0)
	stdscr.keypad(True)

	game_map = map.Map(5, 5, fill=curses.ACS_BULLET)
	game_display = display.DisplayMap(stdscr, game_map, 7, 7)
	game_input = input.Input(stdscr)
	player = entity.Entity()

	gui_scr = curses.newwin(5, 5)
	display.DisplayGUI(gui_scr, game_display, display.Orientation.right)

	game_map.put_entity(player)

	game_display.refresh_map()

	done = False
	while not done:
		key = game_input.get_move_key()
		player.move(key)

		game_map.flush()

		game_map.put_entity(player)

		game_display.refresh_map()

		if key == input.MoveKey.done:
			done = True


if __name__ == "__main__":
	curses.wrapper(main)
