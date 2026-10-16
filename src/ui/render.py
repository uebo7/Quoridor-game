# draw the board, players, walls, and HUD

import pygame

from config import BOARD_SIZE, CELL_SIZE, WINDOW_TITLE
from ui.hud import Hud


class Renderer:
    def __init__(self, game):
        self.game = game
        self.mode = "move"
        self.panel_width = 220
        self.width = BOARD_SIZE * CELL_SIZE + self.panel_width
        self.height = BOARD_SIZE * CELL_SIZE
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(WINDOW_TITLE)
        self.clock = pygame.time.Clock()
        self.hud = Hud(game, self.panel_width)
        self.running = True
        self.input_handler = None

    def draw_board(self):
        self.screen.fill((18, 18, 18))
        self._draw_goal_rows()

        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(self.screen, (70, 70, 70), rect, 1)

        self._draw_walls()
        self._draw_players()
        self.hud.draw(self.screen, self.mode)
        pygame.display.flip()

    def _draw_goal_rows(self):
        for player in self.game.players:
            row = player.goal_row
            for col in range(BOARD_SIZE):
                rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                tint = self._goal_tint(player.color)
                pygame.draw.rect(self.screen, tint, rect)

    def _draw_players(self):
        for player in self.game.players:
            center_x = player.col * CELL_SIZE + CELL_SIZE // 2
            center_y = player.row * CELL_SIZE + CELL_SIZE // 2
            radius = CELL_SIZE // 3
            pygame.draw.circle(self.screen, self._color(player.color), (center_x, center_y), radius)

    def _draw_walls(self):
        for row, col in self.game.board.horizontal_walls:
            x = col * CELL_SIZE
            y = row * CELL_SIZE + CELL_SIZE // 2 - 5
            wall_rect = pygame.Rect(x, y, CELL_SIZE * 2, 10)
            pygame.draw.rect(self.screen, (200, 180, 120), wall_rect)

        for row, col in self.game.board.vertical_walls:
            x = col * CELL_SIZE + CELL_SIZE // 2 - 5
            y = row * CELL_SIZE
            wall_rect = pygame.Rect(x, y, 10, CELL_SIZE * 2)
            pygame.draw.rect(self.screen, (200, 180, 120), wall_rect)

    def _goal_tint(self, color_name):
        tints = {
            "blue": (50, 90, 120),
            "red": (120, 60, 50),
            "green": (50, 120, 70),
            "yellow": (120, 110, 40),
        }
        return tints.get(color_name, (80, 80, 80))

    def _color(self, color_name):
        colors = {
            "blue": (60, 120, 255),
            "red": (255, 80, 80),
            "green": (90, 220, 120),
            "yellow": (235, 210, 80),
        }
        return colors.get(color_name, (255, 255, 255))

    def handle_click(self, pos, button):
        if pos[0] >= BOARD_SIZE * CELL_SIZE or pos[1] >= BOARD_SIZE * CELL_SIZE:
            return

        col = pos[0] // CELL_SIZE
        row = pos[1] // CELL_SIZE

        if not self.game.board.in_bounds(row, col):
            return

        if self.game.game_over:
            return

        if self.mode == "move":
            self.game.move_player(row, col)
            return

        if self.mode == "wall":
            orientation = "horizontal" if button == 1 else "vertical"
            self.game.place_wall(row, col, orientation)
            self.mode = "move"

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if self.input_handler is not None:
                    self.input_handler.handle_event(event)
                else:
                    if event.type == pygame.QUIT:
                        self.running = False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.handle_click(event.pos, event.button)

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            self.running = False
                        elif event.key == pygame.K_m:
                            self.mode = "move"
                        elif event.key == pygame.K_w:
                            self.mode = "wall"

            self.draw_board()
            self.clock.tick(60)

        pygame.quit()