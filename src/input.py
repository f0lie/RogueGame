from config import keys
from entity import Move


class Input(object):
    def __init__(self, scr):
        """
        Uses curses screen to take in input
        """
        self.scr = scr

    def get_move_key(self):
        input_move = chr(self.scr.getch())

        # From config.py, return the correct move type
        for key, value in keys.items():
            if value == input_move:
                return Move.__members__.get(key, Move.none)
