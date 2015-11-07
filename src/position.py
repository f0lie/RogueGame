from math import sqrt, pow, floor, fabs

from orient import Orientation


class Position(object):
    __slots__ = ['_row', '_col']

    def __init__(self, row=0, col=0):
        self._row = row
        self._col = col

    def __eq__(self, other_pos):
        return (self.row == other_pos.row and
                self.col == other_pos.col)

    def __str__(self):
        return "({}, {})".format(self.row, self.col)

    @property
    def row(self):
        return self._row

    @row.setter
    def row(self, value):
        if value < 0:
            raise ValueError("Row: {} is below zero".format(value))
        self._row = value

    @property
    def col(self):
        return self._col

    @col.setter
    def col(self, value):
        if value < 0:
            raise ValueError("Col: {} is below zero".format(value))
        self._col = value

    @property
    def point(self):
        return self.row, self.col

    @point.setter
    def point(self, value):
        self.row = value.row
        self.col = value.col

    def distance(self, other_pos):
        y = fabs(self.row - other_pos.row)
        x = fabs(self.col - other_pos.col)

        return floor(sqrt(pow(y, 2) + pow(x, 2)))

    def compare_orient(self, other_pos):
        """
        Returns the relative position of other_pos to the object
        Thus if other_pos is to the right of object then
        you will find other_pos to the right of object
        """
        if self.row == other_pos.row:
            if self.col < other_pos.col:
                return Orientation.right
            elif self.col > other_pos.col:
                return Orientation.left
            elif self.col == other_pos.col:
                return Orientation.same

        elif self.col == other_pos.col:
            if self.row < other_pos.row:
                return Orientation.bottom
            elif self.row > other_pos.row:
                return Orientation.top
            elif self.row == other_pos.row:
                return Orientation.same

        else:
            # meaning other_pos is diagonal to the object
            return Orientation.none

    def move_up(self):
        self.row -= 1

    def move_down(self):
        self.row += 1

    def move_left(self):
        self.col -= 1

    def move_right(self):
        self.col += 1


class Size(object):
    __slots__ = ['_rows', '_cols']

    def __init__(self, rows=1, cols=1):
        self._rows = rows
        self._cols = cols

    @property
    def rows(self):
        return self._rows

    @rows.setter
    def rows(self, value):
        self._rows = value

    @property
    def cols(self):
        return self._cols

    @cols.setter
    def cols(self, value):
        self._cols = value

    @property
    def size(self):
        return self.rows, self.cols

    @size.setter
    def size(self, value):
        rows, cols = value
        self.rows = rows
        self.cols = cols
