# Manage playing grid and wall position


class Board:
    def __init__(self, size=9):
        if size <= 2:
            raise ValueError("size must be greater than 2")

        self.size = size
        self.horizontal_walls = set()
        self.vertical_walls = set()

    def in_bounds(self, row, col):
        return 0 <= row < self.size and 0 <= col < self.size

    def valid_wall_position(self, row, col):
        return 0 <= row < self.size - 1 and 0 <= col < self.size - 1

    def has_wall(self, row, col, orientation):
        if orientation == "horizontal":
            return (row, col) in self.horizontal_walls
        if orientation == "vertical":
            return (row, col) in self.vertical_walls
        raise ValueError("Orientation must be horizontal or vertical")

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

    def _wall_conflicts(self, row, col, orientation):
        if orientation == "horizontal":
            for other_row, other_col in self.horizontal_walls:
                if other_row == row and max(other_col, col) < min(other_col + 2, col + 2):
                    return True

            for other_row, other_col in self.vertical_walls:
                if other_row == row and other_col == col:
                    return True

            return False

        for other_row, other_col in self.vertical_walls:
            if other_col == col and max(other_row, row) < min(other_row + 2, row + 2):
                return True

        for other_row, other_col in self.horizontal_walls:
            if other_row == row and other_col == col:
                return True

        return False

    def valid_move(self, start_row, start_col, end_row, end_col):
        if not self.in_bounds(start_row, start_col):
            return False
        if not self.in_bounds(end_row, end_col):
            return False

        if abs(end_row - start_row) + abs(end_col - start_col) != 1:
            return False

        if end_col > start_col:
            return not (
                self.has_wall(start_row, start_col, "vertical")
                or self.has_wall(start_row - 1, start_col, "vertical")
            )
        if end_col < start_col:
            return not (
                self.has_wall(start_row, end_col, "vertical")
                or self.has_wall(start_row - 1, end_col, "vertical")
            )
        if end_row > start_row:
            return not (
                self.has_wall(start_row, start_col, "horizontal")
                or self.has_wall(start_row, start_col - 1, "horizontal")
            )
        if end_row < start_row:
            return not (
                self.has_wall(end_row, start_col, "horizontal")
                or self.has_wall(end_row, start_col - 1, "horizontal")
            )

        return False

    def wall_at(self, row, col, orientation):
        return self.has_wall(row, col, orientation)