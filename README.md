# Tic Tac Toe Game

A two-player Tic Tac Toe implementation that runs entirely in the terminal. Players alternate turns placing `X` and `O` markers until someone wins or the board fills.

## Features
- Classic 3×3 grid with win detection across rows, columns, and diagonals.
- Randomized selection of the starting player each game.
- Input validation that prevents moves on occupied squares.
- Provided as both a Python script and a matching Jupyter notebook for interactive exploration.

## Project Files
- `MilestoneProject1.py` — ready-to-run command-line script.
- `MilestoneProject1.ipynb` — notebook version containing the same logic.

## Requirements
- Python 3.7 or newer.
- No third-party dependencies; everything uses the standard library.

## How to Play
1. Change into the `Tic-Tac-Toe-Game` directory.
2. Launch the script:
   ```bash
   python3 MilestoneProject1.py
   ```
3. Player 1 chooses to be `X` or `O`; Player 2 receives the remaining marker.
4. When prompted, enter a position (1–9) mapped as:

   ```
   7 | 8 | 9
   --+---+--
   4 | 5 | 6
   --+---+--
   1 | 2 | 3
   ```
5. Keep alternating moves until a player gets three in a row or all squares are occupied, resulting in a draw.

For a step-by-step walkthrough or experimentation, open the notebook in Jupyter:
```bash
jupyter notebook MilestoneProject1.ipynb
```

Enjoy the head-to-head matchup!
