from curses import *

from src import gamemap
from src import gamedisplay
from src import gameinput
from src import gameentity

'''
	Screen should be 80x24 like a VT100
	I'll figure out how to deal with different screens or enforce this.
'''


def main(stdscr):
	curs_set(0)
	stdscr.keypad(True)

	map = gamemap.Gamemap(10, 10)
	display = gamedisplay.GameDisplayMap(stdscr, map, 1, 1)
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
	wrapper(main)
