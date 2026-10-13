import pytest

from game.board import Board


def test_board_defaults_to_nine():
    board = Board()
    assert board.size == 9


def test_pawn_coordinates():
    board = Board()

    assert board.in_bounds(0, 0)
    assert board.in_bounds(8, 8)
    assert not board.in_bounds(9, 8)
    assert not board.in_bounds(-1, 0)


def test_wall_anchor_must_fit():
    board = Board()

    assert board.valid_wall_position(0, 0)
    assert board.valid_wall_position(7, 7)
    assert not board.valid_wall_position(8, 7)
    assert not board.valid_wall_position(7, 8)


def test_place_wall():
    board = Board()

    assert board.place_wall(2, 3, "horizontal")
    assert (2, 3) in board.horizontal_walls

    assert not board.place_wall(2, 3, "horizontal")


def test_crossing_walls_rejected():
    board = Board()

    assert board.place_wall(3, 4, "horizontal")
    assert not board.place_wall(3, 4, "vertical")


def test_invalid_orientation():
    board = Board()

    assert not board.place_wall(2, 3, "diagonal")


def test_invalid_board_size():
    with pytest.raises(ValueError):
        Board(size=1)