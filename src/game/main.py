
import pygame

from game.game_manager import GameManager
from ui.input_handler import InputHandler
from ui.render import Renderer


def main():
    pygame.init()

    game = GameManager()
    renderer = Renderer(game)
    renderer.input_handler = InputHandler(game, renderer)
    renderer.run()

    pygame.quit()


if __name__ == "__main__":
    main()
