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


def test_path_exists_when_walls_leave_a_route_around():
    board = Board(9)
    for col in (0, 2, 4, 6):
        assert board.place_wall(3, col, "horizontal")

    assert has_path_to_goal(board, (8, 4), 0)


def test_full_wall_barrier_leaves_no_path_to_goal():
    board = Board(9)
    board.horizontal_walls.update((3, col) for col in range(board.size - 1))

    assert not has_path_to_goal(board, (8, 4), 0)


def test_pathfinding_rejects_a_start_outside_the_board():
    board = Board(9)

    assert not has_path_to_goal(board, (9, 4), 0)