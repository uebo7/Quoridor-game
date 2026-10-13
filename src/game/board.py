# Manage playing grid and wall position

class Board:
    def __init__(self, size = 9):
        if size <= 2:
            raise ValueError("size must be greater than 2")
        
        self.size = size 
        self.horizontal_walls = set()
        self.vertical_walls = set()

    def in_bounds(self, row, col):
        return 0 <= row < self.size and 0 <= col < self.size

    # bounds checking
    def valid_wall_position(self, row, col):
        return (0 <= row < self.size - 1
            and 0 <= col < self.size - 1
        )

    def has_wall(self, row, col, orientation):
        if orientation == "horizontal":
            return (row, col) in self.horizontal_walls

        if orientation == "vertical":
            return (row, col) in self.vertical_walls

        raise ValueError("Orientation must be horizontal or vertical")

    # checks for possible problems with placing a wall
    # problems checked: invalid orientation, valid wall position, wall conflicts, player has no walls
    # places corresponding wall at location (row, col)
    def place_wall(self, row, col, orientation):
        if not self.valid_wall_position(row, col):
            return False

        if orientation not in ("horizontal", "vertical"):
            return False

        if self.has_wall(row, col, orientation):
            return False

        if self._wall_conflicts(row, col, orientation):
            return False

        if orientation == "horizontal":
            self.horizontal_walls.add((row, col))
        else:
            self.vertical_walls.add((row, col))

        return True

    # checks for walls that are overlapped
    def _wall_conflicts(self, row, col, orientation):
        if orientation == "horizontal":
            if (row, col - 1) in self.horizontal_walls:
                return True
            if (row, col + 1) in self.horizontal_walls:
                return True

            if (row, col) in self.vertical_walls:
                return True

        else:
            if (row - 1, col) in self.vertical_walls:
                return True
            if (row + 1, col) in self.vertical_walls:
                return True

            if (row, col) in self.horizontal_walls:
                return True

        return False

    
