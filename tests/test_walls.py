from game.board import Board
from game.game_manager import GameManager


def test_wall_requires_a_valid_anchor_and_orientation():
    board = Board()

    assert not board.place_wall(8, 0, "horizontal")
    assert not board.place_wall(0, 8, "vertical")
    assert not board.place_wall(0, 0, "diagonal")
    assert not board.horizontal_walls
    assert not board.vertical_walls


def test_touching_walls_are_allowed_but_overlapping_walls_are_not():
    board = Board()

    assert board.place_wall(2, 1, "horizontal")
    assert board.place_wall(2, 3, "horizontal")
    assert not board.place_wall(2, 2, "horizontal")


def test_perpendicular_walls_may_touch_without_crossing():
    board = Board()

    assert board.place_wall(3, 2, "horizontal")
    assert board.place_wall(2, 3, "vertical")


def test_invalid_wall_placement_does_not_consume_a_wall_or_turn():
    game = GameManager()
    player = game.current_player
    current_index = game.current_player_index

    assert not game.place_wall(8, 8, "horizontal")

    assert player.walls == 10
    assert game.current_player_index == current_index
    assert not game.board.horizontal_walls


def test_valid_wall_placement_consumes_one_wall_and_advances_turn():
    game = GameManager()
    player = game.current_player

    assert game.place_wall(0, 0, "horizontal")

    assert player.walls == 9
    assert game.board.has_wall(0, 0, "horizontal")
    assert game.current_player is game.players[1]


def test_player_without_walls_cannot_place_a_wall():
    game = GameManager()
    player = game.current_player
    player.walls = 0

    assert not game.place_wall(0, 0, "horizontal")
    assert game.current_player is player
    assert not game.board.horizontal_walls