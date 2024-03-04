# Sudoku Generator

This Python script generates Sudoku puzzles of variable sizes and difficulty levels. It utilizes backtracking and random number generation to create unique Sudoku grids.

## Features

- Generates Sudoku puzzles of any size (e.g., 9x9, 16x16, etc.).
- Allows customization of difficulty levels by specifying the number of digits to remove.
- Saves generated Sudoku grids to a text file for later use or solving.

## How to Use

1. **Installation**:
    - Clone or download the repository.

2. **Dependencies**:
    - The script requires Python 3.x to run.
    - No external libraries are needed.

3. **Running the Script**:
    - Open a terminal or command prompt.
    - Navigate to the directory containing the script.
    - Run the script using the command:
        ```bash
        python sudoku_generator.py
        ```
    - Adjust parameters (`N` for grid size and `K` for the number of digits to remove) in the script according to your preferences.

4. **Output**:
    - The script generates a Sudoku grid and prints it to the console.
    - It also saves the generated grid to a text file named `sudoku_grid.txt` in the same directory.

## Example

```python
# Generate a 9x9 Sudoku grid with 40 digits removed
N = 9
K = 40
sudoku = SudokuGenerate(N, K)
sudoku.fillValues()
sudoku.printSudoku()
sudoku.saveToFile("sudoku_grid.txt")
