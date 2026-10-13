from game.board import Board
from game.pathfinding import has_path_to_goal


def test_empty_board_has_path():
    board = Board(9)

    assert has_path_to_goal(board, (8, 4), 0)


def test_path_exists_around_partial_wall_barrier():
    board = Board(9)

    # A wall does not block the entire board.
    board.horizontal_walls.add((3, 3))

    assert has_path_to_goal(board, (8, 4), 0)


def test_starting_on_goal_row():
    board = Board(9)

    assert has_path_to_goal(board, (0, 4), 0)