import curses

import map
import display
from display import Display
import input
import entity
import room
from display import Orientation
import block

'''
	Screen should be 80x24 like a VT100
	I'll figure out how to deal with different screens or enforce this.
'''


def main(stdscr):
	curses.curs_set(0)
	stdscr.noutrefresh()

	main_input = input.Input(stdscr)

	main_map = map.Map(50, 50)

	player = entity.Entity(22, 22)
	main_map.put_entity(player)

	first_room = room.Room(0, 0, 25, 25)
	sec_room = room.Room(7, 7, 10, 10, block.Block.space)
	main_map.put_room(first_room)
	main_map.put_room(sec_room)

	map_display = display.DisplayMapScroll(main_map, player, 20, 40)

	hook_display = display.DisplayHook(map_display, Orientation.right, 22, 10)

	map_display.refresh_map()
	hook_display.refresh()
	Display.update()

	done = False
	while not done:
		key = main_input.get_move_key()
		player.move(key)

		main_map.flush()
		main_map.put_entity(player)
		hook_display.print(str(player.pos.get_pos()), 0, 0)

		map_display.refresh_map()
		Display.update()

		if key == entity.Move.done:
			done = True


if __name__ == "__main__":
	curses.wrapper(main)
