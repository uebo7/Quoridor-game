import pygame


class InputHandler:
    def __init__(self, game, renderer):
        self.game = game
        self.renderer = renderer

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.renderer.handle_click(event.pos, event.button)
            return

        if event.type != pygame.KEYDOWN:
            return

        if event.key == pygame.K_q:
            self.renderer.running = False
            return

        if event.key == pygame.K_m:
            self.renderer.mode = "move"
            return

        if event.key == pygame.K_w:
            self.renderer.mode = "wall"
            return

        if event.key == pygame.K_b:
            self.renderer.mode = "wall"
            return

        if event.key in (pygame.K_LEFT, pygame.K_a):
            self.game.move_current_player(0, -1)
        elif event.key in (pygame.K_RIGHT, pygame.K_d):
            self.game.move_current_player(0, 1)
        elif event.key == pygame.K_UP:
            self.game.move_current_player(-1, 0)
        elif event.key == pygame.K_DOWN:
            self.game.move_current_player(1, 0)
        elif event.key == pygame.K_s:
            self.game.move_current_player(1, 0)
        elif event.key == pygame.K_r:
            self.game.reset()