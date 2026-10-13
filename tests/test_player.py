from game.player import Player


def test_player_starts_with_ten_walls():
    player = Player(
        player_id=1,
        position=(0, 4),
        goal_row=8,
    )

    assert player.walls_remaining == 10


def test_player_wins_on_goal_row():
    player = Player(
        player_id=1,
        position=(7, 4),
        goal_row=8,
    )

    assert player.has_won is False

    player.move_to((8, 4))

    assert player.has_won is True


def test_player_cannot_use_more_walls_than_available():
    player = Player(
        player_id=1,
        position=(0, 4),
        goal_row=8,
        walls_remaining=1,
    )

    assert player.use_wall() is True
    assert player.walls_remaining == 0

    assert player.use_wall() is False
    assert player.walls_remaining == 0