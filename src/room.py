from random import randint

from position import Position, Size
from block import Room, Block


class Room(object):
    def __init__(self, pos_row=0, pos_col=0, rows=1, cols=1, fill=Block.empty,
                 left=Room.left, right=Room.right,
                 top=Room.top, bottom=Room.bottom,
                 top_left=Room.top_left, top_right=Room.top_right,
                 bottom_left=Room.bottom_left, bottom_right=Room.bottom_right):
        self.pos = Position(pos_row, pos_col)
        self.center = Position(pos_row + (rows // 2), pos_col + (cols // 2))
        self.size = Size(rows, cols)
        self.fill = fill

        # Specific the block of walls
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom

        self.top_left = top_left
        self.top_right = top_right
        self.bottom_left = bottom_left
        self.bottom_right = bottom_right

    @classmethod
    def from_objects(cls, pos, size, **kwargs):
        return cls(pos.row, pos.col, size.rows, size.cols, **kwargs)

    def collision(self, other_room):
        """
        Checks if two rooms intersect each other
        The logic is clearer as a one dimension line
        """
        pos_2 = Position(self.pos.row + self.size.rows,
                         self.pos.col + self.size.cols)
        other_room_pos_2 = Position(other_room.pos.row + other_room.size.rows,
                                    other_room.pos.col + other_room.size.cols)

        return (self.pos.col <= other_room_pos_2.col and
                pos_2.col >= other_room.pos.col and
                self.pos.row <= other_room_pos_2.row and
                pos_2.row >= other_room.pos.row)

    @classmethod
    def generate(cls, min_pos, max_pos, min_size, max_size):
        """
        Create room from min_size to max_size between min_pos and max_pos
        """
        size = Size(randint(min_size.rows, max_size.rows),
                    randint(min_size.cols, max_size.cols))
        pos = Position(randint(min_pos.row, max_pos.row - size.rows),
                       randint(min_pos.col, max_pos.col - size.cols))
        return cls.from_objects(pos, size)


class RoomList():
    def __init__(self):
        self._room_list = []

    def __iter__(self):
        return iter(self._room_list)

    def __getitem__(self, key):
        return self._room_list[key]

    def __len__(self):
        return len(self._room_list)

    def append(self, room):
        self._room_list.append(room)

    def generate(self, num, min_pos, max_pos, min_size, max_size):
        """
        Given a number of rooms, generate rooms that don't intersect
        """
        for i in range(num):
            room = Room.generate(min_pos, max_pos, min_size, max_size)
            while self.is_collision(room):
                room = Room.generate(min_pos, max_pos, min_size, max_size)
            self.append(room)

    def is_collision(self, room):
        """
        Iterate through the list of rooms to test for collisions
        """
        for other_room in self:
            if other_room.collision(room):
                return True
        return False
