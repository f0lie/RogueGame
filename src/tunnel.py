from enum import Enum
from random import randint

from orient import Orientation
from position import Position


class TunnelType(Enum):
    none, horizontal, vertical = range(3)


class Tunnel(object):
    def __init__(self, pos_row, pos_col, length=1, orient=Orientation.right):
        self.pos = Position(pos_row, pos_col)
        self.length = length
        self.orient = orient

        if orient == Orientation.right or orient == Orientation.left:
            self.type = TunnelType.horizontal
        elif orient == Orientation.top or orient == Orientation.bottom:
            self.type = TunnelType.vertical

    def steps(self):
        """
        Gives the positions the vector of tunnel intersects with
        """
        positions = []

        if self.orient == Orientation.top:
            for num in range(self.length):
                positions.append(Position(self.pos.row - num, self.pos.col))

        elif self.orient == Orientation.bottom:
            for num in range(self.length):
                positions.append(Position(self.pos.row + num, self.pos.col))

        elif self.orient == Orientation.right:
            for num in range(self.length):
                positions.append(Position(self.pos.row, self.pos.col + num))

        elif self.orient == Orientation.left:
            for num in range(self.length):
                positions.append(Position(self.pos.row, self.pos.col - num))

        return positions

    @classmethod
    def from_pos(cls, pos_1, pos_2):
        """
        Return a tunnel given two positions
        """
        orient = pos_1.compare_orient(pos_2)
        if orient == Orientation.none:
            raise AttributeError
        else:
            length = pos_1.distance(pos_2)
        return cls(pos_1.row, pos_1.col, length, orient)

    @classmethod
    def create_vertical(cls, pos_1, pos_2):
        """
        From pos_1's row create a horizontal tunnel to pos_2's row
        """
        return cls.from_pos(pos_1, Position(pos_2.row, pos_1.col))

    @classmethod
    def create_horizontal(cls, pos_1, pos_2):
        """
        From pos_1's col create a vertical tunnel to pos_2's col
        """
        return cls.from_pos(pos_1, Position(pos_1.row, pos_2.col))


class Connection(object):
    def __init__(self, pos_1, pos_2):
        self.tunnels = []
        self._connect(pos_1, pos_2)

    def __iter__(self):
        return iter(self.tunnels)

    def _connect(self, pos_1, pos_2):
        """
        Append two tunnels that go horizontal and vertical or the other way
        """
        if randint(0, 1) == 0:
            self.tunnels.append(Tunnel.create_horizontal(pos_1, pos_2))
            self.tunnels.append(Tunnel.create_vertical(Position(pos_1.row,
                                                                pos_2.col),
                                                       pos_2))
        else:
            self.tunnels.append(Tunnel.create_vertical(pos_1, pos_2))
            self.tunnels.append(Tunnel.create_horizontal(Position(pos_2.row,
                                                                  pos_1.col),
                                                         pos_2))
