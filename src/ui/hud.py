import pygame

from config import BOARD_SIZE, CELL_SIZE


class Hud:
    def __init__(self, game, panel_width=220):
        self.game = game
        self.panel_width = panel_width
        self.font = pygame.font.SysFont(None, 30)
        self.small_font = pygame.font.SysFont(None, 22)

    def draw(self, screen, mode):
        panel_x = BOARD_SIZE * CELL_SIZE
        panel_rect = pygame.Rect(panel_x, 0, self.panel_width, BOARD_SIZE * CELL_SIZE)
        pygame.draw.rect(screen, (30, 30, 30), panel_rect)

        title = self.font.render("Quoridor", True, (255, 255, 255))
        screen.blit(title, (panel_x + 20, 20))

        if self.game.game_over:
            winner_text = f"Winner: {self.game.winner.color.title()}"
            winner_surface = self.font.render(winner_text, True, (255, 220, 120))
            screen.blit(winner_surface, (panel_x + 20, 70))
        else:
            current_name = f"Turn: {self.game.current_player.color.title()}"
            turn_surface = self.font.render(current_name, True, (255, 255, 255))
            screen.blit(turn_surface, (panel_x + 20, 70))

        mode_label = "Mode: Move" if mode == "move" else "Mode: Wall"
        mode_surface = self.small_font.render(mode_label, True, (180, 180, 255))
        screen.blit(mode_surface, (panel_x + 20, 120))

        for index, player in enumerate(self.game.players, start=1):
            y = 180 + (index - 1) * 80
            player_label = self.small_font.render(
                f"P{index}: {player.color.title()}  Walls {player.walls}",
                True,
                self._color(player.color),
            )
            screen.blit(player_label, (panel_x + 20, y))

        instructions = [
            "M = move mode",
            "W = wall mode",
            "R = rotate wall",
            "Arrows/WASD = move",
            "Click = place wall",
            "Q = quit",
        ]

        for i, line in enumerate(instructions):
            text = self.small_font.render(line, True, (220, 220, 220))
            screen.blit(text, (panel_x + 20, 320 + i * 26))

    def _color(self, color_name):
        colors = {
            "blue": (60, 120, 255),
            "red": (255, 80, 80),
            "green": (90, 220, 120),
            "yellow": (235, 210, 80),
        }
        return colors.get(color_name, (255, 255, 255))