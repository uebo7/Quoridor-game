# controls for:
# player turn
# player action
# victory conditions

from game.player import Player
from game.board import Board
from config import BOARD_SIZE, PLAYER_COLORS

class GameManager:
    def __init__(self): 
        self.board = Board(BOARD_SIZE)
        self.players = [Player(BOARD_SIZE - 1, BOARD_SIZE // 2,
        PLAYER_COLORS["player1"], 0), Player(0, BOARD_SIZE // 2, PLAYER_COLORS["player2"], BOARD_SIZE - 1),]

        self.current_player_index = 0 
        self.game_over = False

    @property 
    def current_player(self):
        return self.players[self.current_player_index]

    def next_turn(self):
        if not self.game_over:
            self.current_player_index = 1
            self.current_player_index

    def check_winner(self):
        for player in self.players:
            if player.has_won():
                self.game_over = True
                return player
            return None