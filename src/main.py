import curses

import gamemap
import gamedisplay
import gameinput
import gameentity

'''
	Screen should be 80x24 like a VT100
	I'll figure out how to deal with different screens or enforce this.
'''


def main(stdscr):
	curses.curs_set(0)
	stdscr.keypad(True)

	map = gamemap.Gamemap(15, 15, fill=curses.ACS_BULLET)
	display = gamedisplay.GameDisplayMap(stdscr, map, 5, 5)
	input = gameinput.GameInput(stdscr)
	player = gameentity.GameEntity()

	map.put_entity(player)

	display.refresh_map()

	done = False
	while not done:
		key = input.get_movekey()
		player.move(key)

		map.flush()

		map.put_entity(player)

		display.refresh_map()

		if key == gameinput.MoveKey.done:
			done = True


if __name__ == "__main__":
	curses.wrapper(main)
