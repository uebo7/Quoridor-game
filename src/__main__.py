# run game loop

# tests
from game.game_manager import GameManager

game = GameManager()

print("Board size:", game.board.size)
print("Current player:", game.current_player.color)
print("Player positions:", [
    player.get_position() for player in game.players
])

game.next_turn()
print("Next player:", game.current_player.color)