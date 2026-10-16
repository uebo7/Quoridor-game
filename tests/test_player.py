from game.player import Player


def make_player(row=0, col=4, goal_row=8):
    return Player(row, col, "blue", goal_row)


def test_player_starts_with_ten_walls():
    player = make_player()

    assert player.walls == 10


def test_player_position_can_be_read_and_updated():
    player = make_player(row=7)

    assert player.get_position() == (7, 4)

    player.move_to(8, 5)

    assert player.get_position() == (8, 5)


def test_player_wins_on_goal_row():
    player = make_player(row=7)

    assert player.has_won() is False

    player.move_to(8, 4)

    assert player.has_won() is True


def test_player_cannot_use_more_walls_than_available():
    player = make_player()
    player.walls = 1

    assert player.use_wall() is True
    assert player.walls == 0

    assert player.use_wall() is False
    assert player.walls == 0