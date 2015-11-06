import curses

import entity
import input
import map
import display
from display import Display
from orient import Orientation

"""
    Screen should be 80x24 like a VT100
    I'll figure out how to deal with different screens or enforce this.
"""


def main(stdscr):
    curses.curs_set(0)
    stdscr.noutrefresh()

    main_input = input.Input(stdscr)

    main_map = map.Map(100, 100, rooms=20)

    player = entity.Entity(*main_map.room_list[0].center.point)
    main_map.put_entity(player)

    map_display = display.DisplayMapScroll(main_map,
                                           player,
                                           20, 80,
                                           150, 150)

    hook_display = display.DisplayHook(map_display,
                                       Orientation.bottom,
                                       4, 20)
    hook_to_hook_display = display.DisplayHook(hook_display,
                                               Orientation.right,
                                               4, 10)

    map_display.refresh_map()
    hook_display.refresh()
    hook_to_hook_display.refresh()
    Display.update()

    done = False
    while not done:
        key = main_input.get_move_key()
        main_map.erase_entity(player)
        player.move(key)

        main_map.put_entity(player)
        hook_display.print_screen(str(player.pos.point), 0, 0)

        map_display.refresh_map()
        Display.update()

        if key == entity.Move.done:
            done = True


if __name__ == "__main__":
    curses.wrapper(main)
