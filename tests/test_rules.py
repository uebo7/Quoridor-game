from game.game_manager import GameManager


def test_new_game_starts_with_player_one_and_no_winner():
    game = GameManager()

    assert game.current_player is game.players[0]
    assert game.game_over is False
    assert game.winner is None
    assert game.check_winner() is None


def test_valid_move_advances_to_the_other_player():
    game = GameManager()
    first_player = game.current_player

    assert game.move_player(first_player.row - 1, first_player.col)

    assert first_player.get_position() == (7, 4)
    assert game.current_player is game.players[1]


def test_invalid_move_does_not_change_position_or_turn():
    game = GameManager()
    first_player = game.current_player
    original_position = first_player.get_position()

    assert not game.move_player(first_player.row + 1, first_player.col)

    assert first_player.get_position() == original_position
    assert game.current_player is first_player


def test_winning_move_sets_winner_and_ends_game():
    game = GameManager()
    first_player = game.current_player
    first_player.move_to(1, first_player.col)

    assert game.move_player(0, first_player.col)

    assert game.game_over is True
    assert game.winner is first_player
    assert game.current_player is first_player


def test_game_does_not_accept_moves_after_game_over():
    game = GameManager()
    first_player = game.current_player
    first_player.move_to(1, first_player.col)
    assert game.move_player(0, first_player.col)
    winning_position = first_player.get_position()

    assert not game.move_player(0, first_player.col + 1)

    assert first_player.get_position() == winning_position
    assert game.winner is first_player


def test_reset_restores_initial_game_state():
    game = GameManager()
    assert game.move_player(7, 4)
    assert game.place_wall(0, 0, "horizontal")

    game.reset()

    assert game.current_player is game.players[0]
    assert game.players[0].get_position() == (8, 4)
    assert game.players[0].walls == 10
    assert not game.board.horizontal_walls
    assert not game.board.vertical_walls
    assert game.game_over is False
    assert game.winner is None