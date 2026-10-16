from game.board import Board


def test_adjacent_unblocked_moves_are_legal_in_all_directions():
    board = Board()

    assert board.valid_move(4, 4, 3, 4)
    assert board.valid_move(4, 4, 5, 4)
    assert board.valid_move(4, 4, 4, 3)
    assert board.valid_move(4, 4, 4, 5)


def test_move_must_be_adjacent_and_orthogonal():
    board = Board()

    assert not board.valid_move(4, 4, 4, 4)
    assert not board.valid_move(4, 4, 6, 4)
    assert not board.valid_move(4, 4, 5, 5)


def test_moves_cannot_leave_board():
    board = Board()

    assert not board.valid_move(0, 4, -1, 4)
    assert not board.valid_move(8, 4, 9, 4)
    assert not board.valid_move(4, 0, 4, -1)
    assert not board.valid_move(4, 8, 4, 9)


def test_horizontal_wall_blocks_crossing_in_both_directions():
    board = Board()
    assert board.place_wall(3, 3, "horizontal")

    assert not board.valid_move(3, 3, 4, 3)
    assert not board.valid_move(4, 3, 3, 3)
    assert not board.valid_move(3, 4, 4, 4)
    assert not board.valid_move(4, 4, 3, 4)


def test_vertical_wall_blocks_crossing_in_both_directions():
    board = Board()
    assert board.place_wall(3, 3, "vertical")

    assert not board.valid_move(3, 3, 3, 4)
    assert not board.valid_move(3, 4, 3, 3)
    assert not board.valid_move(4, 3, 4, 4)
    assert not board.valid_move(4, 4, 4, 3)