# BFS to make sure players can reach end goal

from collections import deque

# returns true if the player is blocked from reaching the goal
def is_movement_blocked(board, start, end):
    row, col = start
    next_row, next_col = end

    if not board.in_bounds(next_row, next_col):
        return True

    if row == next_row:
        wall_col = min(col, next_col)

        # A vertical wall blocks this edge.
        return (row, wall_col) in board.vertical_walls or (
            row - 1, wall_col
        ) in board.vertical_walls

    if col == next_col:
        wall_row = min(row, next_row)

        # A horizontal wall blocks this edge.
        return (wall_row, col) in board.horizontal_walls or (
            wall_row, col - 1
        ) in board.horizontal_walls

    return True


def has_path_to_goal(board, start, goal_row):
    if not board.in_bounds(*start) or not 0 <= goal_row < board.size:
        return False

    queue = deque([start])
    visited = {start}

    while queue:
        row, col = queue.popleft()

        if row == goal_row:
            return True

        neighbors = [
            (row - 1, col),
            (row + 1, col),
            (row, col - 1),
            (row, col + 1),
        ]

        for neighbor in neighbors:
            if neighbor in visited:
                continue

            if not board.in_bounds(*neighbor):
                continue

            if is_movement_blocked(board, (row, col), neighbor):
                continue

            visited.add(neighbor)
            queue.append(neighbor)

    return False