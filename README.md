# 15 Puzzle

A terminal-based implementation of the **15 Puzzle developed in Python**.

This project was developed as part of my university studies to practice Python programming, matrix manipulation, keyboard input, randomization, and game logic.

## How It Works

The game uses a **4x4 board** containing the numbers from 1 to 15 and one empty position.

The objective is to move the tiles until they are arranged in ascending order.

The player controls the board using the arrow keys.

## Difficulty Levels

The game includes three difficulty levels:

* **Easy:** approximately 5 tiles out of position
* **Medium:** approximately 10 tiles out of position
* **Hard:** approximately 15 tiles out of position

The board is shuffled using valid movements, keeping the puzzle solvable.

## Controls

Use the arrow keys to move the empty space:

* **↑** Move Up
* **↓** Move Down
* **←** Move Left
* **→** Move Right

## Features

* 4x4 puzzle board
* Three difficulty levels
* Random board shuffling
* Shuffling using valid puzzle movements
* Keyboard controls
* Colored terminal display
* Detection of correctly and incorrectly positioned tiles
* Victory detection
* Option to play again after winning

## Project Structure

```text id="t0jy53"
15-puzzle/
│
├── src/
│   └── fifteen_puzzle.py
│
└── README.md
```

## Requirements

* Python 3
* Keyboard

Install the required dependency using:

```bash id="w28yda"
pip install keyboard
```

Or install the project dependencies using:

```bash id="mfsyfu"
pip install -r requirements.txt
```

## Usage

Run the game with:

```bash id="m0j6rv"
python src/fifteen_puzzle.py
```

Select a difficulty level and use the arrow keys to arrange the tiles in ascending order.

## Technologies

* Python
* Keyboard
* Terminal / ANSI escape codes

## Author

University project developed for programming practice.
