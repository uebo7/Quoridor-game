
# Quoridor Game

## Overview

This project is a Python implementation of **Quoridor**, a strategic board game in which players race to reach the opposite side of the board while placing walls to block their opponents. Players must balance advancing toward their goal with strategically placing walls while maintaining a valid path to their destination.

The game is built with Python and Pygame, with separate modules for game logic, rendering, input handling, and utility functions. The project uses `uv` for dependency management and execution, with packaging configured through `pyproject.toml`.

## Features

### Gameplay

- Play Quoridor on a grid-based game board.
- Move players toward their respective goal edges.
- Place walls to block opponents and control movement.
- Enforce game rules for movement and wall placement.
- Prevent wall placements that eliminate all valid paths to a player's goal.

### Game Logic

- **Board Management:** Maintain the game board and its state.
- **Player Management:** Track player positions and game-related state.
- **Movement Rules:** Validate legal player movements.
- **Wall Management:** Handle wall placement and restrictions.
- **Pathfinding:** Determine whether players can still reach their goals.
- **Game Management:** Coordinate gameplay and game state.

### Graphical User Interface

- Render the board and game elements using Pygame.
- Handle player input through a dedicated input handler.
- Display game information through the user interface.
- Separate rendering, input handling, and game logic into distinct modules.

### Development Tools

- Use `uv` to manage dependencies and run the game.
- Configure project metadata and dependencies through `pyproject.toml`.
- Launch the game using `uv run quoridor`.
- Run automated tests using pytest.

## Project Structure

```text
Quoridor/
├── LICENSE
├── README.md
├── pyproject.toml
├── uv.lock
├── config.py
├── src/
│   ├── __main__.py
│   ├── config.py
│   ├── assets/
│   ├── game/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── board.py
│   │   ├── game_manager.py
│   │   ├── pathfinding.py
│   │   ├── player.py
│   │   ├── rules.py
│   │   └── wall.py
│   ├── ui/
│   │   ├── __init__.py
│   │   ├── hud.py
│   │   ├── input_handler.py
│   │   ├── menu.py
│   │   └── render.py
│   └── utils/
│       ├── __init__.py
│       └── coordinates.py
└── tests/
    ├── test_board.py
    ├── test_game_manager.py
    ├── test_movement.py
    ├── test_pathfinding.py
    ├── test_player.py
    ├── test_rules.py
    └── test_walls.py
```

The application is organized into separate packages according to responsibility:

- **`game/`** contains the core game logic, including board state, player behavior, movement rules, wall placement, and pathfinding.
- **`ui/`** contains rendering, menus, the heads-up display, and input handling.
- **`utils/`** contains shared utility functions, including coordinate-related operations.
- **`assets/`** contains game resources used by the interface.
- **`tests/`** contains automated tests for game mechanics and rules.
- **`pyproject.toml`** defines project metadata, dependencies, the build system, and the game entry point.
- **`uv.lock`** records resolved dependency versions for reproducible environments.

## Prerequisites

### Python

Python 3.13 is recommended for the current development environment.

Check your Python version:

```bash
python --version
```

Download Python from [python.org](https://www.python.org/downloads/).

### Git

Check your Git installation:

```bash
git --version
```

Download Git from [git-scm.com](https://git-scm.com/downloads).

### uv

`uv` manages the project's virtual environment, dependencies, and execution.

Check your installation:

```bash
uv --version
```

Follow the installation instructions at [Astral uv](https://docs.astral.sh/uv/).

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/uebo7/Quoridor-game.git
cd Quoridor
```

### 2. Run the Game

From the project root, run:

```bash
uv run quoridor
```

The first run will create or synchronize the project environment and install the dependencies declared in `pyproject.toml`, including Pygame.

The game will launch in its Pygame window.

### 3. Synchronize Dependencies

To set up the development environment without launching the game, run:

```bash
uv sync
```

### 4. Run the Tests

Run the automated test suite:

```bash
uv run pytest
```

To install the optional testing dependencies explicitly:

```bash
uv sync --extra test
uv run pytest
```

## Usage

After launching the game, interact with the graphical interface to play Quoridor.

The core gameplay actions include:

- **Move:** Move your player toward the opposite side of the board while following the movement rules.
- **Place Walls:** Strategically place walls to slow down opponents without blocking all valid routes to their goals.
- **Plan Routes:** Consider walls and player positions when choosing your next move.
- **Reach the Goal:** Be the first player to reach the opposite edge of the board to win.

Refer to the in-game interface for the controls supported by the current implementation.

## Architecture

The project separates gameplay responsibilities from the graphical interface.

### Game Package

The `src/game/` package contains the core game mechanics.

| Module | Responsibility |
|---|---|
| `board.py` | Represents and manages the game board. |
| `game_manager.py` | Coordinates gameplay and game state. |
| `pathfinding.py` | Checks paths and route accessibility. |
| `player.py` | Represents players and their state. |
| `rules.py` | Implements and validates game rules. |
| `wall.py` | Represents and manages walls. |
| `main.py` | Initializes and launches the game. |

### User Interface Package

The `src/ui/` package manages player interaction and presentation.

| Module | Responsibility |
|---|---|
| `render.py` | Draws the game and manages the rendering loop. |
| `input_handler.py` | Processes player input. |
| `hud.py` | Displays game information. |
| `menu.py` | Provides menu-related interface functionality. |

### Utilities Package

The `src/utils/` package provides shared functionality, including coordinate conversions and related board operations.

## Configuration and Dependencies

Project configuration is managed through `pyproject.toml`.

The project uses:

- **setuptools** as its build backend.
- **Pygame** for graphics, input, and the game window.
- **pytest** as an optional development dependency.
- **uv** for environment management and dependency installation.

The `quoridor` console command is configured through the project's script entry point:

```bash
uv run quoridor
```

The project uses a `src/` layout, with the `game`, `ui`, and `utils` packages discovered by setuptools.

## Testing

The project includes automated tests for the core game mechanics.

Run the full test suite:

```bash
uv run pytest
```

The test suite covers:

- Board behavior
- Game manager behavior
- Player movement
- Pathfinding
- Player state
- Game rules
- Wall placement and restrictions

To run a specific test file:

```bash
uv run pytest tests/test_board.py
```

For more detailed output:

```bash
uv run pytest -v
```

## Development

To contribute to development:

1. Clone the repository.
2. Run `uv sync` to install the project and dependencies.
3. Make changes to the relevant modules in `src/`.
4. Run `uv run pytest` to check for regressions.
5. Launch the game with `uv run quoridor` to verify gameplay changes.

Keep game rules and state management in the `game/` package, and keep rendering and input handling in the `ui/` package. This separation makes the project easier to test, maintain, and extend.

## License

See the `LICENSE` file in the repository for licensing terms.
