import curses

import map
import display
from display import Display
import input
import entity
import room

'''
	Screen should be 80x24 like a VT100
	I'll figure out how to deal with different screens or enforce this.
'''


def main(stdscr):
	curses.curs_set(0)
	stdscr.noutrefresh()

	game_input = input.Input(stdscr)

	game_map = map.Map(20, 30)
	game_display = display.DisplayMap(game_map)

	first_room = room.Room(5, 5, 10, 10)
	game_map.put_room(first_room)

	game_gui = display.DisplayHook(game_display, display.Orientation.right, 22, 20)

	player = entity.Entity()
	game_map.put_entity(player)

	game_gui.print(str(player.pos.get_pos()), 0, 0, True)

	game_gui.refresh()
	game_display.refresh_map()
	Display.update()

	done = False
	while not done:
		key = game_input.get_move_key()
		player.move(key)

		game_map.flush()

		game_map.put_entity(player)

		game_gui.print(str(player.pos.get_pos()), 0, 0, True)
		game_gui.refresh()

		game_display.refresh_map()
		Display.update()

		if key == input.Move.done:
			done = True


if __name__ == "__main__":
	curses.wrapper(main)
